from django import forms


class UserForm(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=20)
    senha = forms.CharField(label='Senha', max_length=20,
                            widget=forms.PasswordInput)
