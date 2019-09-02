# Pixabay-API
# Lightning Code
# Created by Jachimike Onuoha.
# Copyright © 2019 Jachimike Onuoha. All rights reserved.

from pixabay import Image, Video
from Settings import myKey
import urllib.request
import pprint
import os

# Assign your Api key to the environment variable "PIXABAY_API_KEY" and the working variable API_KEY
os.environ["PIXABAY_API_KEY"] = myKey
API_KEY = myKey

# Search for any image using the Image query
Image = Image(API_KEY)
newImage = Image.search(q='YOUR_SEARCH')

# Pretty print response to improve readability
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(newImage)

# Get the value for the preview URL
payload_one = newImage['hits'][15]['previewURL']
print("This is the preview URL {}".format(payload_one))


# Search for any video using the Video query
Video = Video(API_KEY)
newVideo = Video.search(q='YOUR_SEARCH')

# Pretty print response to improve readability
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(newVideo)

# Get the value for a particular video URL
payload_two = newVideo['hits'][0]['videos']['medium']['url']
print("This is the preview URL {}".format(payload_two))

# Download the particular video
urllib.request.urlretrieve(payload_two, 'FirstVid.mp4')
