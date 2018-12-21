from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = "Email Address"
