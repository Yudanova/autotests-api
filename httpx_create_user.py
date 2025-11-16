import httpx

# Instead of get_random_email, imports fake
from tools.fakers import fake
"""
to replace import from all files-> Ctrl + Shift + R -> from (old import) -> 
to new import (from tools.fakers import fake) -> 'Replace All'
"""

payload = {
    "email": fake.email(), # Using fake.email() instead of fake.email() with function 'Replace All'('from get_random_email()' -> 'fake.email(),' in all files. !!! dont forget use ',' in after fake.email()
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())




# import httpx
# from tools.fakers import fake  # import random fake email
#
# payload = {
#     "email": fake.email(),  # using random generation email
#     "password": "string",
#     "lastName": "string",
#     "firstName": "string",
#     "middleName": "string"
# }
# response = httpx.post("http://localhost:8000/api/v1/users", json=payload)
#
# print(response.status_code)
# print(response.json())
