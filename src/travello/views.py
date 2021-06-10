from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # dest1 = Destination()
    # dest1.name = 'Istanbul'
    # dest1.price = 750
    # dest1.img = 'destination_1.jpg'
    # dest1.desc = 'Free turkey for all!!!'
    # dest1.offer = False
    #
    #
    # dest2 = Destination()
    # dest2.name = 'America'
    # dest2.price = '990'
    # dest2.img = 'destination_2.jpg'
    # dest2.desc = 'People will shoot your balls!!'
    # dest2.offer = True
    #
    #
    # dest3 = Destination()
    # dest3.name = 'India'
    # dest3.price = 450
    # dest3.img = 'destination_3.jpg'
    # dest3.desc = 'Get your covid for free!!'
    # dest1.offer = False
    #
    # context = {'dest1': dest1, 'dest2':dest2, 'dest3':dest3}

    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()


    return render(request, 'index.html', {'dests': dests})
