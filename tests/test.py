import unittest

import main


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        client = main.app.test_client()
        rv = client.post('/', data=dict(
            calc='計算',
            height=160,
            weight=50))
        self.html = rv.data.decode('utf-8').lower()

    def test_result(self):
        self.assertTrue('19.53' in self.html, msg='結果が正しく表示されていません')
