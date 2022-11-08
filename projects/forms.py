from socket import fromshare
from django.forms import ModelForm
from .models import Project

from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "demo_link",
            "source_link",
            "featured_image",
            "tags",
        ]

        widgets = {"tags": forms.CheckboxSelectMultiple()}

        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({"class": "input"})
