"""
Fields to support various HTML5 input types.
"""
from . import core

__all__ = (
    'DateField', 'DateTimeField', 'DateTimeLocalField', 'DecimalField',
    'DecimalRangeField', 'EmailField', 'IntegerField', 'IntegerRangeField',
    'SearchField', 'TelField', 'TimeField', 'URLField',
)


class SearchField(core.StringField):
    """
    Represents an ``<input type="search">``.
    """
    input_type = 'search'


class TelField(core.StringField):
    """
    Represents an ``<input type="tel">``.
    """
    input_type = 'tel'


class URLField(core.StringField):
    """
    Represents an ``<input type="url">``.
    """
    input_type = 'url'


class EmailField(core.StringField):
    """
    Represents an ``<input type="email">``.
    """
    input_type = 'email'


class DateTimeField(core.DateTimeField):
    """
    Represents an ``<input type="datetime">``.
    """
    input_type = 'datetime'


class DateField(core.DateField):
    """
    Represents an ``<input type="date">``.
    """
    input_type = 'date'


class TimeField(core.TimeField):
    """
    Represents an ``<input type="time">``.
    """
    input_type = 'time'


class DateTimeLocalField(core.DateTimeField):
    """
    Represents an ``<input type="datetime-local">``.
    """
    input_type = 'datetime-local'


class IntegerField(core.IntegerField):
    """
    Represents an ``<input type="number">``.
    """
    input_type = 'number'
    field_attrs = {"step": "1"}


class DecimalField(core.DecimalField):
    """
    Represents an ``<input type="number">``.
    """
    input_type = 'number'
    field_attrs = {"step": "any"}


class IntegerRangeField(core.IntegerField):
    """
    Represents an ``<input type="range">``.
    """
    input_type = 'range'


class DecimalRangeField(core.DecimalField):
    """
    Represents an ``<input type="range">``.
    """
    input_type = 'range'
    field_attrs = {"step": "any"}
