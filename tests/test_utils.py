import unittest
from unittest.mock import patch

from gwf.utils import _split_import_path, cache, import_object


class TestCache(unittest.TestCase):

    def test_returns_same_object_when_called_twice_with_same_args(self):
        func = cache(lambda x: object())
        obj1 = func(42)
        obj2 = func(42)
        self.assertEqual(id(obj1), id(obj2))

    def test_does_not_return_same_object_when_called_with_diff_args(self):
        func = cache(lambda x: object())
        obj1 = func(42)
        obj2 = func(43)
        self.assertNotEqual(id(obj1), id(obj2))


class TestImportObject(unittest.TestCase):

    def test_split_import_path_without_object_specified(self):
        filename, basedir, obj = _split_import_path(
            '/some/dir/workflow.py', 'workflow_obj'
        )

        self.assertEqual(filename, 'workflow')
        self.assertEqual(basedir, '/some/dir')
        self.assertEqual(obj, 'workflow_obj')

    def test_split_import_path_with_object_specified(self):
        filename, basedir, obj = _split_import_path(
            '/some/dir/workflow.py:other_obj', 'workflow_obj'
        )

        self.assertEqual(filename, 'workflow')
        self.assertEqual(basedir, '/some/dir')
        self.assertEqual(obj, 'other_obj')

    def test_split_invalid_import_path_raises_value_error(self):
        with self.assertRaises(ValueError):
            filename, basedir, obj = _split_import_path(
                '/some/dir/workflow.py::other_obj', 'workflow_obj'
            )

