from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={
        "product1":'MAC',
        "product2":'DELL',
        "product3":'ASUS',
    }
    return render(request,'producttemplates/products.html',product_dict)
def shoes(request):
    product_dict={
        "product1":'REEBOK',
        "product2":'ADIDAS',
        "product3":'CAMPUS',
    }
    return render(request,'producttemplates/products.html',product_dict)
def toys(request):
    product_dict={
        "product1":'CAR',
        "product2":'SWORD',
        "product3":'VIDEO GAME',
    }
    return render(request,'producttemplates/products.html',product_dict)
def index(request):
    return render(request,'producttemplates/index.html')