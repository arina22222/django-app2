from django.forms import ModelForm 
from .models import Room, User
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room  # a model we wanna create a form  for
        fields = '__all__' # the fields which we need 
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']