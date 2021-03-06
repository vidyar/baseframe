# -*- coding: utf-8 -*-

import wtforms
from flask import Markup

__all__ = ['TinyMce3', 'TinyMce4', 'SubmitInput', 'DateTimeInput', 'HiddenMultiInput']


class TinyMce3(wtforms.widgets.TextArea):
    """
    Rich text widget with Tiny MCE 3.
    """
    input_type = "tinymce3"

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        if c:
            kwargs['class'] = u'%s %s' % ('richtext', c)
        else:
            kwargs['class'] = 'richtext'
        return super(TinyMce3, self).__call__(field, **kwargs)


class TinyMce4(wtforms.widgets.TextArea):
    """
    Rich text widget with Tiny MCE 4.
    """
    input_type = "tinymce4"

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        if c:
            kwargs['class'] = u'%s %s' % ('richtext', c)
        else:
            kwargs['class'] = 'richtext'
        return super(TinyMce4, self).__call__(field, **kwargs)


class SubmitInput(wtforms.widgets.SubmitInput):
    """
    Submit input with pre-defined classes.
    """
    def __init__(self, *args, **kwargs):
        self.css_class = kwargs.pop('class', '') or kwargs.pop('class_', '')
        super(SubmitInput, self).__init__(*args, **kwargs)

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = u'%s %s' % (self.css_class, c)
        return super(SubmitInput, self).__call__(field, **kwargs)


class DateTimeInput(wtforms.widgets.Input):
    """
    Render date and time inputs.
    """
    input_type = 'datetime'

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        field_id = kwargs.pop('id')
        kwargs.pop('type', None)
        value = kwargs.pop('value', None)
        if value is None:
            value = field._value()
        if not value:
            value = ' '
        date_value, time_value = value.split(' ', 1)
        return Markup(u'<input type="text" class="datetime-date" data-datepicker="datepicker" %s /> <input type="text" class="datetime-time" %s />' % (
            wtforms.widgets.html_params(name=field.name, id=field_id + '-date', value=date_value, **kwargs),
            wtforms.widgets.html_params(name=field.name, id=field_id + '-time', value=time_value, **kwargs)
            ))


class HiddenMultiInput(wtforms.widgets.core.Input):
    """
    Render a hidden input.
    """
    input_type = 'hidden'
