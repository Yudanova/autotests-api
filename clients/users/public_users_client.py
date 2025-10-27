from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

# Added description of the user structure
class User(TypedDict):
    """
    Describes the structure of a user.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):
    """
    Describes the structure of the request for creating a user.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

# Added description of the user creation response structure
class CreateUserResponseDict(TypedDict):
    """
    Describes the structure of the response when creating a user.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Client for interacting with /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Method for creating a user.

        :param request: Dictionary containing email, password, lastName, firstName, middleName.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/users", json=request)

    # Added new method
    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Function creates an instance of PublicUsersClient with a preconfigured HTTP client.

    :return: A ready-to-use PublicUsersClient instance.
    """
    return PublicUsersClient(client=get_public_http_client())