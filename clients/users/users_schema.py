from pydantic import BaseModel, Field, EmailStr, ConfigDict
# Import the pre-created instance of the Fake class
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Description of the user structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Description of the request structure for creating a user.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Added random email generation
    email: EmailStr = Field(default_factory=fake.email)
    # Added random password generation
    password: str = Field(default_factory=fake.password)
    # Added random last name generation
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    # Added random first name generation
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    # Added random middle name generation
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)

"""
default_factory automatically fills all fields with random values. 
There is still an option to specify a particular value, manually:
create_user_request = CreateUserRequestSchema(email="custom@example.com")
"""

    # email: EmailStr
    # password: str
    # last_name: str = Field(alias="lastName")
    # first_name: str = Field(alias="firstName")
    # middle_name: str = Field(alias="middleName")



class CreateUserResponseSchema(BaseModel):
    """
    Description of the response structure for user creation.

    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Description of the request structure for updating a user.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Added random email generation
    email: EmailStr | None = Field(default_factory=fake.email)
    # Added random last name generation
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    # Added random first name generation
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    # Added random middle name generation
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)
"""
All fields in UpdateUserRequestSchema are now optional (None is allowed), so you can update just the fields you need.
Example:
update_user_request = UpdateUserRequestSchema(first_name="Alex")

In this case, only first_name is set manually; the rest will be filled with random values.
"""
    # email: EmailStr | None
    # last_name: str | None = Field(alias="lastName")
    # first_name: str | None = Field(alias="firstName")
    # middle_name: str | None = Field(alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    """
    Description of the response structure for user update.
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Description of the request structure for retrieving a user.
    """
    user: UserSchema
