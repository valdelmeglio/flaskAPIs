#!flask/bin/python
import unittest,requests

class TestCase(unittest.TestCase):
    def test_sum(self):
        url = 'http://127.0.0.1:5000/api/sum/4&9'
        string_json_request=requests.get(url)
        string_json=string_json_request.json()
        assert string_json['sum']==13
        assert string_json['first']==9
        assert string_json['second']==4
        
    def test_string(self):
        url = 'http://127.0.0.1:5000/api/string/these are paolo''s friends'    
        string_json_request=requests.get(url)
        string_json=string_json_request.json()
        assert string_json['api_string']=='These Are Paolo''s Friends'
        
if __name__ == '__main__':
    unittest.main()        