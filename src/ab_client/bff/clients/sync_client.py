from __future__ import annotations

import json
from collections.abc import Generator
from typing import Any, Dict, Optional, Union

import httpx
from pydantic import BaseModel, TypeAdapter

from ..exceptions import HTTPException
from ..models import *


class SyncClient(BaseModel):
    model_config = {"validate_assignment": True}

    base_url: str = "/"
    verify: Union[bool, str] = True
    access_token: Optional[str] = None

    def get_access_token(self) -> Optional[str]:
        return self.access_token

    def set_access_token(self, value: str) -> None:
        self.access_token = value

    def login_auth_login_get(
        self,
        return_to: Optional[Union[str, None]] = None,
    ) -> Any:
        base_url = self.base_url
        path = f"/auth/login"

        headers = {
            "Accept": "application/json",
        }

        _token = self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {
            "return_to": return_to,
        }
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        with httpx.Client(base_url=base_url, verify=self.verify) as client:
            response = client.request(
                "get",
                httpx.URL(path),
                headers=headers,
                params=query_params,
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"login_auth_login_get failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return body

    def refresh_auth_refresh_get(
        self,
        return_to: Optional[Union[str, None]] = None,
        refresh_token: Optional[Union[str, None]] = None,
    ) -> OAuth2TokenExposed:
        base_url = self.base_url
        path = f"/auth/refresh"

        headers = {
            "Accept": "application/json",
        }

        _token = self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {
            "return_to": return_to,
        }
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        with httpx.Client(base_url=base_url, verify=self.verify) as client:
            response = client.request(
                "get",
                httpx.URL(path),
                headers=headers,
                params=query_params,
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"refresh_auth_refresh_get failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return TypeAdapter(OAuth2TokenExposed).validate_python(body)

    def callback_auth_callback_get(self) -> OAuth2TokenExposed:
        base_url = self.base_url
        path = f"/auth/callback"

        headers = {
            "Accept": "application/json",
        }

        _token = self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {}
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        with httpx.Client(base_url=base_url, verify=self.verify) as client:
            response = client.request(
                "get",
                httpx.URL(path),
                headers=headers,
                params=query_params,
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"callback_auth_callback_get failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return TypeAdapter(OAuth2TokenExposed).validate_python(body)

    def logout_auth_logout_get(
        self,
        return_to: Optional[Union[str, None]] = None,
    ) -> Any:
        base_url = self.base_url
        path = f"/auth/logout"

        headers = {
            "Accept": "application/json",
        }

        _token = self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {
            "return_to": return_to,
        }
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        with httpx.Client(base_url=base_url, verify=self.verify) as client:
            response = client.request(
                "get",
                httpx.URL(path),
                headers=headers,
                params=query_params,
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"logout_auth_logout_get failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return body

    def me_auth_me_get(
        self,
        authorization: Optional[Union[str, None]] = None,
        access_token: Optional[Union[str, None]] = None,
    ) -> IdentityContext:
        base_url = self.base_url
        path = f"/auth/me"

        headers = {
            "Accept": "application/json",
        }

        _token = self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {}
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        with httpx.Client(base_url=base_url, verify=self.verify) as client:
            response = client.request(
                "get",
                httpx.URL(path),
                headers=headers,
                params=query_params,
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"me_auth_me_get failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return TypeAdapter(IdentityContext).validate_python(body)
