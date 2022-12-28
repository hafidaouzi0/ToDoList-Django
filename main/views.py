from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import ToDoList,Item
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required
# Create your views here.

#this fucntion will create our first view
@login_required(login_url='/login/')
def index(response,id):
    ls=ToDoList.objects.get(id=id)
    #we have to control pages ,  a user can't see other users todolists
    if ls in response.user.todolist.all():
        #if the condition is true then this is valid

   # ls=ToDoList.objects.get(name=name)
    #let s get our  item
    #item=ls.item_set.get(id=1)
    #return HttpResponse('<h1>%s</h1> <br> <p>%s</p>' %(ls.name,item.text))
     if response.method=="POST":
        print(response.POST)
        #post is a dictioannary that containes data from the form like ,{"name":"value"}
        #{"save":"save","c1":"clicked"}
        if response.POST.get("save"):#this means fif we're saving
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id))=="clicked":
                    item.complete=True
                else:
                    item.complete=False
                item.save()    
        elif response.POST.get("newItem"):#this means if we're adding a new item
            txt=response.POST.get("new")
            if len(txt)>2:
             ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid text")
            
     return render(response,"main/list.html",{"ls":ls})
    else:
      return render(response,"main/view.html",{})

#let's create another view
@login_required(login_url='/login/')
def v1(response):
 return HttpResponse("<h1>this is VIEW 1</h1>")

def home(response):
    return render(response,"main/home.html",{"name":"test"})

@login_required(login_url='/login/')
def create(response):
     if response.method == "POST":
        form=CreateNewList(response.POST)
        if form.is_valid():
           #now we wanna create a tododlist and save it the database for specefic user
           n=form.cleaned_data['name']
           t=ToDoList(name=n)
           t.save()
           response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
     else:
        form=CreateNewList()
     return render(response,'main/create.html',{"form":form})

#to display their own to do list for specefic users that created them 
def view(response):
 return render(response,"main/view.html",{})