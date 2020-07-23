import git

def git_push_operation(local_repo, remote_repo_name, commit_message, branch_name, file_name):
	try:
		repo = git.Repo(local_repo)											
		current_branch = repo.branches[branch_name]						
		current_branch.checkout(force=True)							
		repo.git.pull(remote_repo_name, branch_name)
		repo.index.add([file_name])										
		repo.index.commit(commit_message)								
		repo.git.push(remote_repo_name, branch_name)					
		return {'status': 'Pass', 'error': None}										
	                        
	except git.exc.NoSuchPathError as error:
		return {'status': 'Fail', 'error': str(error) + ', No such folder exists'}

	except git.exc.InvalidGitRepositoryError as error:
		return {'status': 'Fail', 'error': str(error) + ' is a Invalid git repository'}
                       
	except git.exc.GitCommandError as error:
		return {'status': 'Fail', 'error': str(error)}

	except AttributeError as error:
		return {'status': 'Fail', 'error': str(error)}

	except IndexError as error:
		return {'status': 'Fail', 'error': str(error)}

	except FileNotFoundError as error:
		return {'status': 'Fail', 'error': str(error)}

	except Exception as error:
		return {'status': 'Fail', 'error': str(error)}

local_repo = 'c:\\testing'
commit_message = "adding file to the repository"
branch_name = "branch"
file_name = 'createnewfile.py'
remote_repo_name = 'https://github.com/praveenpro123/praveen.git'

print(git_push_operation(local_repo, remote_repo_name, commit_message, branch_name, file_name))
