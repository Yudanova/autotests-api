from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
# Import the pre-created instance of the Fake class
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Description course structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    """
    Description request structure for getting course List.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")

class GetCoursesResponseSchema(BaseModel):
    """
    Description request structure for getting course List.
    """
    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    """
    Description request structure for creating course List.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Added random title generation
    title: str = Field(default_factory=fake.sentence)
    # Added random maximum score generation
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    # Added random minimum score generation
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    # Added random description generation
    description: str = Field(default_factory=fake.text)
    # Added random estimated course duration generation
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    # Added random file ID generation
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    # Added random user ID generation
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

"""
Random data of preview_file_id and created_by_user_id are not suitable for tests with valid data. 
It’s only appropriate for negative test cases.
When the course should be created successfully you need to pass real IDs of existing files and users like:
create_course_request = CreateCourseRequestSchema(
    preview_file_id="a1b2c3d4-5678-90ab-cdef-1234567890ab",
    created_by_user_id="user-uuid-1234-5678-90ab-cdef"
)

For negative tests (e.g., “File not found”, “User not found”), you can use randomly generated UUIDs:
create_course_request = CreateCourseRequestSchema()

"""


    # title: str
    # max_score: int = Field(alias="maxScore")
    # min_score: int = Field(alias="minScore")
    # description: str
    # estimated_time: str = Field(alias="estimatedTime")
    # preview_file_id: str = Field(alias="previewFileId")
    # created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """
    Description response structure of creating course.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Description request structure of updating course.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Added random title generation
    title: str | None = Field(default_factory=fake.sentence)
    # Added random maximum score generation
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    # Added random minimum score generation
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    # Added random description generation
    description: str | None = Field(default_factory=fake.text)
    # Added random estimated course duration generation
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
"""
In `UpdateCourseRequestSchema`, all fields can be `None`, allowing you to update only the specific data you need.

The schema does not include `preview_file_id` or `created_by_user_id`, 
since updating a course does not involve changing its author or preview file.

"""
    # title: str | None
    # max_score: int | None = Field(alias="maxScore")
    # min_score: int | None = Field(alias="minScore")
    # description: str | None
    # estimated_time: str | None = Field(alias="estimatedTime")

class UpdateCourseResponseSchema(BaseModel):
    """
        Structure description of the updated course's response
        """
    course: CourseSchema














