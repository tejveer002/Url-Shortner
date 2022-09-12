from django.shortcuts import redirect, render
from django.http import HttpResponse
from main.models import url

# Create your views here.

def createurl(request):
    if request.method == "POST":
        full_url = request.POST.get("full_url")
        obj = url.create(full_url)
        return render(request,'main/index.html', { 
            'full_url' : obj.full_url , 
            'short_url' : request.get_host()+ '/'+ obj.short_url ,})
    
    return render(request,'main/index.html')

def routeToUrl(request ,key):
    try:
        obj = url.objects.get(short_url= key)
        return redirect(obj.full_url)
    except:
        return redirect(createurl)
#    return redirect