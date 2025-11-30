from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
from tools.assertions.base import assert_equal



def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Verifies that the user creation response matches the original request.

    :param request: The original user creation request.
    :param response: The API response containing user data.
    :raises AssertionError: If any field does not match.

    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Verifies that the actual user data matches the expected data.

    :param actual: The actual user data.
    :param expected: The expected user data.
    :raises AssertionError: If at least one field does not match.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Verifies that the response for retrieving a user matches the response for creating the user.

    Args:
        get_user_response (GetUserResponseSchema): The API response when requesting user data.
        create_user_response (CreateUserResponseSchema): The API response when creating the user.

    Raises:
        AssertionError: If the user data does not match.


    """
    assert_user(get_user_response.user, create_user_response.user)