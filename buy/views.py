from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
    text_var = 'This is my grocery buying app'
    return HttpResponse(text_var)

# c_slug is a category
def allProdCat(request,c_slug=None):
    cat_page = None
    products_list = None
    if c_slug != None:
        cat_page = get_object_or_404(Category,slug = c_slug)
        products_list = Product.objects.filter(category = cat_page,available = True)
    else:
        products_list = Product.objects.all().filter(available= True)
    paginator = Paginator(products_list,4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request,'buy/category.html',{'category':cat_page,'products':products})



def allProducts(request, c_slug, p_slug):
    try:
        product = Product.objects.get(category__slug= c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'buy/product_detail.html',{'product':product})



def signupView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			signup_user = User.objects.get(username=username)
			customer_group = Group.objects.get(name='Customer')
			customer_group.user_set.add(signup_user)
	else:
		form = SignUpForm()
	return render(request, 'accounts/signup.html', {'form':form})


def signinView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('buy:allProdCat')
			else:
				return redirect('signup')
	else:
		form = AuthenticationForm()
	return render(request,'accounts/signin.html', {'form':form })


def signoutView(request):
	logout(request)
	return redirect('signin')
