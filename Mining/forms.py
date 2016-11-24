
# make sure this is at the top if it isn't already
from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_phone = forms.RegexField(required=True, regex=r'^\+?1?\d{9,16}$', error_message=( "Phone number must be entered in the format: '+999999999'."))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name"
        self.fields['contact_email'].label = "Email"
        self.fields['contact_phone'].label = "Phone"
        self.fields['content'].label = "Request Details"

