from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


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


class CreateCourseRequestSchema(BaseModel):
    """
    Description request structure for creating course List.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


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

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")












from pydantic import BaseModel
from typing import Optional

class CreateCourseRequestSchema(BaseModel):
    title: str
    max_score: int
    min_score: int
    description: Optional[str]
    estimated_time: Optional[str]
    preview_file_id: str
    created_by_user_id: str

class CreateCourseResponseSchema(BaseModel):
    id:str
    title: str
    max_score: int
    min_score: int
    description: Optional[str]
    estimated_time: Optional[str]
    preview_file_id: str
    created_by_user_id: str