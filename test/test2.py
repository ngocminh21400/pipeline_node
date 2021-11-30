import requests

def test_get_random_api():
     response = requests.get("http://localhost:4000/random")
     assert response.status_code == 200

