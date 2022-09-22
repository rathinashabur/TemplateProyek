from django.test import TestCase

# Create your tests here.
class jsonTests(TestCase):
    def tests_testjsonpage(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)