from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import MyModel

class PostForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('description',)