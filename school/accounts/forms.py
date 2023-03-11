from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=155, required=True)
    password = forms.CharField(widget=forms.PasswordInput)# for getting password input usind django forms

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise forms.ValidationError("Username cannot contain blank spaces.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if ' ' in password:
            raise forms.ValidationError("Password cannot contain blank spaces.")
        return password


class SignupForm(forms.Form):
    username = forms.CharField(max_length=155, required=True)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise forms.ValidationError("Username cannot contain blank spaces.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if ' ' in email:
            raise forms.ValidationError("Email id cannot be blank")
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        if ' ' in password1:
            raise forms.ValidationError("Password cannot contain blank spaces.")
        return password1
    
    def clean_password(self):
        password2 = self.cleaned_data.get('password2')
        if ' ' in password2:
            raise forms.ValidationError("Password cannot contain blank spaces.")
        return password2
    


