import requests

voice = 'banmai'
url = 'https://api.fpt.ai/hmi/tts/v5'
apiKey = '0ZGJgMClDttHIicFtiic1N9JZc8ZyQsF'


class VoiceGenerator:

  def getVoice(payload: str):
    data = payload.encode('utf-8')
    headers = {
        'speed': '',
        'voice': voice,
        'api-key': apiKey,
    }
    response = requests.request('POST', url, data=data, headers=headers)
    print(response.text)

    return response.json()

    # {"async": "https://file01.fpt.ai/text2speech-v5/short/2023-12-21/1b26bab1b2f0825b486b300426645b2e.mp3", "error": 0,
    #  "message": "The content will be returned after a few seconds under the async link.", "request_id": "0a88a3a4-e988-4ad3-accf-4e4ecbc4783b"}
