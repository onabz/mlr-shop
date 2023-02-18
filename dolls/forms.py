from django import forms
from .models import Doll, DollType


class DolltypeForm(forms.ModelForm):

    class Meta:
        model = Doll
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dolltypes = DollType.objects.all()

        names = [(d.id, d.__str__()) for d in dolltypes]

        self.fields['dolltype'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
