from unittest import TestCase
from fastforms.form import BaseForm
from fastforms.utils import WebobInputWrapper
from fastforms.utils import unset_value
from fastforms.fields import Field

class MockMultiDict(object):
    def __init__(self, tuples):
        self.tuples = tuples

    def __len__(self):
        return len(self.tuples)

    def __iter__(self):
        for k, _ in self.tuples:
            yield k

    def __contains__(self, key):
        for k, _ in self.tuples:
            if k == key:
                return True
        return False

    def getall(self, key):
        result = []
        for k, v in self.tuples:
            if key == k:
                result.append(v)
        return result


class SneakyField(Field):
    def __init__(self, sneaky_callable, **kwargs):
        super(SneakyField, self).__init__(**kwargs)
        self.sneaky_callable = sneaky_callable

    def process(self, formdata, data=unset_value):
        self.sneaky_callable(formdata)


class WebobWrapperTest(TestCase):
    def setUp(self):
        w_cls = MockMultiDict

        self.test_values = [('a', 'Apple'), ('b', 'Banana'), ('a', 'Cherry')]
        self.empty_mdict = w_cls([])
        self.filled_mdict = w_cls(self.test_values)

    def test_automatic_wrapping(self):
        def _check(formdata):
            self.assertIsInstance(formdata, WebobInputWrapper)

        form = BaseForm({'a': SneakyField(sneaky_callable=_check)})
        form.process(self.filled_mdict)

    def test_empty(self):
        formdata = WebobInputWrapper(self.empty_mdict)
        self.assertFalse(formdata)
        self.assertEqual(len(formdata), 0)
        self.assertEqual(list(formdata), [])
        self.assertEqual(formdata.getlist('fake'), [])

    def test_filled(self):
        formdata = WebobInputWrapper(self.filled_mdict)
        self.assertTrue(formdata)
        self.assertEqual(len(formdata), 3)
        self.assertEqual(list(formdata), ['a', 'b', 'a'])
        self.assertTrue('b' in formdata)
        self.assertTrue('fake' not in formdata)
        self.assertEqual(formdata.getlist('a'), ['Apple', 'Cherry'])
        self.assertEqual(formdata.getlist('b'), ['Banana'])
        self.assertEqual(formdata.getlist('fake'), [])
