# Create your views here.
# blog/views.py
from django.http import HttpResponse

def quick_test(request):
	return HttpResponse("Hello testing world!");


from django.shortcuts import render_to_response
 
def quick_test(request):
	return render_to_response("blog.html", {})

