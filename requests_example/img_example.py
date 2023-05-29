import requests

def get_image(URL,path):
    '''
    Method to download any file from a remote server
    '''
    response = requests.get(URL,stream = True)           #keep open the connection
    if response.status_code == 200:
        with open(path,'wb') as file:                    #create a local file
            for chunk in response.iter_content(1024):    #iterate in chunks the remote file
                file.write(chunk)                        #write in local file
    
    
if __name__ == '__main__':
    URL = "https://images.pexels.com/photos/2662116/pexels-photo-2662116.jpeg"
    path = "images/test.jpeg"
    get_image(URL,path)    
