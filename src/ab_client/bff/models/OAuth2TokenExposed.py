from typing import *

from pydantic import BaseModel, Field


class OAuth2TokenExposed(BaseModel):
    """
    OAuth2TokenExposed model
        OAuth2TokenExposed model
        An OAuth2 token model with secrets exposed as plain strings.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    access_token: str = Field(validation_alias="access_token")

    id_token: Optional[Union[str, None]] = Field(validation_alias="id_token", default=None)

    refresh_token: Optional[Union[str, None]] = Field(validation_alias="refresh_token", default=None)

    app_context: Optional[Union[Dict[str, str], None]] = Field(validation_alias="app_context", default=None)
