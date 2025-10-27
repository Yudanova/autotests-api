from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict

class AuthenticationUserDict(TypedDict):  # Data structure for user authentication
    email: str
    password: str

# Create private builder
def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    This function creates an instance of httpx.Client with user authentication.

    :param user: AuthenticationUserSchema object containing the user's email and password.
    :return: A ready-to-use httpx.Client object with the Authorization header set.
    """
    # Initialize AuthenticationClient for authentication
    authentication_client = get_authentication_client()

    # Prepare the authentication request
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    # Perform POST request and authenticate
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Add Authorization header
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )