from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        '''Test that the name field is required'''
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_if_not_required(self):
        '''Test that the done field is not required'''
        form = ItemForm({'name': 'Test todo item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        '''
        Test that the fields are explicitly defined in the form's Meta class,
        which means that the form will only include the fields specified in
        the Meta class. This is a security measure to prevent unwanted data
        from being submitted through the form.
        '''
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
