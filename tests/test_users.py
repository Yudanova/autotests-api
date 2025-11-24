from http import HTTPStatus
import pytest

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
# Import the status code assertion function
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

# Import the assertion function for validating user creation response
from tools.assertions.users import assert_create_user_response

@pytest.mark.users
@pytest.mark.regression
def test_create_user():
    public_users_client = get_public_users_client()

    request = CreateUserRequestSchema()
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