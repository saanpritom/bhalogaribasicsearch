from django import forms


class CarCreationFrom(forms.Form):
    total_numbers = forms.CharField(label='Total Car Numbers', widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'InputCarNumbers', 'placeholder': 'Ex: 10'}), required=True, max_length=60, help_text='Required. Provide Total Numbers of Cars You Want to Create')

    class Meta:
        fields = ('total_numbers',)
