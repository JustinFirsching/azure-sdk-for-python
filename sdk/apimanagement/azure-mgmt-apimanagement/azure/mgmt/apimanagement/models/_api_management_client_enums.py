# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessIdName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessIdName."""

    ACCESS = "access"
    GIT_ACCESS = "gitAccess"


class AccessType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of access to be used for the storage account."""

    #: Use access key.
    ACCESS_KEY = "AccessKey"
    #: Use system assigned managed identity.
    SYSTEM_ASSIGNED_MANAGED_IDENTITY = "SystemAssignedManagedIdentity"
    #: Use user assigned managed identity.
    USER_ASSIGNED_MANAGED_IDENTITY = "UserAssignedManagedIdentity"


class AlwaysLog(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies for what type of messages sampling settings should not apply."""

    #: Always log all erroneous request regardless of sampling settings.
    ALL_ERRORS = "allErrors"


class ApiManagementSkuCapacityScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scale type applicable to the sku."""

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    NONE = "None"


class ApiManagementSkuRestrictionsReasonCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason for restriction."""

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"


class ApiManagementSkuRestrictionsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of restrictions."""

    LOCATION = "Location"
    ZONE = "Zone"


class ApimIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes
    both an implicitly created identity and a set of user assigned identities. The type 'None' will
    remove any identities from the service.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class ApiType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of API."""

    HTTP = "http"
    SOAP = "soap"
    WEBSOCKET = "websocket"
    GRAPHQL = "graphql"


class ApiVersionSetContractDetailsVersioningScheme(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An value that determines where the API Version identifier will be located in a HTTP request."""

    SEGMENT = "Segment"
    QUERY = "Query"
    HEADER = "Header"


class AppType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AppType."""

    #: User create request was sent by legacy developer portal.
    PORTAL = "portal"
    #: User create request was sent by new developer portal.
    DEVELOPER_PORTAL = "developerPortal"


class AsyncOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of an async operation."""

    STARTED = "Started"
    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class AuthorizationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AuthorizationMethod."""

    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class BackendProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backend communication protocol."""

    #: The Backend is a RESTful service.
    HTTP = "http"
    #: The Backend is a SOAP service.
    SOAP = "soap"


class BearerTokenSendingMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BearerTokenSendingMethod."""

    AUTHORIZATION_HEADER = "authorizationHeader"
    QUERY = "query"


class BearerTokenSendingMethods(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Form of an authorization grant, which the client uses to request the access token."""

    #: Access token will be transmitted in the Authorization header using Bearer schema
    AUTHORIZATION_HEADER = "authorizationHeader"
    #: Access token will be transmitted as query parameters.
    QUERY = "query"


class CertificateConfigurationStoreName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The System.Security.Cryptography.x509certificates.StoreName certificate store location. Only
    Root and CertificateAuthority are valid locations.
    """

    CERTIFICATE_AUTHORITY = "CertificateAuthority"
    ROOT = "Root"


class CertificateSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Certificate Source."""

    MANAGED = "Managed"
    KEY_VAULT = "KeyVault"
    CUSTOM = "Custom"
    BUILT_IN = "BuiltIn"


class CertificateStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Certificate Status."""

    COMPLETED = "Completed"
    FAILED = "Failed"
    IN_PROGRESS = "InProgress"


class ClientAuthenticationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ClientAuthenticationMethod."""

    #: Basic Client Authentication method.
    BASIC = "Basic"
    #: Body based Authentication method.
    BODY = "Body"


class ConfigurationIdName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ConfigurationIdName."""

    CONFIGURATION = "configuration"


class Confirmation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the type of confirmation e-mail that will be sent to the newly created user."""

    #: Send an e-mail to the user confirming they have successfully signed up.
    SIGNUP = "signup"
    #: Send an e-mail inviting the user to sign-up and complete registration.
    INVITE = "invite"


class ConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The connection status."""

    UNKNOWN = "Unknown"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    DEGRADED = "Degraded"


class ConnectivityCheckProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The request's protocol. Specific protocol configuration can be available based on this
    selection. The specified destination address must be coherent with this value.
    """

    TCP = "TCP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"


class ConnectivityStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource Connectivity Status Type identifier."""

    INITIALIZING = "initializing"
    SUCCESS = "success"
    FAILURE = "failure"


class ContentFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Format of the Content in which the API is getting imported."""

    #: The contents are inline and Content type is a WADL document.
    WADL_XML = "wadl-xml"
    #: The WADL document is hosted on a publicly accessible internet address.
    WADL_LINK_JSON = "wadl-link-json"
    #: The contents are inline and Content Type is a OpenAPI 2.0 JSON Document.
    SWAGGER_JSON = "swagger-json"
    #: The OpenAPI 2.0 JSON document is hosted on a publicly accessible internet address.
    SWAGGER_LINK_JSON = "swagger-link-json"
    #: The contents are inline and the document is a WSDL/Soap document.
    WSDL = "wsdl"
    #: The WSDL document is hosted on a publicly accessible internet address.
    WSDL_LINK = "wsdl-link"
    #: The contents are inline and Content Type is a OpenAPI 3.0 YAML Document.
    OPENAPI = "openapi"
    #: The contents are inline and Content Type is a OpenAPI 3.0 JSON Document.
    OPENAPI_JSON = "openapi+json"
    #: The OpenAPI 3.0 YAML document is hosted on a publicly accessible internet address.
    OPENAPI_LINK = "openapi-link"
    #: The OpenAPI 3.0 JSON document is hosted on a publicly accessible internet address.
    OPENAPI_JSON_LINK = "openapi+json-link"
    #: The GraphQL API endpoint hosted on a publicly accessible internet address.
    GRAPHQL_LINK = "graphql-link"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DataMaskingMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data masking mode."""

    #: Mask the value of an entity.
    MASK = "Mask"
    #: Hide the presence of an entity.
    HIDE = "Hide"


class ExportApi(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ExportApi."""

    TRUE = "true"


class ExportFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ExportFormat."""

    #: Export the Api Definition in OpenAPI 2.0 Specification as JSON document to the Storage Blob.
    SWAGGER = "swagger-link"
    #: Export the Api Definition in WSDL Schema to Storage Blob. This is only supported for APIs of
    #: Type ``soap``
    WSDL = "wsdl-link"
    #: Export the Api Definition in WADL Schema to Storage Blob.
    WADL = "wadl-link"
    #: Export the Api Definition in OpenAPI 3.0 Specification as YAML document to Storage Blob.
    OPENAPI = "openapi-link"
    #: Export the Api Definition in OpenAPI 3.0 Specification as JSON document to Storage Blob.
    OPENAPI_JSON = "openapi+json-link"


class ExportResultFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Format in which the API Details are exported to the Storage Blob with Sas Key valid for 5
    minutes.
    """

    #: The API Definition is exported in OpenAPI Specification 2.0 format to the Storage Blob.
    SWAGGER = "swagger-link-json"
    #: The API Definition is exported in WSDL Schema to Storage Blob. This is only supported for APIs
    #: of Type ``soap``
    WSDL = "wsdl-link+xml"
    #: Export the API Definition in WADL Schema to Storage Blob.
    WADL = "wadl-link-json"
    #: Export the API Definition in OpenAPI Specification 3.0 to Storage Blob.
    OPEN_API = "openapi-link"


class GrantType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """GrantType."""

    #: Authorization Code Grant flow as described https://tools.ietf.org/html/rfc6749#section-4.1.
    AUTHORIZATION_CODE = "authorizationCode"
    #: Implicit Code Grant flow as described https://tools.ietf.org/html/rfc6749#section-4.2.
    IMPLICIT = "implicit"
    #: Resource Owner Password Grant flow as described
    #: https://tools.ietf.org/html/rfc6749#section-4.3.
    RESOURCE_OWNER_PASSWORD = "resourceOwnerPassword"
    #: Client Credentials Grant flow as described https://tools.ietf.org/html/rfc6749#section-4.4.
    CLIENT_CREDENTIALS = "clientCredentials"


class GroupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Group type."""

    CUSTOM = "custom"
    SYSTEM = "system"
    EXTERNAL = "external"


class HostnameType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Hostname type."""

    PROXY = "Proxy"
    PORTAL = "Portal"
    MANAGEMENT = "Management"
    SCM = "Scm"
    DEVELOPER_PORTAL = "DeveloperPortal"


class HttpCorrelationProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sets correlation protocol to use for Application Insights diagnostics."""

    #: Do not read and inject correlation headers.
    NONE = "None"
    #: Inject Request-Id and Request-Context headers with request correlation data. See
    #: https://github.com/dotnet/corefx/blob/master/src/System.Diagnostics.DiagnosticSource/src/HttpCorrelationProtocol.md.
    LEGACY = "Legacy"
    #: Inject Trace Context headers. See https://w3c.github.io/trace-context.
    W3_C = "W3C"


class IdentityProviderType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IdentityProviderType."""

    #: Facebook as Identity provider.
    FACEBOOK = "facebook"
    #: Google as Identity provider.
    GOOGLE = "google"
    #: Microsoft Live as Identity provider.
    MICROSOFT = "microsoft"
    #: Twitter as Identity provider.
    TWITTER = "twitter"
    #: Azure Active Directory as Identity provider.
    AAD = "aad"
    #: Azure Active Directory B2C as Identity provider.
    AAD_B2_C = "aadB2C"


class IssueType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of issue."""

    UNKNOWN = "Unknown"
    AGENT_STOPPED = "AgentStopped"
    GUEST_FIREWALL = "GuestFirewall"
    DNS_RESOLUTION = "DnsResolution"
    SOCKET_BIND = "SocketBind"
    NETWORK_SECURITY_RULE = "NetworkSecurityRule"
    USER_DEFINED_ROUTE = "UserDefinedRoute"
    PORT_THROTTLED = "PortThrottled"
    PLATFORM = "Platform"


class KeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Key to be used to generate token for user."""

    PRIMARY = "primary"
    SECONDARY = "secondary"


class LoggerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Logger type."""

    #: Azure Event Hub as log destination.
    AZURE_EVENT_HUB = "azureEventHub"
    #: Azure Application Insights as log destination.
    APPLICATION_INSIGHTS = "applicationInsights"
    #: Azure Monitor
    AZURE_MONITOR = "azureMonitor"


class Method(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The HTTP method to be used."""

    GET = "GET"
    POST = "POST"


class NameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Invalid indicates the name provided does not match the resource provider’s naming requirements
    (incorrect length, unsupported characters, etc.)  AlreadyExists indicates that the name is
    already in use and is therefore unavailable.
    """

    VALID = "Valid"
    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class NotificationName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """NotificationName."""

    #: The following email recipients and users will receive email notifications about subscription
    #: requests for API products requiring approval.
    REQUEST_PUBLISHER_NOTIFICATION_MESSAGE = "RequestPublisherNotificationMessage"
    #: The following email recipients and users will receive email notifications about new API product
    #: subscriptions.
    PURCHASE_PUBLISHER_NOTIFICATION_MESSAGE = "PurchasePublisherNotificationMessage"
    #: The following email recipients and users will receive email notifications when new applications
    #: are submitted to the application gallery.
    NEW_APPLICATION_NOTIFICATION_MESSAGE = "NewApplicationNotificationMessage"
    #: The following recipients will receive blind carbon copies of all emails sent to developers.
    BCC = "BCC"
    #: The following email recipients and users will receive email notifications when a new issue or
    #: comment is submitted on the developer portal.
    NEW_ISSUE_PUBLISHER_NOTIFICATION_MESSAGE = "NewIssuePublisherNotificationMessage"
    #: The following email recipients and users will receive email notifications when developer closes
    #: his account.
    ACCOUNT_CLOSED_PUBLISHER = "AccountClosedPublisher"
    #: The following email recipients and users will receive email notifications when subscription
    #: usage gets close to usage quota.
    QUOTA_LIMIT_APPROACHING_PUBLISHER_NOTIFICATION_MESSAGE = "QuotaLimitApproachingPublisherNotificationMessage"


class OperationNameFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The format of the Operation Name for Application Insights telemetries. Default is Name."""

    #: API_NAME;rev=API_REVISION - OPERATION_NAME
    NAME = "Name"
    #: HTTP_VERB URL
    URL = "Url"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The origin of the issue."""

    LOCAL = "Local"
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class PlatformVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Compute Platform Version running the service."""

    #: Platform version cannot be determined, as compute platform is not deployed.
    UNDETERMINED = "undetermined"
    #: Platform running the service on Single Tenant V1 platform.
    STV1 = "stv1"
    #: Platform running the service on Single Tenant V2 platform.
    STV2 = "stv2"
    #: Platform running the service on Multi Tenant V1 platform.
    MTV1 = "mtv1"


class PolicyContentFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Format of the policyContent."""

    #: The contents are inline and Content type is an XML document.
    XML = "xml"
    #: The policy XML document is hosted on a http endpoint accessible from the API Management
    #: service.
    XML_LINK = "xml-link"
    #: The contents are inline and Content type is a non XML encoded policy document.
    RAWXML = "rawxml"
    #: The policy document is not Xml encoded and is hosted on a http endpoint accessible from the API
    #: Management service.
    RAWXML_LINK = "rawxml-link"


class PolicyExportFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PolicyExportFormat."""

    #: The contents are inline and Content type is an XML document.
    XML = "xml"
    #: The contents are inline and Content type is a non XML encoded policy document.
    RAWXML = "rawxml"


class PolicyIdName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PolicyIdName."""

    POLICY = "policy"


class PolicyScopeContract(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PolicyScopeContract."""

    TENANT = "Tenant"
    PRODUCT = "Product"
    API = "Api"
    OPERATION = "Operation"
    ALL = "All"


class PortalRevisionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the portal's revision."""

    #: Portal's revision has been queued.
    PENDING = "pending"
    #: Portal's revision is being published.
    PUBLISHING = "publishing"
    #: Portal's revision publishing completed.
    COMPLETED = "completed"
    #: Portal's revision publishing failed.
    FAILED = "failed"


class PreferredIPVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The IP version to be used. Only IPv4 is supported for now."""

    I_PV4 = "IPv4"


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PrivateEndpointServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private endpoint connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ProductState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """whether product is published or not. Published products are discoverable by users of developer
    portal. Non published products are visible only to administrators. Default state of Product is
    notPublished.
    """

    NOT_PUBLISHED = "notPublished"
    PUBLISHED = "published"


class Protocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol."""

    HTTP = "http"
    HTTPS = "https"
    WS = "ws"
    WSS = "wss"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether or not public endpoint access is allowed for this API Management service.  Value is
    optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints
    are the exclusive access method. Default value is 'Enabled'.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ResourceSkuCapacityScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scale type applicable to the sku."""

    #: Supported scale type automatic.
    AUTOMATIC = "automatic"
    #: Supported scale type manual.
    MANUAL = "manual"
    #: Scaling not supported.
    NONE = "none"


class SamplingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sampling type."""

    #: Fixed-rate sampling.
    FIXED = "fixed"


class SchemaType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Schema Type. Immutable."""

    #: Xml schema type.
    XML = "xml"
    #: Json schema type.
    JSON = "json"


class SettingsTypeName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SettingsTypeName."""

    PUBLIC = "public"


class Severity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The severity of the issue."""

    ERROR = "Error"
    WARNING = "Warning"


class SkuType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the Sku."""

    #: Developer SKU of Api Management.
    DEVELOPER = "Developer"
    #: Standard SKU of Api Management.
    STANDARD = "Standard"
    #: Premium SKU of Api Management.
    PREMIUM = "Premium"
    #: Basic SKU of Api Management.
    BASIC = "Basic"
    #: Consumption SKU of Api Management.
    CONSUMPTION = "Consumption"
    #: Isolated SKU of Api Management.
    ISOLATED = "Isolated"


class SoapApiType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of API to create.


    * ``http`` creates a REST API
    * ``soap`` creates a SOAP pass-through API
    * ``websocket`` creates websocket API
    * ``graphql`` creates GraphQL API.
    """

    #: Imports a SOAP API having a RESTful front end.
    SOAP_TO_REST = "http"
    #: Imports the SOAP API having a SOAP front end.
    SOAP_PASS_THROUGH = "soap"
    #: Imports the API having a Websocket front end.
    WEB_SOCKET = "websocket"
    #: Imports the API having a GraphQL front end.
    GRAPH_QL = "graphql"


class State(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the issue."""

    #: The issue is proposed.
    PROPOSED = "proposed"
    #: The issue is opened.
    OPEN = "open"
    #: The issue was removed.
    REMOVED = "removed"
    #: The issue is now resolved.
    RESOLVED = "resolved"
    #: The issue was closed.
    CLOSED = "closed"


class SubscriptionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Subscription state. Possible states are * active – the subscription is active, * suspended –
    the subscription is blocked, and the subscriber cannot call any APIs of the product, *
    submitted – the subscription request has been made by the developer, but has not yet been
    approved or rejected, * rejected – the subscription request has been denied by an
    administrator, * cancelled – the subscription has been cancelled by the developer or
    administrator, * expired – the subscription reached its expiration date and was deactivated.
    """

    SUSPENDED = "suspended"
    ACTIVE = "active"
    EXPIRED = "expired"
    SUBMITTED = "submitted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class TemplateName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TemplateName."""

    APPLICATION_APPROVED_NOTIFICATION_MESSAGE = "applicationApprovedNotificationMessage"
    ACCOUNT_CLOSED_DEVELOPER = "accountClosedDeveloper"
    QUOTA_LIMIT_APPROACHING_DEVELOPER_NOTIFICATION_MESSAGE = "quotaLimitApproachingDeveloperNotificationMessage"
    NEW_DEVELOPER_NOTIFICATION_MESSAGE = "newDeveloperNotificationMessage"
    EMAIL_CHANGE_IDENTITY_DEFAULT = "emailChangeIdentityDefault"
    INVITE_USER_NOTIFICATION_MESSAGE = "inviteUserNotificationMessage"
    NEW_COMMENT_NOTIFICATION_MESSAGE = "newCommentNotificationMessage"
    CONFIRM_SIGN_UP_IDENTITY_DEFAULT = "confirmSignUpIdentityDefault"
    NEW_ISSUE_NOTIFICATION_MESSAGE = "newIssueNotificationMessage"
    PURCHASE_DEVELOPER_NOTIFICATION_MESSAGE = "purchaseDeveloperNotificationMessage"
    PASSWORD_RESET_IDENTITY_DEFAULT = "passwordResetIdentityDefault"
    PASSWORD_RESET_BY_ADMIN_NOTIFICATION_MESSAGE = "passwordResetByAdminNotificationMessage"
    REJECT_DEVELOPER_NOTIFICATION_MESSAGE = "rejectDeveloperNotificationMessage"
    REQUEST_DEVELOPER_NOTIFICATION_MESSAGE = "requestDeveloperNotificationMessage"


class UserState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Account state. Specifies whether the user is active or not. Blocked users are unable to sign
    into the developer portal or call any APIs of subscribed products. Default state is Active.
    """

    #: User state is active.
    ACTIVE = "active"
    #: User is blocked. Blocked users cannot authenticate at developer portal or call API.
    BLOCKED = "blocked"
    #: User account is pending. Requires identity confirmation before it can be made active.
    PENDING = "pending"
    #: User account is closed. All identities and related entities are removed.
    DELETED = "deleted"


class Verbosity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The verbosity level applied to traces emitted by trace policies."""

    #: All the traces emitted by trace policies will be sent to the logger attached to this diagnostic
    #: instance.
    VERBOSE = "verbose"
    #: Traces with 'severity' set to 'information' and 'error' will be sent to the logger attached to
    #: this diagnostic instance.
    INFORMATION = "information"
    #: Only traces with 'severity' set to 'error' will be sent to the logger attached to this
    #: diagnostic instance.
    ERROR = "error"


class VersioningScheme(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An value that determines where the API Version identifier will be located in a HTTP request."""

    #: The API Version is passed in a path segment.
    SEGMENT = "Segment"
    #: The API Version is passed in a query parameter.
    QUERY = "Query"
    #: The API Version is passed in a HTTP header.
    HEADER = "Header"


class VirtualNetworkType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of VPN in which API Management service needs to be configured in. None (Default Value)
    means the API Management service is not part of any Virtual Network, External means the API
    Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint,
    and Internal means that API Management deployment is setup inside a Virtual Network having an
    Intranet Facing Endpoint only.
    """

    #: The service is not part of any Virtual Network.
    NONE = "None"
    #: The service is part of Virtual Network and it is accessible from Internet.
    EXTERNAL = "External"
    #: The service is part of Virtual Network and it is only accessible from within the virtual
    #: network.
    INTERNAL = "Internal"
