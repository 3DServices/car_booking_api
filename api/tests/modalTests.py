from django.test import TestCase
from api.models import User
import uuid
# Create your tests here.


class TestUserModal(TestCase):

    def test_existence_of_user_created(self):
        user = User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

        check_existence = User.objects.filter(first_name='timo').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_user_record(self):
        user = User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')
        user_store = User.objects.get(first_name='timo')
        user_store.first_name = 'masiko'

        user_store.save()

        check_existence = User.objects.filter(first_name='masiko').exists()
        self.assertEqual(check_existence, True)

    def test_delete_of_user_record(self):
        user = User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')
        user_store = User.objects.get(first_name='timo')
        user_store.delete()
        check_existence = User.objects.filter(first_name='timo').exists()
        self.assertEqual(check_existence, False)


# guidance with the crud operation
