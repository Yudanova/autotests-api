from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class Token(TypedDict):  # Added structure for authentication tokens
    """
    Describes the structure of authentication tokens.
    """
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):
    """
    Describes the structure of the authentication request.
    """
    email: str
    password: str

class LoginResponseDict(TypedDict):  # Added structure for authentication response
    """
    Describes the structure of the authentication response.
    """
    token: Token

class RefreshRequestDict(TypedDict):
    """
    Describes the structure of the token refresh request.
    """
    refreshToken: str

class AuthenticationClient(APIClient):
    """
    Client for interacting with /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Method for authenticating a user.

        :param request: Dictionary containing email and password.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Method for refreshing the authentication token.

        :param request: Dictionary containing refreshToken.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    # Added login method
    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)  # Send authentication request
        return response.json()  # Extract JSON from the response

def get_authentication_client() -> AuthenticationClient:
    """
    Function creates an instance of AuthenticationClient with a preconfigured HTTP client.

    :return: A ready-to-use AuthenticationClient instance.
    """
    return AuthenticationClient(client=get_public_http_client())