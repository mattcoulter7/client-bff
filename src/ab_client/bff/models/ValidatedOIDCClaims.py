from typing import *

from pydantic import BaseModel, Field


class ValidatedOIDCClaims(BaseModel):
    """
    ValidatedOIDCClaims model
        ValidatedOIDCClaims model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    iss: str = Field(validation_alias="iss")

    sub: str = Field(validation_alias="sub")

    aud: Union[str, List[str]] = Field(validation_alias="aud")

    exp: int = Field(validation_alias="exp")

    iat: int = Field(validation_alias="iat")

    auth_time: int = Field(validation_alias="auth_time")

    acr: str = Field(validation_alias="acr")

    email: Optional[Union[str, None]] = Field(validation_alias="email", default=None)

    email_verified: Optional[Union[bool, None]] = Field(validation_alias="email_verified", default=None)

    name: Optional[Union[str, None]] = Field(validation_alias="name", default=None)

    given_name: Optional[Union[str, None]] = Field(validation_alias="given_name", default=None)

    preferred_username: Optional[Union[str, None]] = Field(validation_alias="preferred_username", default=None)

    nickname: Optional[Union[str, None]] = Field(validation_alias="nickname", default=None)

    groups: Optional[Union[List[str], None]] = Field(validation_alias="groups", default=None)
