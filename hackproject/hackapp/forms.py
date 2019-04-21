from django import forms
from .models import TextEntry

class HomeForm(forms.ModelForm):
    class Meta:
        model = TextEntry
        fields = ('text',)

    post = forms.CharField(max_length=2000,label='',
        widget=forms.Textarea(attrs={'rows': "10", 'cols': 150,
                'style': 'padding-right: 50px; ;',
            }),)



