from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    # gets all product
    product_objects = Products.objects.all()

    # add search, item_name being the name on the input_field
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None: 
        product_objects = product_objects.filter(title__icontains=item_name)
    
    # add pagination import paginator
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})


#equalled id or the latter is the argument for the param passed in the fxn

def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html',{'product_object': product_object})
    
def checkout(request):
    return render(request, 'shop/checkout.html')