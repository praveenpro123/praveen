import git

def git_clone_repo(ssh_repo_url, local_repo):
	try:
		git.Repo.clone_from(ssh_repo_url, local_repo)					
		return {'status': 'Pass', 'error': None}
                       
	except git.exc.NoSuchPathError as error:
		return {'status': 'Fail', 'error': str(error) + ', No such folder exists'}

	except git.exc.GitCommandError as error:
		return {'status': 'Fail', 'error': str(error)}
					
	except Exception as error:
		return {'status': 'Fail', 'error': str(error)}

ssh_repo_url = "https://github.com/praveenpro123/praveen.git"
local_repo = "C:\\testing"
print(git_clone_repo(ssh_repo_url, local_repo))
