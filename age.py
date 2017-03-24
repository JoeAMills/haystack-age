import requests
import json
import sys

apiKey = "**API KEY**"

# https://www.haystack.ai/docs?python#analyze
def getEthnicity(imageData1):
	outputType = "json"
	requestUri = "https://api.haystack.ai/api/image/analyze?output={}&apikey={}&model=age".format(outputType, apiKey)
	apiResponse = requests.post(requestUri, data=imageData1)
	response = json.loads(apiResponse.text)
	
	return response["people"][0]["age"]

image1 = sys.argv[1]

with open(image1, "rb") as imageData1:
	print(getEthnicity(imageData1))