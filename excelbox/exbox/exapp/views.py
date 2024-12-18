from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Totalsolutions

@login_required
def home(request):
 return render(request, "home.html", {})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("exapp:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

def totalsolutions(request):
    # Get search query parameters
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', 'all')
    
    # Filter the products based on the search query and category
    products = Totalsolutions.objects.all()

    if search_query:
        products = products.filter(application__icontains=search_query)
    
    if category_filter != 'all':
        products = products.filter(category=category_filter)
    
    context = {
        'products': products
    }
    return render(request, 'totalsolutions.html', context)
