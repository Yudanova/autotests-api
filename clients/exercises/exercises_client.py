from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, GetExerciseResponseSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExercisesClient(APIClient):
    """
    Client for interacting with /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Method for retrieving a list of exercises.

        :param query: Dictionary with courseId.
        :return: Server response as an httpx.Response object
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Method for retrieving an exercise.

        :param exercise_id: Exercise identifier.
        :return: Server response as an httpx.Response object
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Method for creating an exercise.

        :param request: Dictionary with title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Method for updating an exercise.

        :param exercise_id: Exercise identifier.
        :param request: Dictionary with title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Server response as an httpx.Response object
        """
        return self.patch(
            f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True)
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Method for deleting an exercise.

        :param exercise_id: Exercise identifier.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Function creates an instance of ExercisesClient with a preconfigured HTTP client.

    :return: A ready-to-use ExercisesClient instance.
    """
    return ExercisesClient(client=get_private_http_client(user))



# from typing import TypedDict
#
# from httpx import Response
#
# from clients.api_client import APIClient
# from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
#
# class Exercise(TypedDict):
#     """
#     Describes the structure of an exercise.
#     """
#     id: str
#     title: str
#     courseId: str
#     maxScore: int
#     minScore: int
#     orderIndex: int
#     description: str
#     estimatedTime: str
#
# class GetExerciseResponseDict(TypedDict):
#     """
#     Describes the structure of the response when retrieving an exercise.
#     """
#     exercise: Exercise
#
# class GetExercisesQueryDict(TypedDict):
#     """
#     Describes the structure of the request for retrieving a list of exercises.
#     """
#     courseId: str
#
# class GetExercisesResponseDict(TypedDict):
#     """
#     Describes the structure of the response when retrieving a list of exercises.
#     """
#     exercises: list[Exercise]
#
# class CreateExerciseRequestDict(TypedDict):
#     """
#     Describes the structure of the request for creating an exercise.
#     """
#     title: str
#     courseId: str
#     maxScore: int
#     minScore: int
#     orderIndex: int
#     description: str
#     estimatedTime: str
#
# class CreateExerciseResponseDict(TypedDict):
#     """
#     Describes the structure of the response when creating an exercise.
#     """
#     exercise: Exercise
#
# class UpdateExerciseRequestDict(TypedDict):
#     """
#     Describes the structure of the request for updating an exercise.
#     """
#     title: str | None
#     maxScore: int | None
#     minScore: int | None
#     orderIndex: int | None
#     description: str | None
#     estimatedTime: str | None
#
# class UpdateExerciseResponseDict(TypedDict):
#     """
#     Describes the structure of the response when updating an exercise.
#     """
#     exercise: Exercise
#
# class ExercisesClient(APIClient):
#     """
#     Client for interacting with /api/v1/exercises
#     """
#
#     def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
#         """
#         Method for retrieving a list of exercises.
#
#         :param query: Dictionary containing courseId.
#         :return: Server response as an httpx.Response object
#         """
#         return self.get("/api/v1/exercises", params=query)
#
#     def get_exercise_api(self, exercise_id: str) -> Response:
#         """
#         Method for retrieving an exercise.
#
#         :param exercise_id: Exercise identifier.
#         :return: Server response as an httpx.Response object
#         """
#         return self.get(f"/api/v1/exercises/{exercise_id}")
#
#     def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
#         """
#         Method for creating an exercise.
#
#         :param request: Dictionary containing title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
#         :return: Server response as an httpx.Response object
#         """
#         return self.post("/api/v1/exercises", json=request)
#
#     def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
#         """
#         Method for updating an exercise.
#
#         :param exercise_id: Exercise identifier.
#         :param request: Dictionary containing title, maxScore, minScore, orderIndex, description, estimatedTime.
#         :return: Server response as an httpx.Response object
#         """
#         return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)
#
#     def delete_exercise_api(self, exercise_id: str) -> Response:
#         """
#         Method for deleting an exercise.
#
#         :param exercise_id: Exercise identifier.
#         :return: Server response as an httpx.Response object
#         """
#         return self.delete(f"/api/v1/exercises/{exercise_id}")
#
#     def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
#         response = self.get_exercises_api(query)
#         return response.json()
#
#     def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
#         response = self.get_exercise_api(exercise_id)
#         return response.json()
#
#     def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
#         response = self.create_exercise_api(request)
#         return response.json()
#
#     def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
#         response = self.update_exercise_api(exercise_id, request)
#         return response.json()
#
# def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
#     """
#     Function creates an instance of ExercisesClient with a preconfigured HTTP client.
#
#     :return: A ready-to-use ExercisesClient instance.
#     """
#     return ExercisesClient(client=get_private_http_client(user))