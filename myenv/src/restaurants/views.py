from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

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
    context = {
        "msg": "Hello World!",
        "var1": "Suveen"
    }
    return render(request, "home.html", context)  # response


def about(request):
    return render(request, "about.html", {})  # response


def contact(request):
    return render(request, "contact.html", {})  # response


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        print(context)
        context = {
            "msg": "Hello World!",
            "var1": "Suveen"
        }
        return context
