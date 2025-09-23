# OpenSearch RESTful API

- Document
  - https://docs.opensearch.org/latest/api-reference/#rest-apis
- Git Repo
  - https://github.com/opensearch-project/opensearch-api-specification
- Release
  - https://github.com/opensearch-project/opensearch-api-specification/releases

## 2025-09-20

- By Microsoft 365 Copilot
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a Python CLI example with the following functionality?

1. read OpenSearch Server URL from option `-s`
2. read AWS Cognito authentication tokens from cookie file (default: storage_state.json) from option `-c`
3. call OpenSearch API and show Server Information as response

</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Here's a Python CLI example using `argparse` to read the OpenSearch server URL and AWS Cognito authentication tokens from a cookie file, then call the OpenSearch API to retrieve and display server information.

### ✅ Features:
1. `-s` or `--server`: OpenSearch server URL
2. `-c` or `--cookie`: Cookie file path (default: `storage_state.json`)
3. Uses `requests` to make the API call with cookies

---

### 🐍 Python Code Example

```python
import argparse
import json
import requests

def load_cookies(cookie_file):
    try:
        with open(cookie_file, 'r') as f:
            cookies_data = json.load(f)
        # Convert cookies to a dict suitable for requests
        cookies = {cookie['name']: cookie['value'] for cookie in cookies_data.get('cookies', [])}
        return cookies
    except Exception as e:
        print(f"Error loading cookies: {e}")
        return {}

def get_server_info(server_url, cookies):
    try:
        response = requests.get(f"{server_url}/", cookies=cookies)
        response.raise_for_status()
        print("Server Information:")
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to OpenSearch server: {e}")

def main():
    parser = argparse.ArgumentParser(description="OpenSearch Server Info CLI")
    parser.add_argument("-s", "--server", required=True, help="OpenSearch server URL")
    parser.add_argument("-c", "--cookie", default="storage_state.json", help="Path to cookie file (default: storage_state.json)")
    args = parser.parse_args()

    cookies = load_cookies(args.cookie)
    get_server_info(args.server, cookies)

if __name__ == "__main__":
    main()
```

---

### 🧪 Example Usage

```bash
python opensearch_info.py -s https://your-opensearch-domain.com -c storage_state.json
```

Would you like me to help you test this with a mock OpenSearch server or generate a sample `storage_state.json` file?
</td></tr></table>

- By Microsoft Bing Copilot
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
opensearch restful api swagger
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
OpenSearch provides a RESTful API that can be documented and explored using Swagger/OpenAPI specifications. Here's how you can work with OpenSearch's REST API and Swagger:

1. OpenSearch REST API Overview
OpenSearch's REST API allows you to interact with the OpenSearch cluster for operations like:

Indexing and searching documents
Managing indices
Monitoring the cluster
Performing aggregations and more

The API is compatible with Elasticsearch's REST API, making it easy to integrate with existing tools.

2. Swagger/OpenAPI Specification for OpenSearch
The OpenSearch project provides an OpenAPI 3.1.0 specification for its REST APIs. This specification can be used to generate Swagger documentation or client SDKs.
Key Resources:

GitHub Repository: The OpenSearch API specification is maintained in the OpenSearch API Specification GitHub repository.
OpenAPI Specification: The repository contains a YAML file that defines the OpenSearch REST API in OpenAPI format.


3. Using Swagger with OpenSearch
To use Swagger with OpenSearch, follow these steps:
Step 1: Download the OpenAPI Specification

Visit the OpenSearch API Specification GitHub repository.
Download the openapi.yaml file, which contains the OpenAPI 3.1.0 specification.

Step 2: Load the Specification into Swagger UI

Install Swagger UI locally or use the hosted version at Swagger Editor.
Upload the openapi.yaml file to Swagger UI.
Explore the API documentation interactively.

Step 3: Generate Client SDKs (Optional)
You can use tools like Swagger Codegen or OpenAPI Generator to generate client SDKs in various programming languages (e.g., Python, Java, JavaScript).

4. Example: Accessing OpenSearch REST API
Here’s an example of a REST API call to OpenSearch using curl:
Request: Search for documents in an index
Bashcurl -X GET "http://localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "field_name": "value"
    }
  }
}'

Response:
Json{
  "took": 10,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "my-index",
        "_id": "1",
        "_score": 1.0,
        "_source": {
          "field_name": "value"
        }
      }
    ]
  }
}


5. Benefits of Using Swagger with OpenSearch

Interactive Documentation: Swagger UI provides a user-friendly interface to explore and test APIs.
Client SDK Generation: Automate the creation of client libraries for your applications.
Standardized API Documentation: OpenAPI ensures consistent and machine-readable API documentation.


If you need help setting up Swagger or working with OpenSearch APIs, let me know!
</td></tr></table>

## Cluster API

- https://docs.opensearch.org/latest/api-reference/cluster-api/cluster-health/
- https://docs.opensearch.org/latest/api-reference/cluster-api/cluster-settings/