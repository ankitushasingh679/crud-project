from mysqlcrud1app.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets={
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'umail': forms.EmailInput(attrs={'class': 'form-control'}),
            'upassword': forms.TextInput(attrs={'class': 'form-control'}),
        }
