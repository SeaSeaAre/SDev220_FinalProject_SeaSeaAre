from django import forms
from AppV2.models import Client

class ClientForm(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Client
        fields = "__all__"