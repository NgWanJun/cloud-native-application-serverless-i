import json


def hello(event, context):
    body = {
        "message": "Ello World!!! :D",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
