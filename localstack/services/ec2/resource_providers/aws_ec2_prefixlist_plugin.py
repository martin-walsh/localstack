from typing import Optional, Type

from localstack.services.cloudformation.resource_provider import (
    CloudFormationResourceProviderPlugin,
    ResourceProvider,
)


class EC2PrefixListProviderPlugin(CloudFormationResourceProviderPlugin):
    name = "AWS::EC2::PrefixList"

    def __init__(self):
        self.factory: Optional[Type[ResourceProvider]] = None

    def load(self):
        from localstack.services.ec2.resource_providers.aws_ec2_prefixlist import (
            EC2PrefixListProvider,
        )

        self.factory = EC2PrefixListProvider
