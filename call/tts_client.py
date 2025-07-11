import requests
ELEVENLABS_API_KEY = 'your_api_key_here'
VOICE_ID = 'your_cloned_voice_id'

def text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}}
    response = requests.post(url, json=data, headers=headers, stream=True)
    return response.iter_content(chunk_size=1024)
