# list Azure User Groups listed in Entra ID (Active Directory)

## Prompt:

> how to use python to list azure user license and groups

## Bing Copilot Response:

Certainly! To list Azure user licenses and groups using Python, you can leverage the Azure SDK for Python, specifically the azure-identity and azure-graphrbac libraries. Below is a concise guide to help you get started:

### Prerequisites

- Azure Subscription: Ensure you have an Azure subscription.
- Service Principal: Create a service principal with the necessary permissions to read user information.
- Install Required Libraries: Install the Azure SDK libraries using pip:
```
pip install azure-identity azure-graphrbac
```

### Step-by-Step Guide

1. Authentication

First, authenticate using the `DefaultAzureCredential` from `azure-identity`.

```python
from azure.identity import DefaultAzureCredential
from azure.graphrbac import GraphRbacManagementClient

# Initialize the credential
credential = DefaultAzureCredential()

# Replace with your Azure AD tenant ID
tenant_id = 'your-tenant-id'

# Initialize the GraphRbacManagementClient
client = GraphRbacManagementClient(credential, tenant_id)
```

2. List Users and Their Licenses

To list users and their licenses, you can use the users property of the GraphRbacManagementClient.

```python
# List all users
users = client.users.list()

for user in users:
    print(f"User: {user.display_name}, Email: {user.mail}")
    # Assuming you have a method to get licenses for a user
    licenses = client.users.get_license_details(user.object_id)
    for license in licenses:
        print(f"  License: {license.sku_id}")
```

3. List User Groups

To list the groups a user belongs to, you can use the get_member_groups method.

```python
for user in users:
    print(f"User: {user.display_name}, Email: {user.mail}")
    groups = client.users.get_member_groups(user.object_id, security_enabled_only=False)
    for group in groups:
        print(f"  Group: {group}")
```

### Complete Example

Here is a complete example combining both user licenses and groups:

```python
from azure.identity import DefaultAzureCredential
from azure.graphrbac import GraphRbacManagementClient

# Initialize the credential
credential = DefaultAzureCredential()

# Replace with your Azure AD tenant ID
tenant_id = 'your-tenant-id'

# Initialize the GraphRbacManagementClient
client = GraphRbacManagementClient(credential, tenant_id)

# List all users
users = client.users.list()

for user in users:
    print(f"User: {user.display_name}, Email: {user.mail}")
    
    # List user licenses
    licenses = client.users.get_license_details(user.object_id)
    for license in licenses:
        print(f"  License: {license.sku_id}")
    
    # List user groups
    groups = client.users.get_member_groups(user.object_id, security_enabled_only=False)
    for group in groups:
        print(f"  Group: {group}")
```

### Notes

Ensure your service principal has the necessary permissions to read user and group information.
The `DefaultAzureCredential` will attempt to authenticate using multiple methods. Ensure your environment is configured correctly for one of these methods.

This should help you get started with listing Azure user licenses and groups using Python. If you have any specific requirements or run into issues, feel free to ask!

## 2025-02-08

- 待驗證！