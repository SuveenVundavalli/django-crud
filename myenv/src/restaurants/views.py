from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def home(request):
#     msg = "Hello World!"
#     html_ = f'''
#     <html>
#         <head>
#             <title>Hello</title>
#         </head>
#         <body>
#             <marquee>{msg}</marquee>
#         </body>
#     </html>
#     '''
#     return HttpResponse(html_)
#     # return render(request, "home.html", {}) #response

def home(request):
    return render(request, "home.html", {"msg": "Hello World!", "var1": "Suveen"})  # response

def about(request):
    return render(request, "about.html", {"msg": "Hello World!", "var1": "Suveen"})  # response

def contact(request):
    return render(request, "contact.html", {"msg": "Hello World!", "var1": "Suveen"})  # response
