
from clients.courses.courses_schema import CourseSchema, UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Verifies that the actual course data matches the expected values.

    :param actual: The actual course data.
    :param expected: The expected course data.
    :raises AssertionError: If any field does not match.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    # Validate nested entities
    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Verifies that the response for retrieving the list of courses
    matches the responses returned during course creation.

    :param get_courses_response: The API response for the course list request.
    :param create_course_responses: A list of API responses from course creation.
    :raises AssertionError: If any course data does not match.
    """
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)

def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Verifies that the course update response matches the data from the request.

    :param request: The original course update request.
    :param response: The API response containing the updated course data.
    :raises AssertionError: If any field does not match.
    """
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")



