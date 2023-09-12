from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Inventory App', 
        'name': 'Adrasa Cantya Salaka',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)