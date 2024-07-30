from builtins import str, int, super

from django import forms
from django.contrib.auth.hashers import make_password
from .models import Employee, Medicine
import re

class EmployeeRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Employee
        fields = ['empid', 'empfname', 'emplname', 'emppasswd', 'emprole']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        cleaned_data['emppasswd'] = make_password(password)  # 修正箇所
        return cleaned_data


class CapitalSearchForm(forms.Form):
    capital = forms.CharField(label='資本金', max_length=20)

    def clean_capital(self):
        data = self.cleaned_data['capital']
        # 半角カンマ、全角カンマ、半角円記号、全角円記号を除去
        normalized_data = re.sub(r'[,\u3001\\￥¥]', '', data)
        # 全角数字を半角に変換
        normalized_data = normalized_data.translate(str.maketrans('０１２３４５６７８９', '0123456789'))

        # 数字とカンマ以外の文字が含まれているか確認
        if not re.match(r'^[\d,]*$', data):
            raise forms.ValidationError('資本金には数字とカンマのみを含めてください。')

        return int(normalized_data)

class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(label='新しいパスワード', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='パスワード確認', widget=forms.PasswordInput)

class MedicineForm(forms.Form):
    medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), label='薬剤名')
    quantity = forms.IntegerField(label='数量', min_value=1)

class PatientSearchForm(forms.Form):
    patfname = forms.CharField(label='患者名', required=False)
    patlname = forms.CharField(label='患者姓', required=False)

class PatientidSearchForm(forms.Form):
    patient_id = forms.CharField(label='患者ID', max_length=8)

