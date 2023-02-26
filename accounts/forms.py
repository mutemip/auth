from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# signup form
class NewUserForm(UserCreationForm):
    STAFF_STATUS = (
        ("True", "True"),
        ("False", "False")
    )
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField()

    


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.is_staff = self.cleaned_data['is_staff']

        if commit:
            user.save()
        return user
