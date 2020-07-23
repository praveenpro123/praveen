import git

def git_fetch_repo(local_repo, remote_repo_name):
	try:
		repo = git.Repo(local_repo)									
		repo.git.fetch(remote_repo_name)							
		return {'status': 'Pass', 'error': None}
                        
	except git.exc.NoSuchPathError as error:
		return {'status': 'Fail', 'error': str(error) + ', No such folder exists'}

	except git.exc.InvalidGitRepositoryError as error:
		return {'status': 'Fail', 'error': str(error) + ' is a Invalid git repository'}
                       
	except git.exc.GitCommandError as error:
		return {'status': 'Fail', 'error': str(error)}

	except Exception as error:
		return {'status': 'Fail', 'error': str(error)}

local_repo = "C:\\testing"
remote_repo_name = 'https://github.com/praveenpro123/praveen.git'

print(git_fetch_repo(local_repo, remote_repo_name))
