import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture

# Creating an ExerciseFixture model
# It stores both the request and response so that tests can easily access the data----->
class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


# The fixture expects function_user: UserFixture
# takes the authentication_user object from user
# passes it to get_exercises_client
# receives the authorized client ------>
@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


# Receives the client
# Receives the course created by the function_course fixture
# Creates a request object
# Sends it via exercises_client
# Returns the ExerciseFixture --->
@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(
        course_id=function_course.response.course.id
    )
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)

