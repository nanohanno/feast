"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

* Copyright 2020 The Feast Authors
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     https://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
"""
import builtins
import collections.abc
import feast.types.Value_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Entity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEC_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def spec(self) -> global___EntitySpecV2:
        """User-specified specifications of this entity."""
    @property
    def meta(self) -> global___EntityMeta:
        """System-populated metadata for this entity."""
    def __init__(
        self,
        *,
        spec: global___EntitySpecV2 | None = ...,
        meta: global___EntityMeta | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["meta", b"meta", "spec", b"spec"]) -> None: ...

global___Entity = Entity

class EntitySpecV2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class TagsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    VALUE_TYPE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    JOIN_KEY_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the entity."""
    project: builtins.str
    """Name of Feast project that this feature table belongs to."""
    value_type: feast.types.Value_pb2.ValueType.Enum.ValueType
    """Type of the entity."""
    description: builtins.str
    """Description of the entity."""
    join_key: builtins.str
    """Join key for the entity (i.e. name of the column the entity maps to)."""
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """User defined metadata"""
    owner: builtins.str
    """Owner of the entity."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        project: builtins.str = ...,
        value_type: feast.types.Value_pb2.ValueType.Enum.ValueType = ...,
        description: builtins.str = ...,
        join_key: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        owner: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "join_key", b"join_key", "name", b"name", "owner", b"owner", "project", b"project", "tags", b"tags", "value_type", b"value_type"]) -> None: ...

global___EntitySpecV2 = EntitySpecV2

class EntityMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATED_TIMESTAMP_FIELD_NUMBER: builtins.int
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: builtins.int
    @property
    def created_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_updated_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        created_timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_updated_timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_timestamp", b"created_timestamp", "last_updated_timestamp", b"last_updated_timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_timestamp", b"created_timestamp", "last_updated_timestamp", b"last_updated_timestamp"]) -> None: ...

global___EntityMeta = EntityMeta

class EntityList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTITIES_FIELD_NUMBER: builtins.int
    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Entity]: ...
    def __init__(
        self,
        *,
        entities: collections.abc.Iterable[global___Entity] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entities", b"entities"]) -> None: ...

global___EntityList = EntityList
