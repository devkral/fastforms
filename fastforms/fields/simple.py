from .core import Field, StringField, BooleanField

__all__ = (
    'BooleanField', 'TextAreaField', 'PasswordField', 'FileField', 'MultipleFileField',
    'HiddenField', 'SubmitField'
)


class TextAreaField(StringField):
    """
    This field represents an HTML ``<textarea>`` and can be used to take
    multi-line input.
    """
    def __str__(self):
        """ Just an example, use templates in real code and check for TextAreaField """
        attrs = self.field_attrs.copy()
        value = attrs.pop("value")
        return "<textarea {attrs}>{value}</textarea>".format(value=value, attrs=attrs)


class PasswordField(StringField):
    """
    A StringField, except renders an ``<input type="password">``.

    Also, whatever value is accepted by this field is not rendered back
    to the browser like normal fields.
    """
    input_type = 'password'


class FileField(Field):
    """Renders a file upload field.

    By default, the value will be the filename sent in the form data.
    WTForms **does not** deal with frameworks' file handling capabilities.
    A WTForms extension for a framework may replace the filename value
    with an object representing the uploaded data.
    """

    input_type = 'file'

    def _value(self):
        # browser ignores value of file input for security
        return False


class MultipleFileField(FileField):
    """A :class:`FileField` that allows choosing multiple files."""

    input_type = 'file'
    field_attrs = {"multiple": "multiple"}

    def process_formdata(self, valuelist):
        self.data = valuelist


class HiddenField(StringField):
    """
    HiddenField is a convenience for a StringField with a HiddenInput widget.

    It will render as an ``<input type="hidden">`` but otherwise coerce to a string.
    """
    input_type = 'hidden'
    # for having hidden flag
    field_attrs = {"hidden": "hidden"}


class SubmitField(BooleanField):
    """
    Represents an ``<input type="submit">``.  This allows checking if a given
    submit button has been pressed.
    """
    input_type = 'submit'
