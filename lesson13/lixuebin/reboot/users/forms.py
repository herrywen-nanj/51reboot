from django import forms
from django.contrib.auth.models import Group, Permission
from .models import UserProfile
import re


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = "__all__"
        fields = ['username', 'name_cn', 'phone']

    def clean_phone(self):
        """
        通过正则表达式验证手机号码是否合法
        """
        phone = self.cleaned_data['phone']
        phone_regex = r'^1[34578][0-9]{9}$'
        p = re.compile(phone_regex)
        if p.match(phone):
            return phone
        else:
            # forms.ValidationError自定义表单错误
            raise forms.ValidationError('手机号码非法', code='invalid')



class UserUpdateForm(forms.Form):
    username = forms.CharField(required=True, max_length=10)
    name_cn = forms.CharField(required=True, max_length=30)
    phone = forms.CharField(required=True, max_length=11)

    def clean_phone(self):
        """
        通过正则表达式验证手机号码是否合法
        """
        phone = self.cleaned_data['phone']
        phone_regex = r'^1[34578][0-9]{9}$'
        p = re.compile(phone_regex)
        if p.match(phone):
            return phone
        else:
            # forms.ValidationError自定义表单错误
            raise forms.ValidationError('手机号码非法', code='invalid')


class RoleProfileForm(forms.Form):
    class Meta:
        model = Group
        fields = ['name']

    def clean_name(self):
        name = self.clean_data['name']
        name_regex = r'\S{1,16}$'
        p = re.compile(name_regex)
        if p.match(name):
            return name
        else:
            raise forms.ValidationError('角色名有误',code='invaild')