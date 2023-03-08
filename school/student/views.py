from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Students
from django.http import HttpResponse
from .forms import AddUserForm
from .forms import SearchForm

# the below code is doesn't contain filter option to check whether a name already exists in the db or not without django forms

'''def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # do something with the username, such as save it to the database
        user = Students(username=username)
        user.save()  # Make sure to save the user object
        messages.success(request, f"Student '{username}' added successfully.")
        return HttpResponse('Record Submitted Successfully :)')
    else:
        return render(request, 'index.html')'''

# the below code implements the add user option using django forms


def add_user_view(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            username = form.cleaned_data['username']
            user = Students(username=username) # here students is the database
            user.save()
            return HttpResponse('Record Submitted Successfully :)')
            # ...
    else:
        form = AddUserForm()
    return render(request, 'index.html', {'form': form})



# below code filters the already existing name in the db directly without having any specific button to filter


'''def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_exists = Students.objects.filter(username=username).exists()
        if user_exists:
            message = 'Username already exists!'
        else:
            user = Students(username=username)
            user.save()
            message = 'Username submitted successfully!'
        context = {'message': message}
        return HttpResponse('Record Submitted Successfully :)')
    else:
        return render(request, 'index.html')'''


# this below code is specifically created for handling the search option without django forms


'''def search(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user_exists = Students.objects.filter(username=username).exists()
        context = {'username': username, 'user_exists': user_exists}
        return render(request, 'search.html', context)
    else:
        return HttpResponse('The username does not exist')'''

# the below code is for implementing the search feature using django froms with post method

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            username = form.cleaned_data['username'] # here we are checking whether the user data is safe or malicious code
            user_exists = Students.objects.filter(username=username).exists()
            context = {'username': username, 'user_exists': user_exists}
            return render(request, 'search.html', context) # passing the context to templates
            # ...
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})
