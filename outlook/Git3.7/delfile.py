import github

def git_delete_file(username, password, repo_fullname, filename, commit_message, branch):
	try:
		login = github.Github(username, password)							
		repo = login.get_repo(repo_fullname)						
		contents = repo.get_contents(filename)				
		repo.delete_file(contents.path, commit_message, contents.sha, branch)				
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

username = "praveenpro123"
password = "Naveenkr@123"
repo_fullname = "praveenpro123/praveen"
filename =  "Test"
commit_message = "deleting the file"
branch = "branch"

print (git_delete_file(username, password, repo_fullname, filename, commit_message, branch))
