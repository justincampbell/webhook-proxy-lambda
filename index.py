import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def proxy_request(event, context):
    logger.info("event:{}".format(event))
    logger.info("context:{}".format(context))

    url = event["url"]
    payload = event["payload"]

    response = requests.post(url, data=payload)

    response.raise_for_status()

    parsed_response = json.loads(response.text)
    logger.info("response:{}".format(parsed_response))

    return parsed_response
