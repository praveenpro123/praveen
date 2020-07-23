def git_get_archive_link(username, reponame, archive_type, branch_name):
	return 'https://api.github.com/repos/'+username+'/'+reponame+'/'+archive_type+'/'+branch_name

username = "praveenpro123"
reponame = "praveen"
archive_type = "zipball"
branch_name = "branch"

print (git_get_archive_link(username, reponame, archive_type, branch_name))
