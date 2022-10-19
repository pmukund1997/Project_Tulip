from django import forms
from.models import User


# overridden the user creatuin form in admin panel to show additional fields
class UserCreationForm(forms.ModelForm):
    ''' Custom user creation form which shows additional fields '''

    user_role = forms.IntegerField()
    class Meta:
        model = User
        fields = '__all__'

    def clean_user_role(self):
        user_role = self.cleaned_data.get("user_role")
        if user_role == None or user_role == 0:
            raise forms.ValidationError("Role is Invalid !")
        return user_role

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_role = self.clean_user_role()
        if commit:
            user.save()
        return user