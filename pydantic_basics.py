"""
{
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "estimatedTime": "string"
}
"""


from pydantic import BaseModel, Field, ValidationError,field_validator, ConfigDict
from typing import List
from pydantic.alias_generators import to_camel
import uuid

from pydantic import EmailStr, HttpUrl


# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True   # default value
#
# # Valid data
# user = User(id='123', name='Anna', email='anna@example.com')
# print(user)
# print(user.id, type(user.id))  # converted automatically to int
#
# # Invalid data Pydantic automatically converted '123' → 123 (string → int).
# # But 'abc' can’t be converted → it raised a validation error.
# try:
#     invalid_user = User(id='abc', name='Anna', email='anna@example.com')
# except ValidationError as e:
#     print(e)
#
#
# # Nested models
#
# class Address(BaseModel):
#     city: str
#     country: str
#
# class User(BaseModel):
#     name: str
#     age: int
#     addresses: List[Address]
#
# data = {
#     "name": "Alice",
#     "age": 30,
#     "addresses": [
#         {"city": "Tel Aviv", "country": "Israel"},
#         {"city": "Milan", "country": "Italy"}
#     ]
# }
#
# user = User(**data)
# print(user.model_dump())  # serialize to dict
# # Pydantic automatically created and validated each nested Address object.
#
#
# # Validation and transformation, add custom validation
# class User(BaseModel):
#     name: str
#     age: int
#
#     @field_validator("age")
#     def check_age(cls, value):
#         if value < 0:
#             raise ValueError("Age must be positive")
#         return value
#
# user = User(name="Anna", age=28)
# print(user)
#
# # user = User(name="Anna", age=-5) → raises validation error
#
# # Using environment variables (for configs). Needed for configuration management — it automatically reads .env files and validates the environment variables
# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     app_name: str
#     debug: bool = False
#     database_url: str
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()
# print(settings.app_name)


# Added the FileSchema model
class FileSchema(BaseModel):
    id: str
    url: HttpUrl  # Using HttpUrl instead of str
    filename: str
    directory: str


# Added the UserSchema model
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Using EmailStr instead of str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    # Nested object for the preview file
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    # Nested object for the user who created the course
    created_by_user: UserSchema = Field(alias="createdByUser")


# Initialize the CourseSchema model by passing arguments
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Added initialization of the nested FileSchema model
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # Added initialization of the nested UserSchema model
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
print('Course default model:', course_default_model)

# Initialize the CourseSchema model by unpacking a dictionary
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    # Added the previewFile key
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    # Added the createdByUser key
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print(course_dict_model.model_dump())
print(course_dict_model.model_dump(by_alias=True))

# Initialize the CourseSchema model using JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)

# Initialize FileSchema with an invalid URL
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())






