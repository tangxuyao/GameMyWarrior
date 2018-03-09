import requests
import unittest


class ActorTestCase(unittest.TestCase):
    @staticmethod
    def test_create():
        for i in range(2000):
            r1 = requests.post("http://localhost:8811/v1/signup")
            ret = r1.json()
            token = ret["token"]

            payload = {'token': token, 'name': 'imGod %d' % i}
            r2 = requests.post("http://localhost:8811/v1/startgame", data=payload)
            assert r2.ok

if __name__ == '__main__':
    unittest.main()
