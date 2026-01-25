from http import HTTPStatus
import allure
from allure_commons.types import Severity
import pytest
from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema,GetFileResponseSchema
from fixtures.files import FileFixture
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic  # Added enum AllureEpic
from tools.allure.features import AllureFeature  # Import enum AllureFeature
from tools.allure.stories import AllureStory  # Import enum AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_create_file_with_empty_filename_response, \
    assert_create_file_with_empty_directory_response, assert_file_not_found_response, assert_get_file_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.files import assert_get_file_with_incorrect_file_id_response





@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # Added epic
@allure.feature(AllureFeature.FILES)  # Added feature
class TestFiles:   # positive
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)  # Added story
    @allure.title("Create file")
    @allure.severity(Severity.BLOCKER)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get file")
    @allure.story(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())


# python -m pytest -k "test_create_file"
# python -m pytest -k "test_get_file"

   # class TestFiles:   # negative
    @allure.title("Create file with empty filename")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        """
        Verifies that creating a file with an empty filename
        returns the expected validation error response.

        Steps:
            1. Send a request with an empty filename and a valid file upload.
            2. Check that the response status code is 422 (Unprocessable Entity).
            3. Verify that the API response matches the expected validation error.
            4. Validate the JSON schema to ensure the response structure has not changed.
        """
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/image.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # Check that the response code matches expectations (422 - Unprocessable Entity)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # Check that the API response matches the expected validation error
        assert_create_file_with_empty_filename_response(response_data)
        # Additional check of JSON structure to ensure the validation error schema has not changed
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create file with empty directory")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        """
        Verifies that creating a file with an empty directory value
        returns the expected validation error response.

        Steps:
            1. Send a request with an empty directory and a valid file upload.
            2. Check that the response status code is 422 (Unprocessable Entity).
            3. Verify that the API response matches the expected validation error.
            4. Validate the JSON schema to ensure the response structure has not changed.
        """
        request = CreateFileRequestSchema(
            directory="",
            upload_file="./testdata/files/image.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # Check that the response code matches expectations (422 - Unprocessable Entity)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # Check that the API response matches the expected validation error
        assert_create_file_with_empty_directory_response(response_data)
        # Additional check of JSON structure
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Delete file")
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        """
        Verifies that deleting a file works correctly and that subsequent access
        to the deleted file returns the expected error.

        Steps:
            1. Delete the file using its ID.
            2. Check that the file was successfully deleted (status 200 OK).
            3. Attempt to retrieve the deleted file.
            4. Verify that the server returns 404 Not Found.
            5. Verify that the response contains the "File not found" error.
            6. Validate the JSON schema to ensure the response structure is correct.
        """
        # 1. Delete the file
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        # 2. Verify that the file was successfully deleted (status 200 OK)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        # 3. Attempt to retrieve the deleted file
        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        # 4. Verify that the server returned 404 Not Found
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        # 5. Verify that the response contains the "File not found" error
        assert_file_not_found_response(get_response_data)

        # 6. Validate that the response matches the schema
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.title("Get file with incorrect file id")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        response = files_client.get_file_api("incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    # python -m pytest -k "test_delete_file"