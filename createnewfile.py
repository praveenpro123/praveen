def createNewFile(repo_fullname,username,password,filename, commit_message, file_content, branch_name):
    try:
        import github
        login = github.Github(username, password)
        repo = login.get_repo(repo_fullname)
        repo.create_file(filename, commit_message, file_content, branch_name)
        return {'status': 'Pass', 'repo': repo.full_name, 'error': None}
    except github.BadCredentialsException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except github.UnknownObjectException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except github.GithubException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except Exception as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
repo_fullname="praveenpro123/praveen"
username="praveenpro123"
password="Naveenkr@123"
filename="Test"
commit_message="Testing"
file_content="Hello"
branch_name="branch"
print(createNewFile(repo_fullname,username,password,filename, commit_message, file_content, branch_name))
