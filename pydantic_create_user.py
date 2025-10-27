from pydantic import BaseModel, Field, EmailStr

# Structure
"""
   {
  "id": "string",
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
"""
# UserSchema implementation - user data model

class UserSchema(BaseModel):
    """
    Describes the structure of a user.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

# 2-nd Structure
"""
{
  "email": "user@example.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

"""

# CreateUserRequestSchema implementation - a request to create a user model


class CreateUserRequestSchema(BaseModel):
    """
    Describes the structure of a user creation request.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


# 3-d Structure
"""
{
  "user": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
  }
}
"""


#CreateUserResponseSchema implementation - response with data of the created user

class CreateUserResponseSchema(BaseModel):
    """
    Describes the structure of a user creation response.
    """
    user: UserSchema