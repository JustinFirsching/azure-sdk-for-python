# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._check_name_availability_without_location_operations import build_execute_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CheckNameAvailabilityWithoutLocationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.rdbms.mysql_flexibleservers.aio.MySQLManagementClient`'s
        :attr:`check_name_availability_without_location` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def execute(
        self,
        name_availability_request: _models.NameAvailabilityRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailability:
        """Check the availability of name for server.

        :param name_availability_request: The required parameters for checking if server name is
         available. Required.
        :type name_availability_request:
         ~azure.mgmt.rdbms.mysql_flexibleservers.models.NameAvailabilityRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailability or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.NameAvailability
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def execute(
        self, name_availability_request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NameAvailability:
        """Check the availability of name for server.

        :param name_availability_request: The required parameters for checking if server name is
         available. Required.
        :type name_availability_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailability or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.NameAvailability
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def execute(
        self, name_availability_request: Union[_models.NameAvailabilityRequest, IO], **kwargs: Any
    ) -> _models.NameAvailability:
        """Check the availability of name for server.

        :param name_availability_request: The required parameters for checking if server name is
         available. Is either a model type or a IO type. Required.
        :type name_availability_request:
         ~azure.mgmt.rdbms.mysql_flexibleservers.models.NameAvailabilityRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailability or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.NameAvailability
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2021-12-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.NameAvailability]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(name_availability_request, (IO, bytes)):
            _content = name_availability_request
        else:
            _json = self._serialize.body(name_availability_request, "NameAvailabilityRequest")

        request = build_execute_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.execute.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("NameAvailability", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    execute.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.DBforMySQL/checkNameAvailability"}  # type: ignore
