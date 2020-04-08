from django import forms
from django.contrib.auth.models import User
from .models import *

#here we add forms

class UserCreationForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'class':"input--style-2",'type':"text",'placeholder':"Username",'name':"Username"}))
    userfirstname = forms.CharField(widget= forms.TextInput(attrs={'class':"input--style-2",'type':"text",'placeholder':"FirstName",'name':"Firstname"}))
    userlastname= forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-2",'type':"text",'placeholder':"LastName",'name':"Lastname"}))
    usercontact = forms.IntegerField(widget=forms.TextInput(attrs={'class':"input--style-2",'type':"text",'placeholder':"Contact",'name':"Contact"}))
    userpassword = forms.CharField(widget= forms.TextInput(attrs={'class':"input--style-2",'type':"password",'placeholder':"Password",'name':"Password"}))
    userconfirmpassword = forms.CharField(widget= forms.TextInput(attrs={'class':"input--style-2",'type':"password",'placeholder':"Confirm password",'name':"Confirm password"}))
    usermail = forms.EmailField(widget = forms.EmailInput(attrs={'class':"input--style-2",'type':"text",'placeholder':"Mail",'name':"Mail"}))
    userDoB= forms.CharField(widget= forms.TextInput(attrs={'class':"input--style-2 js-datepicker", 'type':"text", 'placeholder':"Birthdate", 'name':"birthday"}))
    userlocation = forms.CharField(widget= forms.TextInput(attrs={'class':"input--style-2", 'type':"text", 'placeholder':"Your Location(City,State)", 'name':"Location"}))
    usergender = forms.CharField(widget = forms.TextInput(attrs={'class':"input--style-2", 'type':"text", 'placeholder':"Gender", 'name':"Gender"}))


class BookForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields= ['bookname', 'bookdescription' ,'bookimage','bookimage0','bookimage1','bookimage2','bookauthor']


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':"input--style-2",'type':"text",'placeholder':"Username",'name':"Username"}))
    password = forms.CharField(widget= forms.TextInput(attrs={'class':"input--style-2",'type':"password",'placeholder':"Password",'name':"Password"}))



class BookAvailableRequest(forms.Form):
    reason = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','id':'exampleFormControlTextarea1', 'row':"10", 'placeholder':'why you need this book..?'}))



class SearchABook(forms.Form):
    query = forms.CharField(widget = forms.TextInput(attrs={'class':"form-control mr-sm-2 bg-dark",'type':"search",'placeholder':"Search", 'aria-label':"Search"}))



class RequestForm(forms.Form):
    askedBookname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'exampleFormControlTextarea1', 'row':"20", 'placeholder':'Name the book..?'}))
