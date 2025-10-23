from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateFileRequestDict(TypedDict):
    """
    Description of the file creation request structure.
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """
    Client for working with /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Method for retrieving a file
        :param file_id: The file's identifier.
        :return: The server's response as an httpx.Response object.
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Method for creating a file
        :param request: A dictionary containing filename, directory, and upload_file.
        :return: The server's response as an httpx.Response object.
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        МMethod for deleting a file
        :param file_id: The file's identifier.
        :return: The server's response as an httpx.Response object.
        """
        return self.delete(f"/api/v1/files/{file_id}")
