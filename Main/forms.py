from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label = "List Name: " , max_length = 100)
    check = forms.BooleanField(label = "Complete" , required = False)