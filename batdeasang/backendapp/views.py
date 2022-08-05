from django.shortcuts import render
from .crawling import call_menu
# Create your views here.
def main(request):
    return render(request, 'main.html')

def test(request):
    a = call_menu()
    return render(request, 'test.html', {'a':a})