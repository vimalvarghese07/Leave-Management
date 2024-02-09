from django import forms
from .models import UserProfile,TeacherModel,StudentModel,LeaveModel

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'username', 'email', 'password', 'age', 'user_type']
        widgets = {
            'password': forms.PasswordInput(),
            'user_type': forms.Select(choices=UserProfile.USER_TYPE_CHOICES),}
        
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))
    user = None
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        

        if username and password:
            user = UserProfile.objects.get(username=username, password=password)

            if user:
                self.user = user
            else:
                raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data
    
class TeacherDetails(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ['subject','department']
        exclude = ['id']  
        
        
class StudentDetails(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['course','semester']
        exclude = ['id']  
        
        


class ReasonForm(forms.ModelForm):
    class Meta:
        model = LeaveModel
        fields = ['teacher','message']
        exclude = ['student','verifystatus']