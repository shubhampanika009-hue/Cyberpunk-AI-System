import json
import urllib.request
import urllib.error

class LiveMatrixBrain:
    # यहाँ अपनी असली Google Gemini API Key डालें
    API_KEY = "YOUR_REAL_GEMINI_API_KEY_HERE"

    @staticmethod
    def process_request(prompt):
        if LiveMatrixBrain.API_KEY == "YOUR_REAL_GEMINI_API_KEY_HERE":
            return "BOSS: Please insert your valid Google Gemini API Key in gemini_brain.py."

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={LiveMatrixBrain.API_KEY}"
        headers = {'Content-Type': 'application/json'}
        
        system_instruction = (
            "You are the Tactical Neural Matrix AI Assistant for Boss Raja. "
            "Give direct, sharp, and military-grade tactical responses."
        )
        
        data = {
            "contents": [{
                "parts": [{"text": f"{system_instruction}\nUser Prompt: {prompt}"}]
            }]
        }

        try:
            req_data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=req_data, headers=headers, method='POST')
            with urllib.request.urlopen(req, timeout=15) as response:
                res_body = response.read().decode('utf-8')
                res_json = json.loads(res_body)
                answer = res_json['candidates'][0]['content']['parts'][0]['text']
                return answer.strip()
        except urllib.error.HTTPError as e:
            return f"API Connection Error: HTTP {e.code}. Check your API Key."
        except Exception as e:
            return f"Neural Matrix Core Error -> {str(e)}"
