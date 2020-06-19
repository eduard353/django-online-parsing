from django.shortcuts import render

def dashboard_view(request):

    return render(request, 'vitrina/dashbord.html')

def parsers_view(request):

    return render(request, 'vitrina/parsers.html')

def data_view(request):

    return render(request, 'vitrina/data.html')

