from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
# Added import of models
from clients.authentication.authentication_schema import LoginRequestSchema,LoginResponseSchema,RefreshRequestSchema

# Old models using TypedDict were commented out, (removed)

class AuthenticationClient(APIClient):
    """
    Client for working with /api/v1/authentication
    """

    # Now we use a Pydantic model for type annotation
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Method performs user authentication.

        :param request: A dictionary with email and password.
        :return: Server response as an httpx.Response object.
        """
        return self.post(
            "/api/v1/authentication/login",
            # Serialize the model into a dictionary using aliases
            json=request.model_dump(by_alias=True)
        )

    # Now we use a Pydantic model for type annotation
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Method refreshes the authorization token.

        :param request: A dictionary with refreshToken.
        :return: Server response as an httpx.Response object.
        """
        return self.post(
            "/api/v1/authentication/refresh",
            # Serialize the model into a dictionary using aliases
            json=request.model_dump(by_alias=True)
        )

    # Now we use a Pydantic model for type annotation
    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        # Initialize the model through JSON string validation
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Function creates an instance of AuthenticationClient with a preconfigured HTTP client.

    :return: Ready-to-use AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())

# class Token(TypedDict):  # Added structure for authentication tokens
#     """
#     Describes the structure of authentication tokens.
#     """
#     tokenType: str
#     accessToken: str
#     refreshToken: str
#
# class LoginRequestDict(TypedDict):
#     """
#     Describes the structure of the authentication request.
#     """
#     email: str
#     password: str
#
# class LoginResponseDict(TypedDict):  # Added structure for authentication response
#     """
#     Describes the structure of the authentication response.
#     """
#     token: Token
#
# class RefreshRequestDict(TypedDict):
#     """
#     Describes the structure of the token refresh request.
#     """
#     refreshToken: str
#
# class AuthenticationClient(APIClient):
#     """
#     Client for interacting with /api/v1/authentication
#     """
#
#     def login_api(self, request: LoginRequestDict) -> Response:
#         """
#         Method for authenticating a user.
#
#         :param request: Dictionary containing email and password.
#         :return: Server response as an httpx.Response object
#         """
#         return self.post("/api/v1/authentication/login", json=request)
#
#     def refresh_api(self, request: RefreshRequestDict) -> Response:
#         """
#         Method for refreshing the authentication token.
#
#         :param request: Dictionary containing refreshToken.
#         :return: Server response as an httpx.Response object
#         """
#         return self.post("/api/v1/authentication/refresh", json=request)
#
#     # Added login method
#     def login(self, request: LoginRequestDict) -> LoginResponseDict:
#         response = self.login_api(request)  # Send authentication request
#         return response.json()  # Extract JSON from the response
#
# def get_authentication_client() -> AuthenticationClient:
#     """
#     Function creates an instance of AuthenticationClient with a preconfigured HTTP client.
#
#     :return: A ready-to-use AuthenticationClient instance.
#     """
#     return AuthenticationClient(client=get_public_http_client())