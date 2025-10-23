from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetCoursesQueryDict(TypedDict):
    """
    Describes the structure of the request for retrieving a list of courses.
    """

    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Describes the structure of the request for creating a course.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    """
    Describes the structure of the request for updating a course.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Client for interacting with /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Method for retrieving a list of courses.

        :param query: Dictionary containing userId.
        :return: Server response as an httpx.Response object
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Method for retrieving a course by ID.

        :param course_id: Course identifier.
        :return: Server response as an httpx.Response object
        """

        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Method for creating a course.

        :param request: Dictionary containing title, maxScore, minScore, description,
        estimatedTime, previewFileId, createdByUserId.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Method for updating a course.

        :param course_id: Course identifier.
        :param request: Dictionary containing title, maxScore, minScore, description, estimatedTime.
        :return: Server response as an httpx.Response object
        """

        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method for deleting a course.

        :param course_id: Course identifier.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/courses/{course_id}")
