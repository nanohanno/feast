"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Copyright 2020 The Feast Authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class FileFormat(google.protobuf.message.Message):
    """Defines the file format encoding the features/entity data in files"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ParquetFormat(google.protobuf.message.Message):
        """Defines options for the Parquet data format"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    class DeltaFormat(google.protobuf.message.Message):
        """Defines options for delta data format"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    PARQUET_FORMAT_FIELD_NUMBER: builtins.int
    DELTA_FORMAT_FIELD_NUMBER: builtins.int
    @property
    def parquet_format(self) -> global___FileFormat.ParquetFormat: ...
    @property
    def delta_format(self) -> global___FileFormat.DeltaFormat: ...
    def __init__(
        self,
        *,
        parquet_format: global___FileFormat.ParquetFormat | None = ...,
        delta_format: global___FileFormat.DeltaFormat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delta_format", b"delta_format", "format", b"format", "parquet_format", b"parquet_format"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delta_format", b"delta_format", "format", b"format", "parquet_format", b"parquet_format"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["format", b"format"]) -> typing_extensions.Literal["parquet_format", "delta_format"] | None: ...

global___FileFormat = FileFormat

class StreamFormat(google.protobuf.message.Message):
    """Defines the data format encoding features/entity data in data streams"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ProtoFormat(google.protobuf.message.Message):
        """Defines options for the protobuf data format"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CLASS_PATH_FIELD_NUMBER: builtins.int
        class_path: builtins.str
        """Classpath to the generated Java Protobuf class that can be used to decode
        Feature data from the obtained stream message
        """
        def __init__(
            self,
            *,
            class_path: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["class_path", b"class_path"]) -> None: ...

    class AvroFormat(google.protobuf.message.Message):
        """Defines options for the avro data format"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SCHEMA_JSON_FIELD_NUMBER: builtins.int
        schema_json: builtins.str
        """Optional if used in a File DataSource as schema is embedded in avro file.
        Specifies the schema of the Avro message as JSON string.
        """
        def __init__(
            self,
            *,
            schema_json: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["schema_json", b"schema_json"]) -> None: ...

    class JsonFormat(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SCHEMA_JSON_FIELD_NUMBER: builtins.int
        schema_json: builtins.str
        def __init__(
            self,
            *,
            schema_json: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["schema_json", b"schema_json"]) -> None: ...

    AVRO_FORMAT_FIELD_NUMBER: builtins.int
    PROTO_FORMAT_FIELD_NUMBER: builtins.int
    JSON_FORMAT_FIELD_NUMBER: builtins.int
    @property
    def avro_format(self) -> global___StreamFormat.AvroFormat: ...
    @property
    def proto_format(self) -> global___StreamFormat.ProtoFormat: ...
    @property
    def json_format(self) -> global___StreamFormat.JsonFormat: ...
    def __init__(
        self,
        *,
        avro_format: global___StreamFormat.AvroFormat | None = ...,
        proto_format: global___StreamFormat.ProtoFormat | None = ...,
        json_format: global___StreamFormat.JsonFormat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["avro_format", b"avro_format", "format", b"format", "json_format", b"json_format", "proto_format", b"proto_format"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["avro_format", b"avro_format", "format", b"format", "json_format", b"json_format", "proto_format", b"proto_format"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["format", b"format"]) -> typing_extensions.Literal["avro_format", "proto_format", "json_format"] | None: ...

global___StreamFormat = StreamFormat