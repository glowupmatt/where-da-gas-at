from pprint import pprint


def test_docs(client):
    response = client.get("api/docs")
    assert response.status_code == 200
