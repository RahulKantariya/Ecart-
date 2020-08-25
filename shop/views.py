from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import product, Contact , Orders ,Orderupdate
from math import ceil
import json
#from django.contrib import auth
#from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User,auth
#from django.contrib import messages



# Create your views here.


def index(request):
    allProds = []
    catprods = product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.catagory.lower():
        return True
    else:    
        return False

def search(request):
    query=request.GET.get('search')
    allProds = []
    catprods = product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(catagory=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    if len(allProds) == 0 or len(query)<4:
        params={'msg':"Please make sure to enter relevent search"}
    return render(request, 'shop/search.html', params)
   

def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')

        try:
           order= Orders.objects.filter(order_id=orderid,email=email)
           if len(order)>0:
              update=Orderupdate.objects.filter(order_id=orderid)
              updates=[]
              for item in update:
                  updates.append({'text':item.update_desc,'time':item.timestamp})
                  response =json.dumps([updates,order[0].items_json],default=str)
              return HttpResponse (response)
           else:
             return HttpResponse ('{}')
        except Exception as e:
            return HttpResponse ('{}')
    return render(request, 'shop/tracker.html')







def prodview(request,myid):
    prod = product.objects.filter(id= myid)
    return render(request, 'shop/prodview.html',{'product':prod[0]})



def checkout(request):
    if request.method == "POST":
        items_json=request.POST.get('itemsjson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " +request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders( items_json=items_json, name=name, email=email, phone=phone, address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        update = Orderupdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank  = True
        id = order.order_id
        return render(request, 'shop/checkout.html',{'thank':thank,'id':id})
    return render(request, 'shop/checkout.html')



def login(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','') 

        user = auth.authenticate(username=username,password=password)
    
        if user is not None:
           auth.login(request,user)
           return redirect('/shop')

        else:
          print("invalid user")
             
    else:
      return render(request,'shop/login.html')


def signup(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')   
        user=User.objects.create_user(username=name,email=email,password=password)
        user.save()
    return render(request,'shop/signup.html')    