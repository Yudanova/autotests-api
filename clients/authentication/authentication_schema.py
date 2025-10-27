from pydantic import BaseModel, Field



# Added the Schema suffix instead of Dict
class TokenSchema(BaseModel): # # Inherit from BaseModel instead of TypedDict
    """
    Description of the structure of authentication tokens.
    """
    token_type: str = Field(alias = "tokenType") # Using alias
    access_token: str = Field(alias = "accessToken")
    refresh_token: str = Field(alias = "refreshToken")


# Added the Schema suffix instead of Dict
class LoginRequestSchema(BaseModel):  #Inherit from BaseModel instead of TypedDict
    """
    Description of the authentication request structure.
    """
    email: str
    password: str

# Added the Schema suffix instead of Dict
class LoginResponseSchema(BaseModel):
    """
    Description of the authentication response structure.
    """
    token: TokenSchema

# Added the Schema suffix instead of Dict
class RefreshRequestSchema(BaseModel):
    """
    Description of the request structure for updating the token.
    """
    refresh_token: str = Field(alias="refreshToken")  #Using alias