import httpx
from tools.fakers import get_random_email  # import random fake email

payload = {
    "email": get_random_email(),  # using random generation email
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
