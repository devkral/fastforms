from fastforms.utils import WebobInputWrapper
from fastforms import i18n


class DefaultMeta(object):
    """
    This is the default Meta class which defines all the default values and
    therefore also the 'API' of the class Meta interface.
    """

    # -- Basic form primitives

    def bind_field(self, form, unbound_field, options):
        """
        bind_field allows potential customization of how fields are bound.

        The default implementation simply passes the options to
        :meth:`UnboundField.bind`.

        :param form: The form.
        :param unbound_field: The unbound field.
        :param options:
            A dictionary of options which are typically passed to the field.

        :return: A bound field
        """
        return unbound_field.bind(form=form, **options)

    def wrap_formdata(self, form, formdata):
        """
        wrap_formdata allows doing custom wrappers of WTForms formdata.

        The default implementation detects webob-style multidicts and wraps
        them, otherwise passes formdata back un-changed.

        :param form: The form.
        :param formdata: Form data.
        :return: A form-input wrapper compatible with WTForms.
        """
        if formdata is not None and not hasattr(formdata, 'getlist'):
            if hasattr(formdata, 'getall'):
                return WebobInputWrapper(formdata)
            elif hasattr(formdata, 'get'):
                return DictWrapper(formdata)
            else:
                raise TypeError("formdata should be a multidict-type wrapper that supports the 'getlist' method or a dict which returns a list/tuple")
        return formdata

    # -- i18n

    locales = False
    cache_translations = True
    translations_cache = {}

    def get_translations(self, form):
        """
        Override in subclasses to provide alternate translations factory.
        See the i18n documentation for more.

        :param form: The form.
        :return: An object that provides gettext() and ngettext() methods.
        """
        locales = self.locales
        if locales is False:
            return None

        if self.cache_translations:
            # Make locales be a hashable value
            locales = tuple(locales) if locales else None

            translations = self.translations_cache.get(locales)
            if translations is None:
                translations = self.translations_cache[locales] = i18n.get_translations(locales)

            return translations

        return i18n.get_translations(locales)

    # -- General

    def update_values(self, values):
        """
        Given a dictionary of values, update values on this `Meta` instance.
        """
        for key, value in values.items():
            setattr(self, key, value)
