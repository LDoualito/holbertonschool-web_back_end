#!/usr/bin/env python3
""" Module for tests """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test the function access_nested_map from utils module """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test the function with correct inputs """
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test the function with wrong inputs """
        with self.assertRaises(Exception) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(e.exception, expected)


class TestGetJson(unittest.TestCase):
    """ Test function get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test the method with correct output """
        with patch('requests.get') as MockClass:
            MockClass.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            MockClass.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Test function memoize """

    def test_memoize(self):
        """ Test the method """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as m:
            obj = TestClass()
            self.assertEqual(obj.a_property, m.return_value)
            self.assertEqual(obj.a_property, m.return_value)
            m.assert_called_once()
