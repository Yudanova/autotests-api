from pydantic import BaseModel, HttpUrl, Field
# Import the pre-created instance of the Fake class
from tools.fakers import fake

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
    Description of the request structure for creating a file.
    """
    # Added random filename generation with PNG extension
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    # Directory is kept static so all test files on the server go into one folder
    directory: str = Field(default="tests")
    upload_file: str





#default_factory, the filename will be automatically generated as a random UUID followed by .png:
#create_file_request = CreateFileRequestSchema(upload_file="file_data")
#directory:
#We keep the static value `"tests"` to simplify testing — all uploaded test files will go into a single folder.




class CreateFileResponseSchema(BaseModel):
    """
     Description the Response structure for creation the file.
    """
    file: FileSchema


# Calling print(CreateFileRequestSchema(upload_file="./text/file.txt")) will output a model instance where:
# - filename is auto-generated as a random UUID with .png extension
# - directory is set to the static value "tests"
# - upload_file is manually provided as "./text/file.txt"
#
#
# print(CreateFileRequestSchema(upload_file="./text/file.txt"))
# Example output:
# filename='64a63696-7538-475b-a04f-a1f86f08d480.png' directory='tests' upload_file='./text/file.txt'












