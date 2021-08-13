
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def signin(request):
    if request.method == 'GET':
        x=AuthenticationForm()
        return render(request, 'login.html',{'form':x})
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
        return render(request,'dashboard.html')

def edittodo(request,id):
    if request.method =='POST':
        stu= Todo_model.objects.get(pk=id)
        form=todo_Form(request.POST,instance=stu)
        if form.is_valid():
            form.save()
        
    else:
        e=Todo_model.objects.get(pk=id)
        form=todo_Form(instance=e)
    return render(request,'todo.html',{'form':form})


 

def delete_data(request,id):
     pi=Todo_model.objects.get(pk=id)
     pi.delete()
     return redirect('todo')

       
@login_required(login_url='signin')
def dashboard(request):
    if request.method=='GET':
        return render(request,'dashboard.html')


def home(request):
    list=Product.objects.all().order_by("-id")
    return render(request,'home.html',{'product_list':list})

def about(request):
    return render(request,'about.html')

def contactview(request):
    return render(request,'contact.html')

# for signout
def signout(request):
    logout(request)
    return redirect('signin')

    
@csrf_exempt
def addproduct(request):
    form = Product_Form(request.POST,request.FILES,None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True) 
        return redirect('addproduct')
    else:
        productlist=Product.objects.all()
        form = Product_Form()
        return render(None,'addproduct.html', {'form':form,'productlist':productlist})

    
@csrf_exempt
def salesproduct(request):
    form = sales_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
        return redirect('salesproduct')
    else:
       
        form = sales_Form()
        return render(None,'salesproduct.html', {'form':form})

@csrf_exempt
def worker_profile(request):
    form = worker_profile_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True) 
        return redirect('worker_profile')
    else:
        worker_list =Worker.objects.all()
        form = worker_profile_Form()
        return render(None,'worker_profile.html', {'form':form,'worker_list':worker_list})

@csrf_exempt
def addcategory(request):
    form = Category_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
        return redirect('addcategory')
    else:
        categories=Category.objects.all()
        form = Category_Form()
        return render(None,'addcategory.html', {'form':form,'allcategories':categories})

@csrf_exempt
def expenses(request):
    form = Expenses_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
        return redirect('expenses')
    else:
        expenses_list=Daily_Expenses.objects.all()
        form = Expenses_Form()
        return render(None,'expenses.html', {'form':form,'expenses_list':expenses_list})

@csrf_exempt
def todo(request):
    y=todo_Form(request.POST)
    if request.method == 'POST':
        if y.is_valid():
            data=y.save(commit=False)
            data.user=request.user
            data.save()
        return  redirect('todo')
    else:
        y=todo_Form()
        todo_out=Todo_model.objects.filter(user=request.user,complete=False)
        return render(request,"todo.html",{"form":y,"todo_out":todo_out})

def allproduct(request):
    categories=Category.objects.all()
    return render(request,'all_product.html',{'allcategories':categories})
    


# def post_list(request):
#     post_list=Todo_model.objects.all().order_by("-id")
#     paginator=Paginator(post_list,3)
#     page=request.GET.get('page')
#     try:
#         posts=paginator.page(page)
#     except PageNotAnInteger:
#         posts=paginator.page(1)
#     except EmptyPage:
#         posts=paginator.page(paginator.num_pages)
#     return render(request,'todo.html',{'posts':posts})