from django.urls import path
from .import views


urlpatterns=[
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('',views.home,name="home"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('about',views.about,name="about"),
    path('contact',views.contactview,name="contact"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("salesproduct",views.salesproduct,name="salesproduct"),
    path("todo",views.todo,name="todo"),
    path("edit/<int:id>",views.edittodo,name="edit"),
    path("delete/<int:id>",views.delete_data,name="delete"),
    path('addcategory',views.addcategory,name="addcategory"),
    #path("postlist",views.post_list,name="postlist"),
    path("expenses",views.expenses,name="expenses"),
    path("worker_profile",views.worker_profile,name="worker_profile"),
    path('allproduct',views.allproduct,name="allproduct"),

]
