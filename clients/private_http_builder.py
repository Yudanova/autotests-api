from functools import lru_cache
from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
# Importing the LoginRequestSchema model
from clients.authentication.authentication_schema import LoginRequestSchema

# Added suffix Schema instead of Dict
class AuthenticationUserSchema(BaseModel):  # Inherit from BaseModel instead of TypedDict
    email: str
    password: str
    model_config = {"frozen": True}

@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentication_client = get_authentication_client()

    # Using the LoginRequestSchema model
    # Values are now accessed through attributes instead of dictionary keys
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Values are now accessed through attributes instead of dictionary keys
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )

# class AuthenticationUserDict(TypedDict):  # Data structure for user authentication
#     email: str
#     password: str
#
# # Create private builder
# def get_private_http_client(user: AuthenticationUserDict) -> Client:
#     """
#     This function creates an instance of httpx.Client with user authentication.
#
#     :param user: AuthenticationUserSchema object containing the user's email and password.
#     :return: A ready-to-use httpx.Client object with the Authorization header set.
#     """
#     # Initialize AuthenticationClient for authentication
#     authentication_client = get_authentication_client()
#
#     # Prepare the authentication request
#     login_request = LoginRequestDict(email=user['email'], password=user['password'])
#     # Perform POST request and authenticate
#     login_response = authentication_client.login(login_request)
#
#     return Client(
#         timeout=100,
#         base_url="http://localhost:8000",
#         # Add Authorization header
#         headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
#     )