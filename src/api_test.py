import requests

# Send a GET request to a sample API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check the status code
assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

# Verify the content of the response
data = response.json()
assert data["id"] == 1, f"Unexpected ID: {data['id']}"
print("API test passed successfully!")
