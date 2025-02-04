# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-apimanagement
# USAGE
    python api_management_create_api_new_version_using_existing_api.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApiManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.api.begin_create_or_update(
        resource_group_name="rg1",
        service_name="apimService1",
        api_id="echoapiv3",
        parameters={
            "properties": {
                "apiVersion": "v4",
                "apiVersionSetId": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/apiVersionSets/aa9c59e6-c0cd-4258-9356-9ca7d2f0b458",
                "description": "Create Echo API into a new Version using Existing Version Set and Copy all Operations.",
                "displayName": "Echo API2",
                "isCurrent": True,
                "path": "echo2",
                "protocols": ["http", "https"],
                "serviceUrl": "http://echoapi.cloudapp.net/api",
                "sourceApiId": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/apis/echoPath",
                "subscriptionRequired": True,
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/apimanagement/resource-manager/Microsoft.ApiManagement/stable/2021-08-01/examples/ApiManagementCreateApiNewVersionUsingExistingApi.json
if __name__ == "__main__":
    main()
