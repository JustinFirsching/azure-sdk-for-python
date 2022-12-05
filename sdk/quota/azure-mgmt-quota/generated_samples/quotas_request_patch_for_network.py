# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.quota import AzureQuotaExtensionAPI

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-quota
# USAGE
    python quotas_request_patch_for_network.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureQuotaExtensionAPI(
        credential=DefaultAzureCredential(),
    )

    response = client.quota.begin_update(
        resource_name="MinPublicIpInterNetworkPrefixLength",
        scope="subscriptions/D7EC67B3-7657-4966-BFFC-41EFD36BAAB3/providers/Microsoft.Network/locations/eastus",
        create_quota_request={
            "properties": {
                "limit": {"limitObjectType": "LimitValue", "value": 10},
                "name": {"value": "MinPublicIpInterNetworkPrefixLength"},
                "resourceType": "MinPublicIpInterNetworkPrefixLength",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/quota/resource-manager/Microsoft.Quota/preview/2021-03-15-preview/examples/patchNetworkOneSkuQuotaRequest.json
if __name__ == "__main__":
    main()
