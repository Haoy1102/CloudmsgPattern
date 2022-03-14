from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def hello(request):
    return render(request,"PYC01-HTMLJSDemo.html")
#render()是一个打包函数，第一个参数是request，第二个参数是页面
