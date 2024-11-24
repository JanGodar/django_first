from django.shortcuts import render
from django.http import HttpResponse


cats_db = [
    {'id': 1, 'name': 'Page 1'},
    {'id': 2, 'name': 'Page 2'},
    {'id': 3, 'name': 'Page 3'},
]

# Create your views here.
def index(request):
    context = {'name': 'Andrey'}
    return render(request, 'firstapp/firsttemplate.html', context)


def about(request):
    return HttpResponse('About')

def show_category(request, cat_id):
    return index(request)