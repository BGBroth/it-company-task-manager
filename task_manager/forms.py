from django import forms


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
