from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client

# Added description of the file structure
class File(TypedDict):
    """
    Describes the structure of a file.
    """
    id: str
    url: str
    filename: str
    directory: str

class CreateFileRequestDict(TypedDict):
    """
    Describes the structure of the request for creating a file.
    """
    filename: str
    directory: str
    upload_file: str

# Added description of the file creation response structure
class CreateFileResponseDict(TypedDict):
    """
    Describes the structure of the response when creating a file.
    """
    file: File

class FilesClient(APIClient):
    """
    Client for interacting with /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Method for retrieving a file.

        :param file_id: File identifier.
        :return: Server response as an httpx.Response object
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Method for creating a file.

        :param request: Dictionary containing filename, directory, upload_file.
        :return: Server response as an httpx.Response object
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Method for deleting a file.

        :param file_id: File identifier.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/files/{file_id}")

    # Added new method
    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()

def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Function creates an instance of FilesClient with a preconfigured HTTP client.

    :return: A ready-to-use FilesClient instance.
    """
    return FilesClient(client=get_private_http_client(user))