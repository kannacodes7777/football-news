from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406407266',
        'name': 'Hillary Elizabeth',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
