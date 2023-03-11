from django.shortcuts import render, redirect
from django.contrib.auth.models import User # to import the default user table available on django
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required

# Create your views here.






def home(request):
    return render(request,'home.html')

# the below code is implemented using normal html forms

def signup(request):
    
   if request.method=='POST':
       uname=request.POST.get('username')# fetch the username from signup from
       email = request.POST.get('email')# fetch the email id from signup page
       pass1 = request.POST.get('password1')# fetch the password 1
       pass2 = request.POST.get('password2')# fetch the confirmation password 

       if uname ==' ' and pass1==' ' and pass2=='':
           return HttpResponse("You have entered a blank space for either username or password....Please enter a valid username and password !!!")

       if pass1!=pass2:
           return HttpResponse("Password Mismatch!!!...Enter the correct password in confirm password field.")
           
       my_user = User.objects.create_user(uname,email,pass1) # this a orm here user is table and objects means it is referencing the entire table and create_user is a model to store data
       
       my_user.save() # to save the data to the database

       # return HttpResponse("User Created Successfully") instead of printing this message i am redirecting the user to login page once he finish with registration

       return redirect(login) # redirects the page to login if signup is successful

       #print(uname,email,pass1,pass2) # to test whether the user submitted data is getting read...this will be shown in terminal
    
   return render(request,'signup.html') #to display the contents present in signup.html
   
   


def login(request):

    
       


    if request.method == 'POST': # checking whether the request is post 
        usr_name = request.POST.get('username')
        pwd = request.POST.get('pass')


        if(usr_name != 'admin1'):
            return HttpResponse("You are not authorised to access admin page!!!")

        if usr_name == ' ' and pwd==' ':
            return HttpResponse("You have entered a blank space for either username or password....Please enter a valid username and password !!!")

        check = authenticate(request, username=usr_name, password=pwd) # by using django's default auth feature checking whether name presents in usr_name variable and username table are same likewise for password
        


        if check is not None:
           
           # return HttpResponse("Logged in successfully:)") #Instead of printing a message I am going to redirect the user to the student app page in the next line

           return redirect('/student/') # to redirect to a different app use the following syntax '/app/'
        else:
           return HttpResponse("Wrong Username And Password!!!...If You Don't Have An Accont Signup")    

    return render(request,'login.html')

def logout_user(request):
    logout(request) # to logout the current user
    return redirect('student_login')

@login_required
def delete_user(request):
    if request.method == 'POST':
        email = request.user.email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse("User does not exist!")
        else:
            user.delete()
            return redirect('student_login')
    else:
        return HttpResponse("Invalid Request!")

def student_login(request):

    if request.method == 'POST': # checking whether the request is post 
        usr_name = request.POST.get('username1')
        pwd = request.POST.get('pass')

        if usr_name == ' ' and pwd==' ':
            return HttpResponse("You have entered a blank space for either username or password....Please enter a valid username and password !!!")

        check = authenticate(request, username=usr_name, password=pwd) # by using django's default auth feature checking whether name presents in usr_name variable and username table are same likewise for password
        
        

        if check is not None:
           
           #return HttpResponse(usr_name+"Logged in successfully:)") #Instead of printing a message I am going to redirect the user to the student app page in the next line
        
           return redirect('profile')

           #return redirect('/student/') # to redirect to a different app use the following syntax '/app/'
        else:
           return HttpResponse("Wrong Username And Password!!!...If You Don't Have An Accont Signup")    

    return render(request,'student_login.html')


# the below code is implemented using django forms

'''def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1!=password2:
                return HttpResponse("Password Mismatch!!!...Enter the correct password in confirm password field.")
           
            my_user = User.objects.create_user(username,email,password1) # this a orm here user is table and objects means it is referencing the entire table and create_user is a model to store data
       
            my_user.save() # to save the data to the database

            # return HttpResponse("User Created Successfully") instead of printing this message i am redirecting the user to login page once he finish with registration

            return redirect(login) # redirects the page to login if signup is successful
        else:
            form =SignupForm()
    return render(request, 'signup.html',{'form':form})'''


'''def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            check = authenticate(request, username=username, password=password)
            
            if check is not None:
           
                    # return HttpResponse("Logged in successfully:)") #Instead of printing a message I am going to redirect the user to the student app page in the next line

                 return redirect('/student/') # to redirect to a different app use the following syntax '/app/'
            else:
                 return HttpResponse("Wrong Username And Password!!!...If You Don't Have An Accont Signup")    
        else:
            form = LoginForm()
            return HttpResponse("Invalid Input!!!")
    return render(request, 'login.html',{'form':form})'''

def profile(request):

    #variable = request.POST.get('username1')
    #return HttpResponse(str(variable)+"logged in")
    return render(request,'profile.html')
