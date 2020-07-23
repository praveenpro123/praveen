import git

def git_merge_operation(local_repo, commit_message, branch1, branch2):
	try:
		repo = git.Repo(local_repo)													
		current_branch = repo.active_branch										
		branch_a = repo.branches[branch1]										
		branch_b = repo.branches[branch2]										
		base = repo.merge_base(branch_a, branch_b)								
		repo.index.merge_tree(branch_b, base=base)							    
		repo.index.commit(commit_message, parent_commits=(branch_a.commit, branch_b.commit))            
		branch_a.checkout(force=True)
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

	except Exception as error:
		return {'status': 'Fail', 'error': str(error)}

local_repo = "c:\\testing"
branch1 = "branch"
branch2 = "local"
commit_message = 'branch and local merged successfully'

print(git_merge_operation(local_repo, commit_message, branch1, branch2))
