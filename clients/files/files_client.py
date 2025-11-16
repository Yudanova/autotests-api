from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema


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

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Method for creating a file.

        :param request: Pydantic schema containing filename, directory, upload_file.
        :return: Server response as an httpx.Response object
        """
        with open(request.upload_file, "rb") as f:
            files = {"upload_file": (request.filename, f, "image/png")}
            data = {
                "filename": request.filename,
                "directory": request.directory
            }
            return self.post(
                url="/api/v1/files",
                data=data,
                files=files
            )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Method for deleting a file.

        :param file_id: File identifier.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        High-level method for creating a file and returning structured response.

        :param request: Pydantic schema with file creation data.
        :return: Pydantic response schema with file data.
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema(**response.json())


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Function creates an instance of FilesClient with a preconfigured HTTP client.

    :return: A ready-to-use FilesClient instance.
    """
    return FilesClient(client=get_private_http_client(user))