# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.http import Http404
from django.http import HttpResponse


def index(request):		
 return render(request, 'index/main.html', {})

#def main(request):
# return render(request,'index/main.html',{})

def fun(request):
 	#var ob = JSON.parse(data);
 	#d=0; 
 	#return HttpResponse(d);
 	print("yes1")
 	if request.method == "GET":
 	    if request.GET.get("typed_question"):
 	        points = request.GET.get("typed_question")
 	        print("yes2")
 	data = {foo:'bar'};
 	console.log("hi")
 	render(request,'index/main.html',data)


def returnjson(request):
    print("yes1")
    if request.method == "GET":
        if request.GET.get("typed_question"):
            points = request.GET.get("typed_question")
            print("yes2")
            context = {'message': "any message"}
            return HttpResponse(template.render(context, request))
