from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response
from tools.assertions.schema import validate_json_schema




@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_course: CourseFixture
    ):
        # Build the query parameters by passing the user_id
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)

        # Send a GET request to retrieve the list of courses
        response = courses_client.get_courses_api(query)

        # Deserialize the JSON response into a Pydantic model
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        # Verify that the response status code is 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Verify that the list of courses matches the previously created courses
        assert_get_courses_response(response_data, [function_course.response])

        # Validate that the JSON response matches the schema
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        # Prepare data for the update
        request = UpdateCourseRequestSchema()

        # Send the course update request
        response = courses_client.update_course_api(function_course.response.course.id, request)

        # Convert the JSON response into a schema object
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Verify the response status code
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Verify that the response data matches the request
        assert_update_course_response(request, response_data)

        # Validate the JSON schema of the response
        validate_json_schema(response.json(), response_data.model_json_schema())

