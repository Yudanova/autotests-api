from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel):
    """
    Description file.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Description the Request structure for creation the file.
    """
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
     Description the Response structure for creation the file.
    """
    file: FileSchema






# class CreateFileRequestSchema(BaseModel):
#     filename: str
#     directory: str
#     upload_file: str  # The path to file
#
# class CreateFileResponseSchema(BaseModel):
#     id: int
#     filename: str
#     directory: str
#     url: str