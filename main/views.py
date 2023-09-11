from django.shortcuts import render

# Create your views here.
'''
def show_main(request):
    context = {
        'name': 'Golden Cage, Golden Tattoo.',
        'amount': 1,
        'description': 'Charities aren’t really her kind of thing.\nAt least, not until Rita showed up and ruined her principle.\nShe really doesn’t think she can get out of this one.',
        'word_count': 2672,
        'genre': 'Romance, Supernatural',
        'chara_source': 'Original (OC)'
    }

    return render(request, "main.html", context)
'''

from django.http import HttpResponse
from django.template import loader
from .models import Item

def show_main(request):
  # mydata = Item.objects.all()
  template = loader.get_template('main.html')
  context = {
        'name': 'Golden Cage, Golden Tattoo.',
        'amount': 1,
        'description': 'Charities aren’t really her kind of thing.\nAt least, not until Rita showed up and ruined her principle.\nShe really doesn’t think she can get out of this one.',
        'word_count': 2672,
        'genre': 'Romance, Supernatural',
        'chara_source': 'Original (OC)'
    }
  return HttpResponse(template.render(context, request))