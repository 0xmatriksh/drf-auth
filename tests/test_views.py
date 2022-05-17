""" 
    import pdb
    This is for debuging purpose
"""

from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_message_get(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        res = self.client.get(self.messageurl)
        self.assertEqual(res.status_code, 200)

    def test_message_post(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        res = self.client.post(self.messageurl, self.message)
        self.assertEqual(res.status_code, 201)
        # 201 : request was successful and as a result, a resource has been created
