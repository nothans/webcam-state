"""

This Python script checks if my webcam is in use and posts my On-Air status to a ThingSpeak Channel.

If my webcam is in use, then I am "On-Air".

For more information: https://nothans.com/on-air-light-for-microsoft-teams-and-zoom-meetings

Dependencies

    * pip install opencv-python
    * pip install requests
    
Setup
    
    * Create ThingSpeak channel at https://thingspeak.com with Field 1 enabled
    * Add your channel's Write API Key to the thingSpeakWriteKey variable

Created: Feb 11, 2021 by Hans Scharler (http://www.nothans.com)

"""

import cv2
import requests

thingspeakWriteURL = 'https://api.thingspeak.com/update.json'
thingSpeakWriteKey = 'WWWWXXXXYYYYZZZZ'

def returnWebcamStatus(webcamIndex):

    webcam = cv2.VideoCapture(webcamIndex, cv2.CAP_DSHOW)

    if webcam.isOpened():
        webcam.release()
        return True #Webcam not in use
    else:
        return False #Webcam in use


def postToThingSpeak(valueToPost):

    thingSpeakWriteData = {'field1': valueToPost, 'api_key': thingSpeakWriteKey}

    thingspeakRequest = requests.post(thingspeakWriteURL, data = thingSpeakWriteData)

    return


def main():

    # Get webcamStatus for webcam 0 - Change this index to match the webcam that you want to track
    webcamStatus = returnWebcamStatus(0)

    # Post if On-Air or not to Field 1 of a ThingSpeak Channel
    if webcamStatus:
        postToThingSpeak(0) #Not On-Air
    else:
        postToThingSpeak(1) #On-Air


if __name__ == '__main__':
    main()
