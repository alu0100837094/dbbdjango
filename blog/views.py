

# Create your views here.
# blog/views.py
from django.http import HttpResponse

def quick_test(request):
	return HttpResponse("Hello testing world!");

