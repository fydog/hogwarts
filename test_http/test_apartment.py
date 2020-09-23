import requests

corpid = 'ww9fff7329472a75df'
corpsecret = '918WWbNMJ1K13wnfCd6vZMLOWfaWZfrpDxdqy4wLyxw'

def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    resulet = requests.get(url).json()
    return resulet['access_token']

def test_add_appartment():

    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}'
    data = {
        'name':'流浪哥谭',
        'parentid': 1
    }
    print(requests.post(url, json=data).json())

def test_get():
    ID = 3
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={get_token()}&id={ID}'
    print(requests.get(url).json())

def test_updata():
    data = {
        "id":3,
        'name':'流浪哥谭213'
    }
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token()}'
    print(requests.post(url, json=data).json())


def test_delete():
    ID = 3
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token()}&id={ID}'
    print(requests.get(url).json())
