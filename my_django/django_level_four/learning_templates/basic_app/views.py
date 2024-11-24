from django.shortcuts import render

# Create your views here.

# halaman index 
def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'basic_app/index.html', context=context_dict)

# halaman profile
def profile(request):
    return render(request, 'basic_app/profile.html')

# halaman contact 
def contact(request):
    return render(request, 'basic_app/contact.html')
