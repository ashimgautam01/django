from django import forms

class postForm(forms.Form):
    description=forms.CharField()
    image=forms.CharField()
    # user:
    like=forms.IntegerField(default=0)
    created_at=forms.DateTimeField(auto_now=True)
