from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
from .related_product.context import Context
from .related_product.category_based_strategy import CategoryBaseStrategy
from .related_product.transaction_strategy import TransactionBaseStrategy



# Create your views here.
def index(request):

    products = Product.objects.all().order_by('-id')
    context = { 
        'page_title' : "This is the page title",
        'another_content' : "This is the another content",
        'products' : products
    }
    return render(request,'index.html',context)

def detail(request,product_id):
    product = Product.objects.get(id=product_id)

    RP_Context = Context(CategoryBaseStrategy())
    product_list = RP_Context.get_related_product(product)
    context={
        'page_title' : "This is detail page",
        'product' : product,
        'related_Product' : product_list
    }
    return render(request,'details.html',context)

def create(request):  
    if request.method == 'POST':        
        post_data = request.POST
        new_product = Product(name = post_data['name'],description = post_data['description'],category = post_data['category'],created_at = '2020-01-01')
        new_product.save()
        return HttpResponseRedirect('/product')
    else:
        print("in the get request")
        return render(request,'create.html')
    