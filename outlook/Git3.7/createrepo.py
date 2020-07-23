import github
def createRepository(repo_name,username,password):
    
    try:
        login = github.Github(username, password)       
        user = login.get_user() 
        repo = user.create_repo(repo_name)       
        return {'status': 'Pass', 'repo': str(repo.full_name), 'error': None}
    except github.BadCredentialsException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except github.GithubException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except Exception as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
repo_name="praveen"
username="praveenpro123"
password="Naveenkr@123"
print(createRepository(repo_name,username,password))
