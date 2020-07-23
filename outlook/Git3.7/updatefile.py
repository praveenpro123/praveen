def updatefile(username,password,filename,repo_fullname,commit_message,update_text,branch):
    try:
        import github
        login = github.Github(username, password)
        repo = login.get_repo(repo_fullname)
        contents = repo.get_contents(filename)
        repo.update_file(contents.path, commit_message, update_text, contents.sha, branch)
        return {'status': 'Pass', 'repo': repo.full_name, 'error': None}
    except github.BadCredentialsException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except github.UnknownObjectException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except github.GithubException as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except AttributeError as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except IndexError as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
    except Exception as error:
        return {'status': 'Fail', 'repo': None, 'error': str(error)}
username="praveenpro123"
password="Naveenkr@123"
filename="Test"
repo_fullname="praveenpro123/praveen"
commit_message="second"
update_text="how are you"
branch="branch"    
print (updatefile(username,password,filename,repo_fullname,commit_message,update_text,branch))
