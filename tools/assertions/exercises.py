from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import ExerciseSchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response



def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
):
    """
    Verifies that the exercise creation response matches the request.

    Args:
        request (CreateExerciseRequestSchema): The original exercise creation request.
        response (CreateExerciseResponseSchema): The API response containing the created exercise data.

    Raises:
        AssertionError: If any field does not match the expected value.
    """

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema

):
    """
        Verifies that the exercise update response matches the data from the request.

        :param request: The original exercise update request.
        :param response: The API response containing the updated exercise data.
        :raises AssertionError: If any field does not match.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Verifies that the actual exercise data matches the expected values.

    Args:
        actual (ExerciseSchema): The actual exercise data returned by the API.
        expected (ExerciseSchema): The expected exercise data used for comparison.

    Raises:
        AssertionError: If any field does not match the expected value.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema

):
    """
    Verifies that the exercise retrieval response matches the exercise creation response.

    Args:
        get_exercise_response (GetExerciseResponseSchema): The API response returned when requesting exercise data.
        create_exercise_response (CreateExerciseResponseSchema): The API response returned when the exercise was created.

    Raises:
        AssertionError: If any exercise data does not match the expected values.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

def assert_exercise_not_found_response (actual: InternalErrorResponseSchema

):
    """
    Checks that the correct error is returned when an exercise is not found on the server.

    Args:
        actual (InternalErrorResponseSchema): The actual API response.

    Raises:
        AssertionError: If the actual response does not match the expected
            "Exercise not found" error.
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)


def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Verifies that the response for retrieving a list of tasks matches the responses for creating them.

   Args:
       get_exercises_response: API response when requesting a list of tasks.
       create_exercise_responses: List of API responses when creating tasks.
    Raises:
          AssertionError: If the task data does not match.
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")
    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)




