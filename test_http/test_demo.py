
import pytest
import requests


class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r)
        assert r.status_code == 200
