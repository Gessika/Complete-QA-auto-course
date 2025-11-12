import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen') #test sends HTTP request with method GET to address and save servers response to variable
    print(f"Response is {r.text}") #using f-strings displays the attribute text of the response from the server


@pytest.mark.http
def test_second_request(): #request full info about user account
    r = requests.get('https://api.github.com/users/defunkt')
    
    #print(f"Response Body is {r.json()}") #data that the server passes to the request in the method json
    body = r.json() #we write value of json method to name body
    assert body['name'] == 'Chris Wanstrath' #check that name = Expected name from body


    #print(f"Response Status Code is {r.status_code}") #show status code on display
    assert r.status_code == 200  #status code check, so we TEST response, not just DISPLAY it as above commented
    
    #print(f"Response Headers are {r.headers}")
    headers = r.headers
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_status_code_request(): #request full info about user account
    r = requests.get('https://api.github.com/users/iryna_matukhno')
    assert r.status_code == 404