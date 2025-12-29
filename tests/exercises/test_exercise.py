from clients.exercises.exercises_client import ExercisesClient, get_exercises_client

from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema




class TestExercise:
    def test_create_exercise(self, function_exercise):
        assert function_exercise.response.exercise.id is not None
        assert function_exercise.request.course_id == function_exercise.response.exercise.course_id

