from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext, ugettext_lazy as _

from eManager.models import MyUser, Comment, Organization, Event

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = MyUser
		fields = ('username', 'email')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = MyUser
		fields = ('username', 'email')

class EventCreateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(EventCreateForm, self).__init__(*args,**kwargs)
		self.fields['organization'] = forms.ModelChoiceField(queryset=Organization.objects.filter(creator=user))

	class Meta:
		model = Event
		fields = ['name', 'start_date', 'description', 'address', 'image']
