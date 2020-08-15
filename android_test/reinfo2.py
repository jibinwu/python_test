import unittest
import json
import requests

from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    @data('浙F9992X','浙A2WY91','浙A551DS','浙AHN058','浙A007US','浙A5BV93','浙FEF106','浙F300VV','浙FH183W','浙A583MH')
    def test_getReInfo1(self,plate):
        url = 'http://114.55.43.36:7091/api/getReInfo'
        headers = {'authorization': 'Bearer def34b98-7276-48b1-b857-fc5dae045214', 'Content-Type': 'application/json'}
        content = {'plateNo': plate, 'cityCode': 9}
        r = requests.post(url, headers=headers, data=json.dumps(content))
        # self.assertIn('"code":"0000"',r.text)
        self.assertEqual(r.status_code,200)

    # def test_getReInfo2(self):
    #     url = 'http://114.55.43.36:7091/api/getReInfo'
    #     headers = {'authorization': 'Bearer def34b98-7276-48b1-b857-fc5dae045214', 'Content-Type': 'application/json'}
    #     content = {'plateNo': '浙F399JD', 'cityCode': 9}
    #     r = requests.post(url, headers=headers, data=json.dumps(content))
    #     # self.assertIn('"code":"0000"',r.text)
    #     self.assertEqual(r.status_code,200)


    # def test_getReInfo3(self):
    #     url = 'http://114.55.43.36:7091/api/getReInfo'
    #     headers = {'authorization': 'Bearer def34b98-7276-48b1-b857-fc5dae045214', 'Content-Type': 'application/json'}
    #     content = {'plateNo': '浙AA80G8', 'cityCode': 9}
    #     r = requests.post(url, headers=headers, json=content)
    #     # self.assertIn('"code":"0000"',r.text)
    #     self.assertEqual(r.status_code,200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
