# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.awslambda import MAXIMUM_MEMORY  # noqa: F401
from .validators.awslambda import MINIMUM_MEMORY  # noqa: F401
from .validators.awslambda import (
    validate_code,
    validate_image_config,
    validate_memory_size,
    validate_package_type,
    validate_variables_name,
)


class VersionWeight(AWSProperty):
    """
    `VersionWeight <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html>`__
    """

    props: PropsDictType = {
        "FunctionVersion": (str, True),
        "FunctionWeight": (double, True),
    }


class AliasRoutingConfiguration(AWSProperty):
    """
    `AliasRoutingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdditionalVersionWeights": ([VersionWeight], True),
    }


class ProvisionedConcurrencyConfiguration(AWSProperty):
    """
    `ProvisionedConcurrencyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html>`__
    """

    props: PropsDictType = {
        "ProvisionedConcurrentExecutions": (integer, True),
    }


class Alias(AWSObject):
    """
    `Alias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html>`__
    """

    resource_type = "AWS::Lambda::Alias"

    props: PropsDictType = {
        "Description": (str, False),
        "FunctionName": (str, True),
        "FunctionVersion": (str, True),
        "Name": (str, True),
        "ProvisionedConcurrencyConfig": (ProvisionedConcurrencyConfiguration, False),
        "RoutingConfig": (AliasRoutingConfiguration, False),
    }


class AllowedPublishers(AWSProperty):
    """
    `AllowedPublishers <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html>`__
    """

    props: PropsDictType = {
        "SigningProfileVersionArns": ([str], True),
    }


class CodeSigningPolicies(AWSProperty):
    """
    `CodeSigningPolicies <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html>`__
    """

    props: PropsDictType = {
        "UntrustedArtifactOnDeployment": (str, True),
    }


class CodeSigningConfig(AWSObject):
    """
    `CodeSigningConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html>`__
    """

    resource_type = "AWS::Lambda::CodeSigningConfig"

    props: PropsDictType = {
        "AllowedPublishers": (AllowedPublishers, True),
        "CodeSigningPolicies": (CodeSigningPolicies, False),
        "Description": (str, False),
    }


class OnFailure(AWSProperty):
    """
    `OnFailure <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html>`__
    """

    props: PropsDictType = {
        "Destination": (str, True),
    }


class OnSuccess(AWSProperty):
    """
    `OnSuccess <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html>`__
    """

    props: PropsDictType = {
        "Destination": (str, True),
    }


class DestinationConfig(AWSProperty):
    """
    `DestinationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html>`__
    """

    props: PropsDictType = {
        "OnFailure": (OnFailure, False),
        "OnSuccess": (OnSuccess, False),
    }


class EventInvokeConfig(AWSObject):
    """
    `EventInvokeConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html>`__
    """

    resource_type = "AWS::Lambda::EventInvokeConfig"

    props: PropsDictType = {
        "DestinationConfig": (DestinationConfig, False),
        "FunctionName": (str, True),
        "MaximumEventAgeInSeconds": (integer, False),
        "MaximumRetryAttempts": (integer, False),
        "Qualifier": (str, True),
    }


class AmazonManagedKafkaEventSourceConfig(AWSProperty):
    """
    `AmazonManagedKafkaEventSourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html>`__
    """

    props: PropsDictType = {
        "ConsumerGroupId": (str, False),
    }


class Filter(AWSProperty):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html>`__
    """

    props: PropsDictType = {
        "Pattern": (str, False),
    }


class FilterCriteria(AWSProperty):
    """
    `FilterCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html>`__
    """

    props: PropsDictType = {
        "Filters": ([Filter], False),
    }


class Endpoints(AWSProperty):
    """
    `Endpoints <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html>`__
    """

    props: PropsDictType = {
        "KafkaBootstrapServers": ([str], False),
    }


class SelfManagedEventSource(AWSProperty):
    """
    `SelfManagedEventSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html>`__
    """

    props: PropsDictType = {
        "Endpoints": (Endpoints, False),
    }


class SelfManagedKafkaEventSourceConfig(AWSProperty):
    """
    `SelfManagedKafkaEventSourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html>`__
    """

    props: PropsDictType = {
        "ConsumerGroupId": (str, False),
    }


class SourceAccessConfiguration(AWSProperty):
    """
    `SourceAccessConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
        "URI": (str, False),
    }


class EventSourceMapping(AWSObject):
    """
    `EventSourceMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html>`__
    """

    resource_type = "AWS::Lambda::EventSourceMapping"

    props: PropsDictType = {
        "AmazonManagedKafkaEventSourceConfig": (
            AmazonManagedKafkaEventSourceConfig,
            False,
        ),
        "BatchSize": (integer, False),
        "BisectBatchOnFunctionError": (boolean, False),
        "DestinationConfig": (DestinationConfig, False),
        "Enabled": (boolean, False),
        "EventSourceArn": (str, False),
        "FilterCriteria": (FilterCriteria, False),
        "FunctionName": (str, True),
        "FunctionResponseTypes": ([str], False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "MaximumRecordAgeInSeconds": (integer, False),
        "MaximumRetryAttempts": (integer, False),
        "ParallelizationFactor": (integer, False),
        "Queues": ([str], False),
        "SelfManagedEventSource": (SelfManagedEventSource, False),
        "SelfManagedKafkaEventSourceConfig": (SelfManagedKafkaEventSourceConfig, False),
        "SourceAccessConfigurations": ([SourceAccessConfiguration], False),
        "StartingPosition": (str, False),
        "StartingPositionTimestamp": (double, False),
        "Topics": ([str], False),
        "TumblingWindowInSeconds": (integer, False),
    }


class Code(AWSProperty):
    """
    `Code <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html>`__
    """

    props: PropsDictType = {
        "ImageUri": (str, False),
        "S3Bucket": (str, False),
        "S3Key": (str, False),
        "S3ObjectVersion": (str, False),
        "ZipFile": (str, False),
    }

    def validate(self):
        validate_code(self)


class DeadLetterConfig(AWSProperty):
    """
    `DeadLetterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html>`__
    """

    props: PropsDictType = {
        "TargetArn": (str, False),
    }


class Environment(AWSProperty):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html>`__
    """

    props: PropsDictType = {
        "Variables": (validate_variables_name, False),
    }


class EphemeralStorage(AWSProperty):
    """
    `EphemeralStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-ephemeralstorage.html>`__
    """

    props: PropsDictType = {
        "Size": (integer, True),
    }


class FileSystemConfig(AWSProperty):
    """
    `FileSystemConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "LocalMountPath": (str, True),
    }


class ImageConfig(AWSProperty):
    """
    `ImageConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html>`__
    """

    props: PropsDictType = {
        "Command": ([str], False),
        "EntryPoint": ([str], False),
        "WorkingDirectory": (str, False),
    }

    def validate(self):
        validate_image_config(self)


class SnapStart(AWSProperty):
    """
    `SnapStart <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html>`__
    """

    props: PropsDictType = {
        "ApplyOn": (str, True),
    }


class TracingConfig(AWSProperty):
    """
    `TracingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html>`__
    """

    props: PropsDictType = {
        "Mode": (str, False),
    }


class VPCConfig(AWSProperty):
    """
    `VPCConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
    }


class Function(AWSObject):
    """
    `Function <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html>`__
    """

    resource_type = "AWS::Lambda::Function"

    props: PropsDictType = {
        "Architectures": ([str], False),
        "Code": (Code, True),
        "CodeSigningConfigArn": (str, False),
        "DeadLetterConfig": (DeadLetterConfig, False),
        "Description": (str, False),
        "Environment": (Environment, False),
        "EphemeralStorage": (EphemeralStorage, False),
        "FileSystemConfigs": ([FileSystemConfig], False),
        "FunctionName": (str, False),
        "Handler": (str, False),
        "ImageConfig": (ImageConfig, False),
        "KmsKeyArn": (str, False),
        "Layers": ([str], False),
        "MemorySize": (validate_memory_size, False),
        "PackageType": (validate_package_type, False),
        "ReservedConcurrentExecutions": (integer, False),
        "Role": (str, True),
        "Runtime": (str, False),
        "SnapStart": (SnapStart, False),
        "Tags": (Tags, False),
        "Timeout": (integer, False),
        "TracingConfig": (TracingConfig, False),
        "VpcConfig": (VPCConfig, False),
    }


class Content(AWSProperty):
    """
    `Content <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html>`__
    """

    props: PropsDictType = {
        "S3Bucket": (str, True),
        "S3Key": (str, True),
        "S3ObjectVersion": (str, False),
    }


class LayerVersion(AWSObject):
    """
    `LayerVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html>`__
    """

    resource_type = "AWS::Lambda::LayerVersion"

    props: PropsDictType = {
        "CompatibleArchitectures": ([str], False),
        "CompatibleRuntimes": ([str], False),
        "Content": (Content, True),
        "Description": (str, False),
        "LayerName": (str, False),
        "LicenseInfo": (str, False),
    }


class LayerVersionPermission(AWSObject):
    """
    `LayerVersionPermission <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html>`__
    """

    resource_type = "AWS::Lambda::LayerVersionPermission"

    props: PropsDictType = {
        "Action": (str, True),
        "LayerVersionArn": (str, True),
        "OrganizationId": (str, False),
        "Principal": (str, True),
    }


class Permission(AWSObject):
    """
    `Permission <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
    """

    resource_type = "AWS::Lambda::Permission"

    props: PropsDictType = {
        "Action": (str, True),
        "EventSourceToken": (str, False),
        "FunctionName": (str, True),
        "FunctionUrlAuthType": (str, False),
        "Principal": (str, True),
        "PrincipalOrgID": (str, False),
        "SourceAccount": (str, False),
        "SourceArn": (str, False),
    }


class Cors(AWSProperty):
    """
    `Cors <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html>`__
    """

    props: PropsDictType = {
        "AllowCredentials": (boolean, False),
        "AllowHeaders": ([str], False),
        "AllowMethods": ([str], False),
        "AllowOrigins": ([str], False),
        "ExposeHeaders": ([str], False),
        "MaxAge": (integer, False),
    }


class Url(AWSObject):
    """
    `Url <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html>`__
    """

    resource_type = "AWS::Lambda::Url"

    props: PropsDictType = {
        "AuthType": (str, True),
        "Cors": (Cors, False),
        "InvokeMode": (str, False),
        "Qualifier": (str, False),
        "TargetFunctionArn": (str, True),
    }


class Version(AWSObject):
    """
    `Version <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html>`__
    """

    resource_type = "AWS::Lambda::Version"

    props: PropsDictType = {
        "CodeSha256": (str, False),
        "Description": (str, False),
        "FunctionName": (str, True),
        "ProvisionedConcurrencyConfig": (ProvisionedConcurrencyConfiguration, False),
    }


class SnapStartResponse(AWSProperty):
    """
    `SnapStartResponse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstartresponse.html>`__
    """

    props: PropsDictType = {
        "ApplyOn": (str, False),
        "OptimizationStatus": (str, False),
    }
