from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args,**kwargs):
    print(request)
    # return HttpResponse("<h1>new home page </h1>") 
    # httprespose transform html string into display
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    print(request)
    my_context = {
        "my_text" : "this is some text i want",
        "my_number" : 69,
        "my_list" : [12134, 231423, 3435246],
    }
    return render(request, "contact.html", my_context)