from attr import NOTHING
from functools import update_wrapper

NOTHING.__bool__ = staticmethod(lambda: False)
unset_value = NOTHING

class WebobInputWrapper(object):
    """
    Wrap a webob MultiDict for use as passing as `formdata` to Field.

    Since for consistency, we have decided in WTForms to support as input a
    small subset of the API provided in common between cgi.FieldStorage,
    Django's QueryDict, and Werkzeug's MultiDict, we need to wrap Webob, the
    only supported framework whose multidict does not fit this API, but is
    nevertheless used by a lot of frameworks.

    While we could write a full wrapper to support all the methods, this will
    undoubtedly result in bugs due to some subtle differences between the
    various wrappers. So we will keep it simple.
    """

    def __init__(self, multidict):
        update_wrapper(self, multidict)
        self.__wrapped__ = multidict

    def __iter__(self):
        return iter(self.__wrapped__)

    def __len__(self):
        return len(self.__wrapped__)

    def __contains__(self, name):
        return (name in self.__wrapped__)

    def getlist(self, name):
        return self.__wrapped__.getall(name)

class DictWrapper(WebobInputWrapper):
    """
    Wrap a Dict for use as passing as `formdata` to Field.
    """

    def getlist(self, name):
        ret = self.__wrapped__.get(name)
        assert(isinstance(ret, (list, tuple)))
        return ret
