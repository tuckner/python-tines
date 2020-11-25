# Tines Python API Wrapper

Python client for interacting with the Tines API

## Usage

```
import tines
import json

api = tines.TinesAPI(tenant=tenant, email=email, token=token)
resp = api.get_agent(id=1)
print(json.dumps(resp.json()))
```
