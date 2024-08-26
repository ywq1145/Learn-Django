from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} # remove the label from the form

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''} # remove the label from the form
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # set the width of the textarea