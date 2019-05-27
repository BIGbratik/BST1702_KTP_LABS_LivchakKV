#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	#return HttpResponse(u'Привет, мир!'.encode('1251'),mimetype="text/plain")
	#return HttpResponse(u'Привет, мир!'.encode('1251'))
	#return render(request,'index.html',{})
    return render(request,'static_handler.html',{})
    
