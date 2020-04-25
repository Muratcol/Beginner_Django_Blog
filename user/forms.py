from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    
class RegisterForm(forms.Form):

    username = forms.CharField(max_length=20, label="Username")
    password = forms.CharField(max_length=20, label="Password", widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Password Confirmation", widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and confirm != password:
            raise forms.ValidationError("Password are not same")

        values = {
            "username" : username,
            "password" : password
        }
        return values