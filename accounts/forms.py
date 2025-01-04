from django import forms
from accounts.models import CustomUser
from .models import UploadedFile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password','public_visibility', 'birth_year', 'address']
        public_visibility = forms.BooleanField(required=False, initial=True)
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class UploadBookForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'description', 'visibility', 'cost', 'year_of_publication', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith(('.pdf', '.jpeg', '.jpg')):
                raise forms.ValidationError("File must be a PDF or JPEG.")
        return file