from django import forms
from .models import TaskItem


class TaskItemCreateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields =('title', 'body','due_date','category')

        widgets = {
	        'due_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
	    }
        
        
class TaskItemUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields =("title", 'body','due_date','task_finished','category')

        widgets = {
	        'due_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
	    }