import requests
import json


class GraphQLTester:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token
        self.headers = {}

        if token:
            self.headers["Authorization"] = f"JWT {token}"
    
    def _execute_query(self, query, variables=None, files=None):
        payload = {
            "query": query,
            "variables": variables or {}
        }

        if files:
            files_payload = {
                'operations': (None, json.dumps(payload), 'application/json'),
                'map': (None, '{"0": ["variables.avatar"]}', 'application/json'),
                '0': (files['file_name', open(files['file_path'], 'rb'), files['file_type']])
            }
            response = requests.post(self.base_url, files=files_payload, headers=self.headers)
        
        else:
            response = requests.post(self.base_url, json=payload, headers=self.headerse)
