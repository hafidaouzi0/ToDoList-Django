#in here we gonna define the paths to our different webPages
from django.urls import path
from . import views

urlpatterns=[ 
    path("<int:id>",views.index,name="index_id"),
    #path("<str:name>",views.index,name="index_name"),
    path("v1/",views.v1,name="v1"),
    path("",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("home/",views.home,name="home"),
    path("view/",views.view,name="view"),
]