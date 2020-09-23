import requests
corpid = "ww9fff7329472a75df"
corpsecret = "918WWbNMJ1K13wnfCd6vZMLOWfaWZfrpDxdqy4wLyxw"


def get_contact():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    result = requests.get(url).json()
    return result['access_token']


def test_add():
    data = {
        "userid":"weilaiwenle",
        "name":"乐乐",
        "email":'1484937423@qq.com',
        "department":[1, 2]
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_contact()}"
    print(requests.post(url,json=data).json())

def test_get():
    USERID = 'weilaiwenle'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_contact()}&userid={USERID}'
    print(requests.get(url).json())

def test_update():
    data = {
        "userid": "weilaiwenle",
        "name": "未来文乐",
        "department": [1]
    }
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_contact()}'
    print(requests.post(url, json=data).json())

def test_delete():
    USERID = 'weilaiwenle'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_contact()}&userid={USERID}'
    print(requests.get(url).json())




