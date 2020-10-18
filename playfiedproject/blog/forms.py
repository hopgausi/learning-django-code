from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Comment, Message


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [    
            'name',
            'email',
            'content',       
        ]
        labels = {
            'name': False,
            'email': False,
            'content': False,            
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Your name',
                    'required':True,
                }    
            ),
            'content': Textarea(
                attrs={
                    'placeholder': 'Type your comment',
                    'required':True,
                }    
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Your Email',
                    'required':True,
                }    
            ),
            
        }
    
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'subject',
            'message', 
        ]
        labels = {
            'name': False,
            'email': False,
            'subject':False,
            'message': False,
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Your Name',
                    'required':True,
                }
            ),
            'email': EmailInput(
                    attrs={
                        'placeholder': 'Your Email',
                        'required':True,
                    }    
                ),
            'message': Textarea(
                    attrs={
                        'placeholder': 'Type your message',
                        'required':True,
                    }
                ),
            'subject': TextInput(
                attrs={
                    'placeholder': 'Subject',
                    'required':True,   
                }
            )
        }
