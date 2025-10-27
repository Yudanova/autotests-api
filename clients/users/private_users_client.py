from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

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

# Added description of the user retrieval response structure
class GetUserResponseDict(TypedDict):
    """
    Describes the structure of the response when retrieving a user.
    """
    user: User

class UpdateUserRequestDict(TypedDict):
    """
    Describes the structure of the request for updating a user.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    """
    Client for interacting with /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Method for retrieving the current user.

        :return: Server response as an httpx.Response object
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Method for retrieving a user by ID.

        :param user_id: User identifier.
        :return: Server response as an httpx.Response object
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Method for updating a user by ID.

        :param user_id: User identifier.
        :param request: Dictionary containing email, lastName, firstName, middleName.
        :return: Server response as an httpx.Response object
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Method for deleting a user by ID.

        :param user_id: User identifier.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/users/{user_id}")

    # Added new method
    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()

def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Function creates an instance of PrivateUsersClient with a preconfigured HTTP client.

    :return: A ready-to-use PrivateUsersClient instance.
    """
    return PrivateUsersClient(client=get_private_http_client(user))