import pytest

from pydantic import BaseModel
from clients.errors_schema import InternalErrorResponseSchema, ValidationErrorSchema, ValidationErrorResponseSchema
from tools.assertions.errors import assert_internal_error_response

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Verifies that the error response corresponds to a "File not found" error on the server.

    Args:
        actual (InternalErrorResponseSchema): The actual API response.

    Raises:
        AssertionError: If the actual response does not match the expected "File not found" error.
    """
    # Expected error message if the file is not found
    expected = InternalErrorResponseSchema(details="File not found")
    # Use the previously created function to check the internal error
    assert_internal_error_response(actual, expected)
