import requests

def git_download_repo_from_archive_link(archive_link, folderpath):
    try:
        request = requests.get(archive_link, allow_redirects=True)
        print(request.status_code)
        with open(folderpath, 'wb') as f:
            f.write(request.content)
        return {'status': 'Pass', 'error': None}
			
    except requests.exceptions.ConnectionError as error:
        return {'status': 'Fail', 'error': 'Failed to establish a connection'}
		
    except requests.exceptions.HTTPError as error:
        return {'status': 'Fail', 'error': 'HTTP error occurred'}

    except Exception as error:
        return {'status': 'Fail', 'error': str(error)}


archive_link = 'https://api.github.com/repos/praveenpro123/praveen/zipball/local'
folderpath = 'C:\\jiffyservice\\praveen.zip'
print(git_download_repo_from_archive_link(archive_link, folderpath))
