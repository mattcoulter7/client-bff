from typing import *

from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User model
        User model
        User model.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    is_active: Optional[Union[bool, None]] = Field(validation_alias="is_active", default=True)

    updated_at: str = Field(validation_alias="updated_at")

    created_at: str = Field(validation_alias="created_at")

    id: Optional[Union[str, None]] = Field(validation_alias="id", default=None)

    oidc_sub: str = Field(validation_alias="oidc_sub")

    oidc_iss: str = Field(validation_alias="oidc_iss")

    email: Optional[Union[str, None]] = Field(validation_alias="email", default=None)

    display_name: Optional[Union[str, None]] = Field(validation_alias="display_name", default=None)

    preferred_username: Optional[Union[str, None]] = Field(validation_alias="preferred_username", default=None)

    last_seen: Union[str, None] = Field(validation_alias="last_seen")
