import requests

BASEURL = "http://127.0.0.1:8000/tenders/"

def test_can_call_endpoint():
    response = requests.get(BASEURL)
    assert response.status_code == 200
    pass