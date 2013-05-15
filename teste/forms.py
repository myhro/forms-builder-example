from django import forms
from forms_builder.forms.models import Form, Field

class CadastroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.fields['send_email'].initial = False
        self.fields['send_email'].widget = forms.HiddenInput()
    class Meta:
        model = Form
        exclude = (
            'button_text',
            'email_copies',
            'email_from',
            'email_message',
            'email_subject',
            'expiry_date',
            'intro',
            'login_required',
            'publish_date',
            'response',
            'sites',
            'status',
        )

class CampoForm(forms.ModelForm):
    class Meta:
        model = Field
        exclude = (
            'form',
            'help_text',
            'order',
            'placeholder_text',
            'slug',
            'visible',
        )
