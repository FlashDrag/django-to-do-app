from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        '''Test that the done field defaults to False'''
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        '''Test that the string method returns the name'''
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
