import requests

class GitHub:

    # def get_user_defunkt(self):
    #     r = requests.get('https://api.github.com/users/defunkt')#send request to url address github documentation and store it on "r" variable
    #     body = r.json() #get the body from http-resp, and store it in a variable
    #     return body
    
    # def get_non_exist_user(self):
    #     r = requests.get('https://api.github.com/users/iryna_matukhno')
    #     body = r.json() #get the body from http-response, and store it in a variable
    #     return body
    
    def get_user(self, username):
         r = requests.get(f'https://api.github.com/users/{username}')
         body = r.json() #get the body from http-response, and store it in a variable
         return body
    
    def search_repo(self, name):
         r = requests.get("https://api.github.com/search/repositories", params={"q": name})
         body = r.json()

         return body

