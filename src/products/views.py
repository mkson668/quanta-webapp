from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    """ context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price,
    } """
    context = {
        'object' : obj,
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    # render form out
    my_form = RawProductForm()
    # check request method and save data
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            # this is what we are actually sending from form after validation
            print(my_form.cleaned_data)
            # ** turns the map into separate arguments func foo(a1, a2, a3 ...)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form' : my_form,
    }
    return render(request, "products/product_create.html", context)

""" def product_create_view(request):
    print(request.POST)
    if request.method == 'POST':
        title = request.POST.get('title')
    # Product.objects.create(title=title...)
    context = {}
    return render(request, "products/product_create.html", context)
 """

""" def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm(request.POST or None)
    context = {
        'form' : form,
    }
    return render(request, "products/product_create.html", context) """