from fastapi.testclient import TestClient

from pet import app

client = TestClient(app)

def test_add_pet():
  response = client.post(
      "/pet",
      headers={ "accept": "application/json", "Content-Type": "application/json" },
      json={ "id": 0, "name": "doggie", "status": "available" }
  )
  assert response.status_code == 200
  assert response.json() == { "id": 0, "name": "doggie", "status": "available" }