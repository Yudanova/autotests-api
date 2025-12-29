from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema,InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length





def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Verifies that a validation error object matches the expected value.

    Args:
        actual (ValidationErrorSchema): The actual validation error.
        expected (ValidationErrorSchema): The expected validation error.

    Raises:
        AssertionError: If any of the fields do not match.
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


def assert_validation_error_response(
    actual: ValidationErrorResponseSchema,
    expected: ValidationErrorResponseSchema
):
    """
    Verifies that an API response containing validation errors
    (`ValidationErrorResponseSchema`) matches the expected value.

    Args:
        actual (ValidationErrorResponseSchema): The actual API response.
        expected (ValidationErrorResponseSchema): The expected API response.

    Raises:
        AssertionError: If any of the fields do not match.
    """
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)

def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    assert_equal(actual.details, expected.details, "details")