from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Description of the exercise structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseResponseSchema(BaseModel):
    """
    Description of the response structure for retrieving an exercise.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Description of the request structure for retrieving a list of exercises.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """
    Description of the response structure for retrieving a list of exercises.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Description of the request structure for creating an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Description of the response structure for exercise creation.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Description of the request structure for updating an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Description of the response structure for exercise update.
    """
    exercise: ExerciseSchema


# from pydantic import BaseModel
# from typing import Optional
#
# class CreateExerciseRequestSchema(BaseModel):
#     title: str
#     description: Optional[str]
#     difficulty: str
#     created_by_user_id: str
#
# class CreateExerciseResponseSchema(BaseModel):
#     id: str
#     title: str
#     description: Optional[str]
#     difficulty: str
#     created_by_user_id: str