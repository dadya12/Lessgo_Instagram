from django.contrib.auth import get_user_model
from django import forms


class MyUserCreationForm(forms.ModelForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'avatar', 'password', 'first_name', 'info', 'phone', 'gender']


class MyUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'email', 'avatar', 'info', 'phone', 'gender']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150, required=False, label='Search')
