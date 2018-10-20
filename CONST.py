LUIS_ENDPOINT = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/7cd5279c-2cdc-4234-b5dc-f2a4bfa809f2"
CREDENTIAL_FILE_NAME = "/speech2code-0d3ecaa13ec2.json"

HEADERS = {
    # Request headers
    "Ocp-Apim-Subscription-Key": "6a6728b9981d417280f4dad97f82df96",
    "content-type": "application/json",
}

PARAMS = {
    # Don't forget to add query parameter "q": "query"
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}