from datetime import datetime

from django.shortcuts import render

# Create your views here.

def home(request):
    data = {
        'title': 'Welcome to My Website',
        'description': 'This is a sample description for practicing template filters.',
        'items': [
            {'name': 'Item 1', 'price': 10.50},
            {'name': 'Item 2', 'price': 20.75},
            {'name': 'Item 3', 'price': 15.00},
        ],
        'date': datetime.now(),
        'value': 12345.67,
        'itemList': ['cricket','football','tennis'],
        'numlist': [4,5,6,7,8,9,10],
    }
    return render(request, 'first_app/home.html' , data)