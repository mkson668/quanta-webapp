from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args,**kwargs):
    print(request)
    # return HttpResponse("<h1>new home page </h1>") 
    # httprespose transform html string into display
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "my_text" : "BC, Vancouver",
        "my_number" : 7788888888,
        "my_list"   : ["Canada" , "V7B 3U9"],
    }
    return render(request, "contact.html", my_context)