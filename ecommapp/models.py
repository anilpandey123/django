from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo_model(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date_added = models.DateField(auto_now_add=True)
    date_complete = models.DateTimeField(auto_now_add=False)
    complete = models.BooleanField()
    important = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Quantity_in(models.Model):
    measurement_type=models.CharField(max_length=100)

    def __str__(self):
        return self.measurement_type

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200,null=True,blank=True)
    joined_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title= models.CharField(max_length=200)
    slug= models.SlugField( unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="products")
    marked_price= models.PositiveIntegerField()
    selling_price= models.PositiveIntegerField()
    description=models.TextField()
    warranty=models.CharField(max_length=200,null=True,blank=True)
    view_count=models.PositiveIntegerField(default=0)
    quantity=models.PositiveIntegerField()
    quantity_in=models.ForeignKey(Quantity_in,on_delete=models.CASCADE)
    source=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Cart(models.Model):
    customer=models.ForeignKey(Customer,models.SET_NULL,null=True,blank=True)
    totals=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "Cart: " +str(self.id)

class CartProduct(models.Model):
    cart =models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    rate=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    subtotal=models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " +str(self.cart.id) + "CartProduct" +str(self.id)


ORDER_STATUS=(
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("On the way","On the way"),
    ("Order Completed","Order Completed"),
    ("Order Canceled","Order Canceled"),

)

class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    order_by=models.CharField(max_length=200)
    shipping_address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(null=True,blank=True)
    subtotal=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    order_status=models.CharField(max_length=50,choices=ORDER_STATUS)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "order: " +str(self.id)



class Worker(models.Model):
    worker_name=models.CharField(max_length=200)
    product_name=models.CharField(max_length=200)
    totalamount=models.PositiveIntegerField()
    advance_amount=models.PositiveIntegerField(null=True,blank=True)
    remarks=models.CharField(max_length=200,null=True,blank=True)
    complete=models.BooleanField()
    quantity=models.PositiveIntegerField()
    quantity_in=models.ForeignKey(Quantity_in,on_delete=models.CASCADE)


    def __str__(self):
        return self.worker_name


class Expenses_type(models.Model):
    worker=models.ForeignKey(Worker,models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.product.title

class Daily_Expenses(models.Model):
    title=models.CharField(max_length=100)
    expenses_type=models.ForeignKey(Expenses_type,models.SET_NULL,null=True,blank=True)
    amount=models.PositiveIntegerField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Sales(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    customer_name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,models.SET_NULL,null=True,blank=True)
    rate=models.PositiveIntegerField()
    description=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField()
    quantity_in=models.ForeignKey(Quantity_in,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title




