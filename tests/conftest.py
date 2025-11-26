import pytest  # Import pytest
from pydantic import BaseModel, EmailStr
# Import API clients
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema



class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

@pytest.fixture  # Declare a fixture, by default scope is function
def authentication_client() -> AuthenticationClient:  # Object's value returned by the fixture
    # Create a new API client for working with authentication
    return get_authentication_client()


@pytest.fixture  # Declare a fixture, by default scope is function
def public_users_client() -> PublicUsersClient:  # Object's value returned by the fixture
    # Create a new API client for working with the public users API
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)