from django.forms import ModelForm
from second_app.models import User

class RegisterInterest(ModelForm):
    class Meta():
        model = User
        fields = "__all__"