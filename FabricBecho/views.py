from django.shortcuts import render
from dashboard.models import Product
from advertisement.models import Advertisement
from featured_seller.models import FeaturedSeller
from large_banner.models import LargeBanner
from home_banner.models import HomeBanner
from category.models import Category
from math import ceil

def index(request):
    allProds = []
    prod = Product.objects.all()
    homebanner = HomeBanner.objects.all()
    featured_seller = FeaturedSeller.objects.all()
    large_banner = LargeBanner.objects.all()
        
    featured = Product.objects.filter(featured_product='Yes')

    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(0, nSlides), nSlides])
    
    params = {'allProds':allProds, 'featured':featured, 'ads':homebanner, 'fs':featured_seller, 'lb':large_banner}
    return render(request, 'index.html', params)

def searchMatch(query, item):
    if query.lower() in item.product_name.lower() or query.lower() in item.category.lower() or query.lower() in item.seller_name.lower() or query.lower() in item.desc.lower() or query.lower() in item.subcategory.lower():
        return True
    else:
        return False
 
def search(request):
    ads = Advertisement.objects.all()
    featured_seller = FeaturedSeller.objects.all()
    if request.method == 'POST':
        searched = request.POST['search']
        print(searched)
        
        productsTemp = Product.objects.all()
        allProds = []
        prod=[item for item in productsTemp if searchMatch(searched, item)]
        
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        
        allProds.append([prod, range(0, nSlides), nSlides])
    
        params = {'allProds':allProds, 'ads':ads, 'fs':featured_seller}
        
        return render(request, 'search.html', params)

    else:
        return render(request, 'search.html')
    
def allproducts(request):
    allProds = []
    c=[]
    prod = Product.objects.all()
    ads = Advertisement.objects.all()
    
    featured = Product.objects.filter(featured_product='Yes')
    category = Category.objects.values('name').distinct()
    
    for i in category:
        temp = {}
        temp['name'] = i['name']
        l = []
        sb = Product.objects.filter(category=i['name']).values('subcategory').distinct()
        for j in sb:
            if j['subcategory'] != '':
                l.append(j['subcategory'])
        temp['sb'] = l
        c.append(temp)
    
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(0, nSlides), nSlides])
    
    params = {'allProds':allProds, 'featured':featured, 'ads':ads, 'categories':c}
    return render(request, 'allProducts.html', params)
    
def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "prodView.html", {'product':product[0]})

def quote(request, myid):
    print(myid,'quote')
    product=Product.objects.filter(id=myid)
    return render(request, "quote.html", {'product':product[0]})

def categoryView(request, icategory):
    allProds = []
    c=[]
    # prod = Product.objects.all()
    ads = Advertisement.objects.all()
    
    featured = Product.objects.filter(featured_product='Yes')
    prod = Product.objects.filter(category=icategory)
    category = Category.objects.values('name').distinct()
    
    for i in category:
        temp = {}
        temp['name'] = i['name']
        l = []
        sb = Product.objects.filter(category=i['name']).values('subcategory').distinct()
        for j in sb:
            if j['subcategory'] != '':
                l.append(j['subcategory'])
        temp['sb'] = l
        c.append(temp)
    
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(0, nSlides), nSlides])
    
    params = {'allProds':allProds, 'featured':featured, 'ads':ads, 'categories':c}
    return render(request, 'allProducts.html', params)
   
def subcategoryView(request, icategory, isub):
    allProds = []
    c=[]
    # prod = Product.objects.all()
    ads = Advertisement.objects.all()
    
    featured = Product.objects.filter(featured_product='Yes')
    prod = Product.objects.filter(category=icategory, subcategory=isub)
    category = Category.objects.values('name').distinct()
    
    for i in category:
        temp = {}
        temp['name'] = i['name']
        l = []
        sb = Product.objects.filter(category=i['name']).values('subcategory').distinct()
        for j in sb:
            if j['subcategory'] != '':
                l.append(j['subcategory'])
        temp['sb'] = l
        c.append(temp)
    
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(0, nSlides), nSlides])
    
    params = {'allProds':allProds, 'featured':featured, 'ads':ads, 'categories':c}
    return render(request, 'allProducts.html', params)
   
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacyPolicy(request):
    return render(request, 'privacyPolicy.html')

def termsAndConditions(request):
    return render(request, 'termsCondition.html')

def returnPolicy(request):
    return render(request, 'returns.html')


def ads(request):
    return render(request, 'ads.html')