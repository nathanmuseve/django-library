from django import forms
from .models import Novel

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
        
