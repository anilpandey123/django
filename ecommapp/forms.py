from django import forms
from .models import *

class Product_Form(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    source=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Category=forms.ModelChoiceField(queryset=Category.objects.all())
    image=forms.ImageField
    title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    marked_price=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    selling_price=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    warranty=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    view_count=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model =Product
        fields =['title','slug','category','source','quantity','quantity_in','image','description','marked_price','selling_price','warranty','view_count']


class sales_Form(forms.ModelForm):
    quantity=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model =Sales
        fields=['customer_name','quantity','product']


class DateInput(forms.DateInput):
    input_type="date"
            

class todo_Form(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    class Meta:
        model =Todo_model
        fields=['title','description','complete','important','date_complete']
        widgets ={
        'date_complete':DateInput()
    }

class Category_Form(forms.ModelForm):
    class Meta:
        model =Category
        fields =['title','slug']

class DateInput(forms.DateInput):
    input_type="date"

class Expenses_Form(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model =Daily_Expenses
        fields =['title','amount','expenses_type']
        widgets ={
            'date':DateInput()
        }

class worker_profile_Form(forms.ModelForm):
    totalamount=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    advance_amount=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    worker_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    remarks=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Worker
        fields =['worker_name','product_name','totalamount','advance_amount','quantity','remarks','complete','quantity_in']      



