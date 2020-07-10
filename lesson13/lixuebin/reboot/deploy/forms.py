from django import forms
from .models import Deploy


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Deploy
        # fields= "__all__"
        fields = ['name', 'version', 'version_desc', 'update_detail']


class DeployForm(forms.ModelForm):
    class Meta:
        model = Deploy
        fields = ['name', 'version', 'version_desc', 'update_detail']