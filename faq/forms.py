"""faq form"""
from django import forms
from .models import FaqPosts


class FaqPostsForm(forms.ModelForm):
    """form for adding questions to the faq"""
    class Meta:
        """defines model and fields which will be used"""
        model = FaqPosts

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
