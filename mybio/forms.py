from .models import Comment, Contact
from django import forms

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'address', 'company', 'message')
		labels = {
			"name": "",
			"email": "",
			"address": "",
			"company": "",
			"message": ""
		}

		widgets = {
			'name' : forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Your Name', "name": "name", "type": "text"}),
			'email' : forms.EmailInput(attrs={'class': 'contact-input', "name": "email", "type": "email", "placeholder": "Your Email"}),
			'address' : forms.TextInput(attrs={'class': 'contact-input', "name": "text", "type": "text", "placeholder": "Your Address"}),
			'company' : forms.TextInput(attrs={'class': 'contact-input', "name": "text", "type": "text", "placeholder": "Your Company"}),
			'message' : forms.Textarea(attrs={'class': 'contact-input', "rows": "5", "placeholder": "Your Messages"}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'subject', 'email', 'body')
		labels = {
			"name": "",
			"email": "",
			"subject": "",
			"body": ""
		}

		widgets = {
			'name' : forms.TextInput(attrs={"name": "name", "type": "text", 'placeholder': 'Name'}),
			'subject' : forms.TextInput(attrs={"name": "url", "type": "text", "placeholder": "Subject"}),
			'email' : forms.EmailInput(attrs={"name": "email", "type": "email", "placeholder": "Email"}),
			'body' : forms.Textarea(attrs={"id": "comment-reply", "name": "comment", "rows": "5", "placeholder": "Type Here Your Comment"}),
		}