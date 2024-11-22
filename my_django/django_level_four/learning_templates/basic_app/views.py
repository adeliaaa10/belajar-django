from django.shortcuts import render

# Create your views here.

# halaman index 
def index(request):
    return render(request, 'basic_app/index.html')

# halaman profile
def profile(request):
    return render(request, 'basic_app/profile.html')

# halaman contact 
def contact(request):
    return render(request, 'basic_app/contact.html')
