#Client allows to make test requests
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
#reverse creates urls for specified page
from django.urls import reverse


class AdminSiteTests(TestCase):
    #func ran before every test
    def setUp(self):
        #create new Client
        self.client = Client()
        #new superuser
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@GMAIL.com',
            password = 'test123'
        )
        #use 'force_login' so doesn't need to manually log in user
        self.client.force_login(self.admin_user)
        #create regular user for testing
        self.user = get_user_model().objects.create_user(
            email = 'test@GMAIL.com',
            password = 'test123',
            name = 'John Doe'
        )

    def test_users_listed(self):
        """Test that users are listed on the admin user site page"""
        #reverse( [appadmin] : [url]) 'core_user_changelist' in admin (docu) will general url for list user page
        #use reverse so that you don't need to type in a static url
        url = reverse('admin:core_user_changelist')
        #res is response
        res = self.client.get(url)
        #check that res contains certain items within its object, and is 200 OK resp
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


    def test_user_change_page(self):
        """Test that the user edit page works"""
        #admin/core/user/id - see fieldsets in admin.py 
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
      
    def test_create_user_page(self):
        """Test that the create user page works"""
        #admin/core/user/id - see fieldsets in admin.py, core_user_add standard url alias, see add_fieldsets in admin.py 
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

