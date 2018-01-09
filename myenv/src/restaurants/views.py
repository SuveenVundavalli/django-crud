from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    msg = "Hello World!"
    html_ = f'''
    <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
            <marquee>{msg}</marquee>
        </body>
    </html>
    '''
    return HttpResponse(html_)
    # return render(request, "home.html", {}) #response

