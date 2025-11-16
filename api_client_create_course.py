
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema


# Initialize the public users client (no authentication required)
public_users_client = get_public_users_client()

# Create a new user using a randomly generated email and static credentials
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)

# Prepare authentication credentials using the newly created user's data
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Initialize authenticated clients for file and course operations
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Upload a file to be used as a course preview image
create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")

create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Create a new course using the uploaded file and user ID
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)






















# from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
# from clients.files.files_client import get_files_client
#
# # Instead of CreateFileRequestDict import CreateFileRequestSchema
# from clients.files.files_schema import CreateFileRequestSchema
# from clients.private_http_builder import AuthenticationUserSchema
# from clients.users.public_users_client import get_public_users_client
# from clients.users.users_schema import CreateUserRequestSchema
# from tools.fakers import fake
#
# public_users_client = get_public_users_client()
#
# create_user_request = CreateUserRequestSchema(
#     email=fake.email(),
#     password="string",
#     last_name="string",
#     first_name="string",
#     middle_name="string"
# )
# create_user_response = public_users_client.create_user(create_user_request)
#
# authentication_user = AuthenticationUserSchema(
#     email=create_user_request.email,
#     password=create_user_request.password
# )
# files_client = get_files_client(authentication_user)
# courses_client = get_courses_client(authentication_user)
#
# # Instead of CreateFileRequestDict using  CreateFileRequestSchema
# create_file_request = CreateFileRequestSchema(
#     filename="image.png",
#     directory="courses",
#     upload_file="./testdata/files/image.png"
# )
# create_file_response = files_client.create_file(create_file_request)
# print('Create file data:', create_file_response)
#
# create_course_request = CreateCourseRequestDict(
#     title="Python",
#     maxScore=100,
#     minScore=10,
#     description="Python API course",
#     estimatedTime="2 weeks",
#     previewFileId=create_file_response.file.id,  #  Using atributes instead of keys
#     createdByUserId=create_user_response.user.id  # Using atributes instead of keys
# )
# create_course_response = courses_client.create_course(create_course_request)
# print('Create course data:', create_course_response)
#





















# from clients.courses.courses_client import get_courses_client
# from clients.courses.courses_schema import CreateCourseRequestSchema
# from clients.files.files_client import get_files_client
# from clients.files.files_schema import CreateFileRequestSchema
# from clients.private_http_builder import AuthenticationUserSchema
#
# from clients.users.public_users_client import get_public_users_client
# from clients.users.users_schema import CreateUserRequestSchema
# from tools.fakers import fake
#
# # Create user
# public_users_client = get_public_users_client()
# create_user_request = CreateUserRequestSchema(
#     email=fake.email(),
#     password="string",
#     last_name="string",
#     first_name="string",
#     middle_name="string"
# )
# create_user_response = public_users_client.create_user(create_user_request)
#
# # Authentication
# authentication_user = AuthenticationUserSchema(
#     email=create_user_request.email,
#     password=create_user_request.password
# )
#
# # Initializing clients
# files_client = get_files_client(authentication_user)
# courses_client = get_courses_client(authentication_user)
#
# # Loading file
# create_file_request = CreateFileRequestSchema(
#     filename="image.png",
#     directory="courses",
#     upload_file="./testdata/files/image.png"
# )
# create_file_response = files_client.create_file(create_file_request)
# print('Create file data:', create_file_response)
#
# # Create new course
# create_course_request = CreateCourseRequestSchema(
#     title="Python",
#     max_score=100,
#     min_score=10,
#     description="Python API course",
#     estimated_time="2 weeks",
#     preview_file_id=create_file_response.file.id,
#     created_by_user_id=create_user_response.user.id
# )
# create_course_response = courses_client.create_course(create_course_request)
# print('Create course data:', create_course_response)