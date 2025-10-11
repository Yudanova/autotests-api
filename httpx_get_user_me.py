import httpx

# Step 1: Sending POST-request to login existed user
login_payload = {
    "email": "gogo@example.com",
    "password": "string"
}

login_url = "http://localhost:8000/api/v1/authentication/login"
login_response = httpx.post(login_url, json=login_payload)

# Succesfull login verification
if login_response.status_code == 200:
    login_data = login_response.json()
    access_token = login_data["token"]["accessToken"]

    # Step 2: Sending GET-request with token
    get_user_headers = {
        "Authorization": f"Bearer {access_token}"
    }

    get_user_url = "http://localhost:8000/api/v1/users/me"
    get_user_response = httpx.get(get_user_url, headers=get_user_headers)

    # Step 3: Print output
    print("Status Code:", get_user_response.status_code)
    print("User data:")
    print(get_user_response.json())

else:
    print("Login error. Status Code:", login_response.status_code)
    print("Response:", login_response.text)

# Option 2

login_payload = {

    "email": "gogo@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

get_user_headers = {

    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_headers)
get_user_response_data = get_user_response.json()

# Refresh Token
print("Get user response:", get_user_response_data)
print("Get user status code:", get_user_response.status_code)

