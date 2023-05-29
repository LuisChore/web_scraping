import requests

def get_user():
    URL = 'https://randomuser.me/api'
    response = requests.get(URL)
    print(response.text)
    
def get_users(number_users):
    URL = 'https://randomuser.me/api'
    params = {
        'results': number_users
    }
    response = requests.get(URL,params = params)
    if response.status_code == 200:
        payload = response.json()
        users = payload['results']
        for user in users:
            name = user["name"]
            print(f'{name["title"]} {name["first"]} {name["last"]}') 
    
if __name__ == '__main__':
    get_users(10)
