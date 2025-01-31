import requests
import json


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'

    def getUser(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
        
    def getRepositories(self,username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def createRepository(self,name):
        headers = {
        "Authorization": f"token {self.token}",
        "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "name" : "Hello-World",
            "descripton" : "This is your first repository",
            "homepage" : "https://github.com",
            "private" : False,
            "has_issues" : True,
            "has_projects" : True,
            "has_wiki" : True
        }
        response = requests.post(self.api_url + '/user/repos', headers=headers, json=data)
        return response.json()
     
github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username =  input('username: ')
            result = github.getUser(username)
            if 'message' in result and result['message'] == 'Not Found':
                print('User not found.')
            else:
                print(f"Name: {result.get('name', 'N/A')}, Public Repos: {result.get('public_repos', 0)}, Followers: {result.get('followers', 0)}")

        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])

        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)

        else:
            print('Yanlış seçim')