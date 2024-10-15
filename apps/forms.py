from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, Form, EmailField

from apps.models import User



class ProfileForm(Form):
    fullname = CharField(max_length=255)
    address = CharField(max_length=255)
    phone = CharField(max_length=255)
    mobile = CharField(max_length=255)
    email = EmailField()



class LoginForm(Form):
    username = CharField(max_length=50)
    password = CharField(max_length=50)


    def clean(self):
        data = super().clean()
        username = data.get('username')
        password = data.get('password')
        self.find_user = User.objects.filter(username=username).first()
        if not self.find_user:
            raise ValidationError("Not Found account")
        if not check_password(password,self.find_user.password):
            raise ValidationError("Your wrong password")
        return data



class RegisterForm(ModelForm):
    confirm_password = CharField(max_length=30)

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'confirm_password'

    def clean_email(self):
        email = self.clean().get("email")
        if not email.endswith('@gmail.com'):
            raise ValidationError("Your Password is short")
        return email
    def clean_password(self):
        password = self.clean().get("password")
        if len(password) < 4:
            raise ValidationError("Your Password is short")
        clean_data = super().clean()
        confirm_password = self.data.get("confirm_password")
        if confirm_password != password:
            raise ValidationError("Password and Confirm password not match")
        return make_password(clean_data.get("password"))

