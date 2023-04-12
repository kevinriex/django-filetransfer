from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *


class Form(forms.Form):
    file = forms.FileField(max_length=900, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div("file", css_class="input"),
            Submit('submit', 'Submit', css_class='btn'),)
