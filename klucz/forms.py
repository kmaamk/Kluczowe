from django import forms
from .models import Question
from django import template

register = template.Library()


class QuestionForm(forms.ModelForm):
    choice_text = forms.MultipleChoiceField(label="Wybierz kierunek kluczowy", choices=Question.base_courses,
                                            widget=forms.CheckboxSelectMultiple, required=True,)
    branch = forms.ChoiceField(label="Oddział", choices=Question.branches, help_text="wybierz kod oddziału")


    class Meta:

        model=Question
        fields=['branch','choice_text']


    @register.filter (name='selected_labels')
    def selected_labels(form, field):
        return [label for value, label in form.fields[field].choices if value in form[field].value()]