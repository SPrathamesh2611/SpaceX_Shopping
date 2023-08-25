from django.shortcuts import render,HttpResponse, redirect
from SpaceX_Shopping.models import credential,cart
from django.contrib import messages
import uuid
from urllib.parse import unquote
fname=''
a=False
gname=''

# Create your views here.
def index(request):
    if fname!='' and a==True:
        return render(request,'index.html',{'a':a,'fname':fname})
    else:
        return render(request,'index.html')

def mens_shirt(request):
    global fname
    global a
    if fname!='' and a==True:
        return render(request,'mens_shirt.html',{'a':a,'fname':fname})
    else:
        return render(request,'mens_shirt.html')
    
def shirt1(request):
    global fname
    global a
    global gname
    if request.method=='POST':
        size=request.POST.get('size')
        number=int(request.POST.get('number'))
        if number>=1:
            if fname!='' and a==True:
                product_id = uuid.uuid4().hex
                user=fname
                email=gname
                photo="/static/mens_shirt/shirt 1.webp"
                name='UNISEX RAPTOR SCHEMATIC T-SHIRT'
                size=request.POST.get('size')
                number=request.POST.get('number')
                obj=cart(product_id=product_id,user=user,email=email,photo=photo,name=name,size=size,quantity=number)
                obj.save()
                details=[]
                cartv=cart.objects.all()
                for i in cartv:
                    if i.email==gname:
                        
                        details.append(i)
                
                return render(request,'cart_view.html',{'det':details,'a':a,'fname':fname,'gname':gname})
            else:
                messages.info(request,'Please Login in your account')
                return render(request, 'login.html')
        else:
            messages.info(request,'Quantity should be greater than 0')
            return render(request, 'shirt1.html')
    else:
        if fname!='' and a==True:
            return render(request, 'shirt1.html',{'a':a,'fname':fname})
        else:
            return render(request, 'shirt1.html')
    
def shirt2(request):
    global fname
    global a
    global gname
    if request.method=='POST':
        size=request.POST.get('size')
        number=int(request.POST.get('number'))
        if number>=1:
            if fname!='' and a==True:
                product_id = uuid.uuid4().hex
                user=fname
                email=gname
                photo="/static/mens_shirt/shirt 2.webp"
                name='UNISEX STARSHIP SCHEMATIC T-SHIRT'
                
                obj=cart(product_id=product_id,user=user,email=email,photo=photo,name=name,size=size,quantity=number)
                obj.save()
                details=[]
                cartv=cart.objects.all()
                for i in cartv:
                    if i.email==gname:
                        
                        details.append(i)
                
                return render(request,'cart_view.html',{'det':details,'a':a,'fname':fname,'gname':gname})
            else:
                messages.info(request,'Please Login in your account')
                return render(request, 'login.html')
        else:
            messages.info(request,'Quantity should be greater than 0')
            return render(request, 'shirt2.html')
    else:
        if fname!='' and a==True:
            return render(request, 'shirt2.html',{'a':a,'fname':fname})
        else:
            return render(request, 'shirt2.html')
        
def login(request):
    global fname
    global a
    global gname
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        cred=credential.objects.all()
        for i in cred:
            if i.email==email:
                fname=i.fname
                gname=i.email
        user=credential.objects.filter(email=email,password=password)
        if user.exists():
            a=True
            messages.info(request,"Login Succesfully")
            return render(request,'login.html',{'a':a,'fname':fname})
        else:
            messages.info(request,"Invalid Creadentials")
            return render(request,'login.html')
    else:
        fname=''
        a=False
        gname=''
        return render (request,'login.html')
    
def register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        mailv=credential.objects.filter(email=email)
        if mailv.exists():     
            messages.info(request,"User already exists, Please")
            return render(request,'register.html')
        else:
            obj=credential(fname=fname,lname=lname,email=email,password=password)
            obj.save()
            return render(request,'login.html')
    else:
        return render (request,'register.html')

def cart_view(request):
    global gname
    global fname
    
    details=[]
    cartv=cart.objects.all()
    for i in cartv:
        if i.email==gname:
            
            details.append(i)
    
    return render(request,'cart_view.html',{'det':details,'a':a,'fname':fname,'gname':gname})
# def cart_view(request):
#     details = cart.objects.all()
#     return render(request, 'cart_view.html', {'det': details})
    

# def remove_from_cart(request, product_id):
#     if request.method == 'POST':
#         # Get the cart products with matching product_id
#         cart_products = cart.objects.filter(product_id=product_id)
        
#         # Delete all matching cart products
#         cart_products.delete()
        
#         return redirect('cart_view')
#     else:
#         return HttpResponse("Invalid request method")

# def remove_from_cart(request, product_id):
#     if request.method == 'POST':
#         # Get the cart product with the matching product_id
#         try:
#             cart_product = cart.objects.get(product_id=product_id)
#             cart_product.delete()
#         except cart.DoesNotExist:
#             messages.error(request, 'Product not found in cart.')
        
#         return redirect('cart_view')
#     else:
#         return HttpResponse("Invalid request method")
def remove_from_cart(request):
    global gname
    global fname
    if request.method == 'POST':
        product_id=request.POST.get('product_id')
        cart_product = cart.objects.get(product_id=product_id)
        cart_product.delete()
        cart_product.save()        
        
        details=[]
        cartv=cart.objects.all()
        for i in cartv:
            if i.email==gname:
                
                details.append(i)
        
        return render(request,'cart_view.html',{'det':details,'a':a,'fname':fname,'gname':gname})
    else:
        details=[]
        cartv=cart.objects.all()
        for i in cartv:
            if i.email==gname:
                
                details.append(i)
        
        return render(request,'cart_view.html',{'det':details,'a':a,'fname':fname,'gname':gname})
    

        

    
