from django.shortcuts import render, redirect
from django.forms.models import model_to_dict

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = list(Phone.objects.values())
    sort_type = request.GET.get("sort")
    if sort_type == "name":
        phones.sort(key=lambda phone: phone["name"])
    elif sort_type == "min_price":
        phones.sort(key=lambda phone: phone["price"])
    elif sort_type == "max_price":
        phones.sort(reverse=True, key=lambda phone: phone["price"])

    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = model_to_dict(Phone.objects.filter(slug=slug).first())
    context = {"phone": phone}
    return render(request, template, context)
