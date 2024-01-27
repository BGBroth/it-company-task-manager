from django import forms
from django.contrib.auth.forms import UserCreationForm
from task_manager.models import Worker, Task


def create_search_field(placeholder):
    return forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": placeholder
            }
        )
    )


class TaskSearchForm(forms.Form):
    name = create_search_field("Search by name")


class WorkerSearchForm(forms.Form):
    username = create_search_field("Search by username")


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
