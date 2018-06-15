from django.shortcuts import render
from django.http import HttpResponse

import pymongo

uri = "mongodb://user:admin123@ds115352.mlab.com:15352/sorokin_sad"
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    data = { 'greetings': [
                {"test": "hold"}, 
                {"test": "my beer"}
                ]
            }
    return render(request, 'index.html', data)


def db(request):

    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

    thingies = db['Thingies']
    first = thingies.find_one()
    data = {
            'greetings': [
                {"test": first['Description']}, 
                {"test": first['Name']}
            ]
        }
    return render(request, 'index.html', data )


