from django.forms import MultipleChoiceField


class MultipleChoiceAnyField(MultipleChoiceField):
    """A MultipleChoiceField with no validation."""

    def valid_value(self, *args, **kwargs):
        return True