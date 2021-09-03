from django import forms
import django.core.validators as validators


class FileFieldForm(forms.Form):
    file_field = forms.FileField(label='选择多个文件', help_text='提示：注意*****',
                                 widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': "bg-info"}),
                                 validators=[validators.FileExtensionValidator(['xlsx'], message='必须是xlsx文件')])
