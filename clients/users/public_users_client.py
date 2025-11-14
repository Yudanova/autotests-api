from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema


class PublicUsersClient(APIClient):
    """
    Client for interacting with /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        1) Replacing TypedDict models with Pydantic.
        2) We use model_dump(by_alias=True) to serialize the request.
        3) We use  to parse the response. This is a safe way to load a JSON response,
        preventing errors when working with raw data.

        Method for creating a user.

        :param request: Dictionary with email, password, lastName, firstName, middleName.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Function creates an instance of PublicUsersClient with a preconfigured HTTP client.

    :return: A ready-to-use PublicUsersClient instance.
    """
    return PublicUsersClient(client=get_public_http_client())