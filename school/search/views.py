from django.shortcuts import render
from student .models import Students # importing student db
from django.http import JsonResponse
# Create your views here.:

def index(request):
    return render(request,'dropdown.html')



def get_names(request):
    search = request.GET.get('search')
    payload = []

    if search:
        objs = Students.objects.filter(username__startswith = search)# changed name to username

        for obj in objs:
            payload.append({
                'name' : obj.username # here i am using username since i have created the same in student models 
            })

    return JsonResponse({
        'status' : True,
        
        'payload' : payload
    })