'''
Examples of the use of HTTPS methods using https://httpbin.org/
'''
import requests

def get_example():
    URL = "https://httpbin.org/get"
    response = requests.get(URL)                     #it returns a Response type
    print(f'Response Type: {type(response)}')    
    print(f'Status Code: {response.status_code}')
    print(f'Response Body:\n{response.text}')        #It returns a JSON object in a str format
    
    payload = response.json()                        #It serialize the str and transform it into a JSON object (dict)
    print(f'Response Origin {payload.get("origin")}')
    print(f'Response URL {payload.get("url")}')
    
def params_example():
    '''
     Example of passing parameters to https://httpbin.org
     https://httpbin.org echoes all the variables sent
     
    '''
    #Using URL
    URL = "https://httpbin.org/get?name=luis&password=123"
    response = requests.get(URL)
    if response.status_code == 200:
        payload = response.json()
        params = payload['args']
        print(params["name"])
        print(params["password"])
        
    #Using requests library
    params = {
        'name': 'Luis',
        'password': '123',
    }
    URL = "https://httpbin.org"
    response = requests.get(URL,params = params)
    if response.status_code == 200:
        print(response.url)

def post_example():
    URL = "https://httpbin.org/post"
    data = {
        'user' : 'Luis',
        'password': '123'
    }
    response = requests.post(URL,data = data)
    if response.status_code == 200:
        payload = response.json()
        print(payload["form"])
        
def headers_example():
    URL = "https://httpbin.org/post"
    headers = {
        'course': 'python',
        'author': 'Jim Shaped'
    }
    response = requests.post(URL, headers = headers)
    if response.status_code == 200:
        payload = response.json()
        print(payload['headers']['Course'])

def put_example():
    URL = "https://httpbin.org/put"
    params = {
        'name': 'Javs',
    }
    headers = {
        'version': '2.0'
    }
    data = {
        'id': 1
    }
    response = requests.put(URL,params = params,headers = headers,data = data)
    if response.status_code == 200:
        print(response.text)
    
def cookies_example():
    URL = "https://httpbin.org/cookies"
    cookies = {
        'user': 'luis',
        'session': '123'
    }
    response = requests.get(URL,cookies = cookies)
    if response.status_code == 200:
        print(response.json())
        
if __name__ == '__main__':
    cookies_example()
