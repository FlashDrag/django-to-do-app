from django.test import TestCase
from .models import Item
from .forms import AddItemForm, EditItemForm


class AddItemFormTest(TestCase):

    def test_item_name_is_required(self):
        '''Test that the name field is required'''
        form = AddItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_if_not_required(self):
        '''Test that the done field is not required'''
        form = AddItemForm({'name': 'Test todo item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        '''
        Test that the fields are explicitly defined in the form's Meta class,
        which means that the form will only include the fields specified in
        the Meta class. This is a security measure to prevent unwanted data
        from being submitted through the form.
        '''
        form = AddItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])


class EditItemFormTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name='Test todo item', done=False)

    def test_edit_item_form_valid(self):
        form = EditItemForm(instance=self.item, data={
                            'name': 'Updated test item', 'done': True})
        self.assertTrue(form.is_valid())

    def test_edit_item_form_invalid(self):
        form = EditItemForm(instance=self.item, data={
                            'name': '', 'done': True})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_edit_item_form_initial_data(self):
        form = EditItemForm(instance=self.item)
        self.assertEqual(form.fields['name'].widget.attrs['value'],
                         self.item.name)

    def test_done_field_if_not_required(self):
        form = EditItemForm({'name': 'Test todo item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = EditItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
