from http import HTTPStatus

import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response

# Import the assertion function for validating user creation response
from tools.assertions.users import assert_create_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
def test_create_user(email: str, public_users_client: PublicUsersClient): #def test_create_user(public_users_client:PublicUsersClient):
    request = CreateUserRequestSchema(email=fake.email(domain=email))  #request = CreateUserRequestSchema()

    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Use the function to check the status code
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Use the function to verify the user creation response
    assert_create_user_response(request, response_data)

    # assert response_data.user.email == request.email, 'Incorrect user email'
    # assert response_data.user.last_name == request.last_name, 'Incorrect user last_name'
    # assert response_data.user.first_name == request.first_name, 'Incorrect user first_name'
    # assert response_data.user.middle_name == request.middle_name, 'Incorrect user middle_name'

    validate_json_schema(response.json(), response_data.model_json_schema())

    # python -m pytest -m users -s -v

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, function_user.response)

    validate_json_schema(response.json(), response_data.model_json_schema())


# python -m pytest -m regression -s -v
