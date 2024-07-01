from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    content="""
    <div style='width:100%; height:100vh; display:flex; justify-content:center; align-items:center'>
    <h1  style='color:green;'>django</h1>
    </div>
    """
    return HttpResponse(content)