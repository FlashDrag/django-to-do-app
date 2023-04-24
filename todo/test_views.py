from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        # make a HTTP GET request to the homepage
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # check that the expected template was used
        self.assertTemplateUsed(response, 'todo/index.html')

    def test_can_add_item(self):
        # make a HTTP POST request to the homepage
        response = self.client.post('/', {'name': 'Test Todo Item'})
        self.assertRedirects(response, '/')

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.post(f'/toggle/{item.id}')
        self.assertEqual(response.url, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_get_item_name_to_edit(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/index.html')
        # check that the item name is in the context
        self.assertContains(response, 'Test Todo Item')

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}',
                                    {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')

    def test_is_max_items_reached(self):
        '''
        Test that the maximum number of creating items is 5
        and that a warning message is displayed
        '''
        # create 5 items
        for i in range(5):
            Item.objects.create(name=f'Item {i}')

        # make a HTTP POST request to the homepage to create a new item
        response = self.client.post('/', {'name': 'Test Todo Item'})
        self.assertEqual(response.url, '/')

        # check that the expected template was used
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'You have reached the maximum limit of 5 items! '
                         'Please delete some tasks before adding new ones.')
