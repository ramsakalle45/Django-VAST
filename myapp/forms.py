# myapp\forms.py
from django import forms
from .models import Item, Post

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']   
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date']         
        
