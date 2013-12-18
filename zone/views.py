# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
	return render(request, 'example.html')

def boys(request):
#	t = loader.get_template('zone/boys.html')
	return render(request, 'boys.html')

def girls(request):
	return render(request, 'girls.html')

def babies(request):
	return render(request, 'babies.html')

def agewise1(request):
	return render(request, '0-12-months.html')


