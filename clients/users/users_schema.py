from pydantic import BaseModel, Field, EmailStr, ConfigDict


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

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


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

    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


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
