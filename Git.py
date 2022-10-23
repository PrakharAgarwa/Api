import requests
import json

def Hw04(username):
    response = requests.get("https://api.github.com/users/"+username+"/repos")
    
    if response.status_code != 200:
        print("No Account Found")
        return False

    response = response.json()

    if len(response) == 0:
        print("Cant locate any Repo")
        return False
    
    for repo in response:
        repoResponse = requests.get("https://api.github.com/repos/"+username+"/"+repo['name']+"/commits")
        repoResponse = repoResponse.json()
        print("Repository Name:"+ repo['name']+"     "+"Number Of Commits: ",str(len(repoResponse)))
   
    return True

if __name__ == "__main__":
    userInput = input("Enter the Username: ")
    Hw04(userInput)
