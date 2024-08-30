from django import forms
from .models import Novel, Contact

class NovelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Book title eg. John Kamau'}), label='Book Title', min_length=2, max_length=50, label_suffix=':', empty_value=None, )
    author = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Book description'}))
    genre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'genre eg. arts'}))
    published_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'eg. 1998/06/28'}))
    edition = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'eg. 3'}))
    bnanner = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Novel
        fields = ['title', 'author','description', 'genre','published_date','edition','bnanner']
        
from django import forms


#with forms.Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    subject = forms.CharField(label='Your Subject', widget=forms.TextInput(attrs={'placeholder': 'Enter your Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))
    subscribe = forms.BooleanField(required=False, label='Subscribe to newsletter')
    
    class Meta:
        model = Contact
        fields = ['name', 'email','subject', 'message', 'subscribe']

#with forms.ModelForm
class ContactForm1(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    subject = forms.CharField(label='Your Subject', widget=forms.TextInput(attrs={'placeholder': 'Enter your Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))
    subscribe = forms.BooleanField(required=False, label='Subscribe to newsletter')
    
    class Meta:
        model = Contact
        fields = ['name', 'email','subject', 'message', 'subscribe']
    
    # Customize the Save Method (Optional)
    def save(self, commit=True):
        contact = super().save(commit=False)
        # Modify the data here (e.g., capitalize the name)
        contact.name = contact.name.capitalize()
        if commit:
            contact.save()
        return contact
