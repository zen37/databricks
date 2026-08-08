"""
One-time setup script: creates the Databricks secret scopes and stores the
Massive API key + Lakebase URL. Run locally (with the Databricks CLI configured)
or from a notebook - never commit the resulting secret value anywhere.

Usage:
    python setup_secrets.py
"""

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace
from databricks.sdk.errors import ResourceAlreadyExists
import getpass

w = WorkspaceClient()


def ensure_scope(scope: str):
    """Create a secret scope, skipping if it already exists."""
    try:
        w.secrets.create_scope(scope=scope)
        print(f"Created scope '{scope}'.")
    except ResourceAlreadyExists:
        print(f"Scope '{scope}' already exists — skipping creation.")


ensure_scope("massive")
w.secrets.put_secret(
    scope="massive",
    key="api-key",
    string_value=getpass.getpass("Paste your Massive API key: "),
)

ensure_scope("database")
w.secrets.put_secret(
    scope="database",
    key="lakebase-url",
    string_value=getpass.getpass("Paste your Lakebase URL: "),
)

w.secrets.put_acl(
    scope="database",
    principal="users",
    permission=workspace.AclPermission.READ,
)
w.secrets.put_acl(
    scope="massive",
    principal="users",
    permission=workspace.AclPermission.READ,
)

print("Secrets and ACLs configured.")
