from django import forms

class userForm(forms.Form):
    userName = forms.CharField(max_length=30,label='', widget=forms.TextInput(attrs={'id' : 'userName'}))
    userEmail = forms.EmailField(max_length=60, label='', widget=forms.EmailInput(attrs={'id' : 'email'}))
    password = forms.CharField(max_length=30, label='', widget=forms.PasswordInput(attrs={'id':'password'}))
    conformPassword = forms.CharField(max_length=30, label='', widget=forms.PasswordInput(attrs={'id':'confpassword'}))



class userLoginForm(forms.Form):
    userEmail = forms.EmailField(max_length=60, label='', widget=forms.EmailInput(attrs={'id' : 'email'}))
    password = forms.CharField(max_length=30, label='', widget=forms.PasswordInput(attrs={'id':'password'}))