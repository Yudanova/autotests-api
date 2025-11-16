from faker import Faker
import requests


fake = Faker()

print(fake.name())         # Output: John Doe
print(fake.address())      # Output: 1234 Elm St, Springfield, IL
print(fake.email())        # Output: j.doe@example.com

fake = Faker()

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}

print(user_data)


fake = Faker()

# Generate fake data
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

# Send a POST request with the fake data
response = requests.post("https://api.example.com/users", json=user_data)

# Check that the request was successful
assert response.status_code == 201
# This domain is just example:  api.example.com is a placeholder.
# Need to using environment variables or config files to manage base URLs for different environments (dev, staging, prod).
