from django import forms

from main.models import ContactProfile

class ContactForm(forms.ModelForm):
    

    message = forms.CharField(max_length=250, required=True,
                              widget=forms.Textarea(attrs={
                                  'rows':6,
                              }))
    class Meta:
        model = ContactProfile
        fields = ("email", 'message', 'name')
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['message'].widget.attrs['placeholder'] = 'Write something..'
  
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
