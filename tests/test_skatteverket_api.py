import pytest
import requests

url = "https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763"


@pytest.mark.parametrize("limit", [10, 15, 20])
def test_get_personnummer_from_skatteverket(limit):

    response = requests.get(url, params={"_limit": limit})

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type")  
    
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) <= limit

    
    for personnummer in data["results"]:
        assert "testpersonnummer" in personnummer
    


