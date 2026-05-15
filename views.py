from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 0.15

def index(request):
    return render(request, "taxapp/index.html")

def calculate(request, number):
    total = number + (number * tax_rate)
    return HttpResponse(f"Price after tax: {total}")

def taxrate(request):
    return render(request, "taxapp/taxrate.html", {"tax_rate": tax_rate})
