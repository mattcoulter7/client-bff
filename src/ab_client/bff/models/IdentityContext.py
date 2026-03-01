from typing import *

from pydantic import BaseModel, Field

from .User import User
from .ValidatedOIDCClaims import ValidatedOIDCClaims


class IdentityContext(BaseModel):
    """
    IdentityContext model
        Per-request identity context resolved from the bearer token.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    token: str = Field(validation_alias="token")

    claims: ValidatedOIDCClaims = Field(validation_alias="claims")

    user: User = Field(validation_alias="user")
