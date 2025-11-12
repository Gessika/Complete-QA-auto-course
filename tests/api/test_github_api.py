import pytest
from modules.api.clients.github import GitHub #create api client for communication with github


@pytest.mark.api
#def test_user_exist():
    #api = GitHub() #initiate class instance (exempliar) and stor in api variable
    #user = api.get_user_defunkt() #get user
    #assert user['login'] == 'defunkt'

def test_user_exists(github_api): #we want to check if user exists
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
#def test_user_not_exist()
#api = GitHub()
#r = api.get_non_exist_user()
#print(r)  # -> then in terminal write: pytest -s -m api :=> output result from print to terminal 
def test_user_not_exists(github_api): #get non-exist user
    r = github_api.get_user('irynamatukhno')
    assert r ['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('Complete-QA-auto-course')
    #print(r)
    assert r['total_count'] == 13
    assert 'Complete-QA-auto-course' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('iramatukhno_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0