from formsapp.models import Review
from django import forms

# class ReviewsForm(forms.Form):
#     name = forms.CharField(label="Name", max_length=100, error_messages={
#         "required": "Needed."
#     })
#     review = forms.CharField(label='Review', widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=0, max_value=5)

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'name': 'Name',
            'review': 'Review',
            'rating': 'Rating',
        }
        error_messages = {
            'name': {'required':'Name invalid.'},
            'review': {'required':'Review invalid.'},
            'rating': {'required':'Rating invalid.'},
        }