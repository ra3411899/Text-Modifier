from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)