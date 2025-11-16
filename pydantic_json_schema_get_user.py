from clients.private_http_builder import AuthenticationUserSchema # Import user authorization scheme - used to transfer login and password when creating a private client.
from clients.users.private_users_client import get_private_users_client # Import a function that returns a private client for working with protected endpoints (requiring authorization).
from clients.users.public_users_client import get_public_users_client # Import a function that returns a public client - used to register a new user (does not require authorization)

#- Schema import:
# - CreateUserRequestSchema — the body structure of the user creation request.
# - GetUserResponseSchema — the expected response structure when retrieving a user by ID:
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

# Get an instance of a public client, which can be used to save API methods without authorization.
public_users_client = get_public_users_client()

# Create a request object for creating a user, filling it with data (including a random email).
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

# Sending a request to create a user and save the response.
create_user_response = public_users_client.create_user(create_user_request)

# Authorization for a private client
authentication_user = AuthenticationUserSchema(

    # Create an object with the login and password of the new user -
    # this is needed for authorization in the private client

    email=create_user_request.email,
    password=create_user_request.password
)

# Get a private client already authorized as the created user. Now I can call protected API methods
private_users_client = get_private_users_client(authentication_user)

# Getting a user by ID
# Send a GET /users/{user_id} request using the private client. Get data about the created user.
get_user_response = private_users_client.get_user_api(create_user_response.user.id)

# Schema generation and validation
# Get the JSON schema from the GetUserResponseSchema model to use for validation
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Checking that the JSON response from the API matches the expected schema. If not, the test will fail.
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

# This script:
# - Creates a new user (getting user_id).
# - Logs in as that user.
# - Gets their user ID.
# - Checks that the response matches the expected structure.