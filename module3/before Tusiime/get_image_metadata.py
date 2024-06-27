from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
image_url = "https://www.shutterstock.com/shutterstock/photos/2407352865/display_1500/stock-photo-a-sea-turtle-gracefully-navigating-the-turquoise-waters-of-island-the-unique-shell-patterns-of-the-2407352865.jpg"
described_response = computervision_client.describe_image(image_url, max_candidates=1)
print(described_response)