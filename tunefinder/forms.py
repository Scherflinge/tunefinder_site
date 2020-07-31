from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()

# widget = forms.TextInput(attrs={'class': 'text', 'accept': 'audio/wav', 'id': "userfile"}))
