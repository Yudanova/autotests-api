from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Initialize the PublicUsersClient
public_users_client = get_public_users_client()

# Prepare the request to create a new user
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
# Send a POST request to create the user
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Prepare user credentials for authentication
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Initialize the PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Send a GET request to retrieve user data
get_user_response = private_users_client.get_user_api(create_user_response_data['user']['id'])
get_user_response_data = get_user_response.json()
print('Get user data:', get_user_response_data)