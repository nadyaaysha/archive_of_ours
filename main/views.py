from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Item

def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Golden Cage, Golden Tattoo.',
        'amount': 1,
        'description': 'Charities aren’t really her kind of thing.\nAt least, not until Rita showed up and ruined her principle.\nShe really doesn’t think she can get out of this one.',
        'word_count': 2672,
        'genre': 'Romance, Supernatural',
        'chara_source': 'Original (OC)',
        'products': items
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")