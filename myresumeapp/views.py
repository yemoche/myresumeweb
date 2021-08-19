from django.shortcuts import redirect, render
from .forms import ContactForm
# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def submitview(request):
    form= ContactForm(request.POST)
    if form.is_valid():
        return redirect('home')
    else:
        return render(request, 'index.html', {'form':form})