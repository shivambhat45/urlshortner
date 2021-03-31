from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid 
from shortner import models
# Create your views here.
def index(request):
    return render(request,'shortner/index.html')
    # return HttpResponse("Hello World")

def create(request):
    if request.method=='POST':
        link=request.POST['link']
        uid=str(uuid.uuid4())[:5]
        new_url=models.Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(request,pk):
    url_details=models.Url.objects.get(uuid=pk)
    return redirect(url_details.link)
