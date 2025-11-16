from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
# Added import of the validate_json_schema function
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
#create_user_response_json = create_user_response.json() - checking error message
create_user_response_schema = CreateUserResponseSchema.model_json_schema() # Get the JSON schema from the response model

#create_user_response_json ['user']['email'] = "Hello!" # to trigger validation error

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

#validate_json_schema(instance=create_user_response_json, schema=create_user_response_schema)# Validate that the JSON response from the API matches the expected JSON schema

{
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "email": {"type": "string", "format": "email"},
    "age": {"type": "integer"}
  },
  "required": ["id", "email"]
}
{
  "type": "object",
  "properties": {
    "username": {
    "type": "string",
    "minLength": 5,
    "maxLength": 15
    }
  },
  "required": ["username"]
}
