from flow import Text2CodeRequest, HEADERS, PARAMS
import json

res = Text2CodeRequest._create_to_code_request("Create a function X with argument alpha, beta and gamma that returns Y", HEADERS, PARAMS)
print(json.dumps(res))