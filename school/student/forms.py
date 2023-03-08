from django import forms

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label='Name')


class SearchForm(forms.Form):
    username =forms.CharField(max_length=50,required=True,label='Name')