from django.shortcuts import render
from .models import Cart
from django.http import HttpResponseRedirect 
from product.models import Product

# Create your views here.
def index(request):  
    if request.method == 'POST':   
        # return request.POST   
        post_data = request.POST
        # return post_data
        new_cart = Cart(product_id = post_data['product_id'],customer_id = 1,qty = 1,created_at = '2020-01-01')
        new_cart.save()
        return HttpResponseRedirect('/cart')
    else:
        print("in the get request")
        cart = Cart.objects.all()
        for cart in cart:
            cart.product=Product.objects.get(cart.product_id)
        context = {
            'cart' : cart
        }
        return render(request,'cart_index.html',context)