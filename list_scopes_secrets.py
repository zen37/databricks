print(dbutils.secrets.listScopes())
print(dbutils.secrets.list("massive"))
print(dbutils.secrets.list("database"))
print("------")
for scope in dbutils.secrets.listScopes():
    for secret in dbutils.secrets.list(scope.name):
        print(f"{scope.name}  →  {secret.key}")
