from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm,PasswordChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()




class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100,widget=forms.TextInput())
    second_name = forms.CharField(max_length=100, widget=forms.TextInput())
    username = forms.CharField(max_length=100,widget=forms.TextInput())
    is_admin = forms.CharField(max_length=100,disabled=True,required=False,widget=forms.CheckboxInput())
    is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput())
    is_staff = forms.CharField(max_length=100,disabled=True,required=False,widget=forms.CheckboxInput())
    is_superuser = forms.CharField(max_length=100,disabled=True,required=False,widget=forms.CheckboxInput())


    class Meta:
        model = User
        fields = ('username','email','first_name','second_name','is_admin','is_staff','is_active','is_superuser')


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField
    new_password1 =  forms.CharField(widget=forms.PasswordInput)
    new_password2 =  forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2',)

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email','username' ,'first_name','second_name','password', 'is_active', 'is_admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]





class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = ['email','username','first_name','second_name']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'second_name': forms.TextInput(attrs={'placeholder': 'Enter second name'}),

        }

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        # user.is_active = False # Send email verification
        if commit:
            user.save()
        return user