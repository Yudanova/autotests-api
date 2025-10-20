from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Description of the request structure for "user" creation.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Client for working with  /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        This method creates a user.
        :param request: A dictionary containing email, password, lastName, firstName, and middleName.
        :return: The server's response as an httpx.Response object.

        """
        return self.post("/api/v1/users", json=request)

