from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class UpdateUserRequestDict(TypedDict):
    """
    Description of the user update request structure.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Client for working with /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Method for retrieving the current user.

        :return: The server's response as an httpx.Response object.
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Method for retrieving a user by ID.
        :param user_id: The user's identifier.
        :return: The server's response as an httpx.Response object.

        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Method for updating a user by ID.
        :param user_id: The user's identifier.
        :param request: A dictionary containing email, lastName, firstName, and middleName.
        :return: The server's response as an httpx.Response object.

        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Method for deleting a user by ID.
        :param user_id: The user's identifier.
        :return: The server's response as an httpx.Response object.

        """
        return self.delete(f"/api/v1/users/{user_id}")
