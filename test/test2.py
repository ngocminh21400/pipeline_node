import requests

def test_random_api_status_code_euqal_200():
     response = requests.get("http://localhost:4000/random")
     assert response.status_code == 200

def test_random_api_response_less_than_1():
    response = requests.get("http://localhost:4000/random")
    assert response.json() < 1
    
def test_random_api_response_greater_than_0():
    response = requests.get("http://localhost:4000/random")
    assert response.json() > 0