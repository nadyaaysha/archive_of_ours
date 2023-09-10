from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Golden Cage, Golden Tattoo.',
        'amount': 2672,
        'description': 'Charities aren’t really her kind of thing. At least, not until Rita showed up and ruined her principle. She really doesn’t think she can get out of this one.'
    }

    return render(request, "main.html", context)