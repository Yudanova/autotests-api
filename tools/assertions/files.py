import httpx

from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response,assert_internal_error_response
from clients.files.files_schema import FileSchema



def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Checks that the file creation response matches the request.

    :param request: The original file creation request.
    :param response: The API response with the file data.
    :raises AssertionError: If at least one field does not match.
    """
    # Generating the expected link to the downloaded file
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")


def assert_file_is_accessible(url: str):
    """
    Checks that the file is available at the specified URL.

    :param url: Link to the file.

    :raises AssertionError: If the file is not available.
    """
    response = httpx.get(url)
    assert response.status_code == 200, f"The file is not available at the URL.: {url}"


def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Checks that the actual file data matches the expected data.

    :param actual: The actual file data.
    :param expected: The expected file data.
    :raises AssertionError: If at least one field does not match.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Checks that the response for retrieving a file matches the response for creating it.

    :param get_file_response: The API response when requesting file data.
    :param create_file_response: The API response when creating a file.
    :raises AssertionError: If the file data does not match.
    """
    assert_file(get_file_response.file, create_file_response.file)

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that the response for creating a file with an empty filename
    matches the expected validation error.

    Args:
        actual (ValidationErrorResponseSchema): The API response with a validation error to be checked.

    Raises:
        AssertionError: If the actual response does not match the expected one.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="", # Empty directory
                context={"min_length": 1}, # min length = 1
                message="String should have at least 1 character", # error message
                location=["body", "filename"] # # error occur in the response body "directory" directory.
            )
        ]
    )

    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that the response for creating a file with an empty directory value
    matches the expected validation error.

    Args:
        actual (ValidationErrorResponseSchema): The API response with a validation error to be checked.

    Raises:
        AssertionError: If the actual response does not match the expected one.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)




def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that the response for getting a file with an incorrect file_id
    matches the expected UUID parsing validation error.

    Args:
        actual (ValidationErrorResponseSchema): The API response with a validation error.

    Raises:
        AssertionError: If the actual response does not match the expected one.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={
                    "error": (
                        "invalid character: expected an optional prefix of `urn:uuid:` "
                        "followed by [0-9a-fA-F-], found `i` at 1"
                    )
                },
                message=(
                    "Input should be a valid UUID, invalid character: expected an optional prefix "
                    "of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                ),
                location=["path", "file_id"]
            )
        ]
    )

    assert_validation_error_response(actual, expected)

