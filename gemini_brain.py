import json
import os
import urllib.request
import urllib.error

class LiveMatrixBrain:
    KEY_FILE = "matrix_config.json"

    @staticmethod
    def get_saved_key():
        if os.path.exists(LiveMatrixBrain.KEY_FILE):
            try:
                with open(LiveMatrixBrain.KEY_FILE, 'r') as f:
                    data = json.load(f)
                    return data.get("api_key", "")
            except Exception:
                pass
        return ""

    @staticmethod
    def save_api_key(key):
        try:
            with open(LiveMatrixBrain.KEY_FILE, 'w') as f:
                json.dump({"api_key": key.strip()}, f)
            return True
        except Exception:
            return False

    @staticmethod
    def process_request(prompt):
        api_key = LiveMatrixBrain.get_saved_key()
        if not api_key:
            return "BOSS: API Key not found! Type '/key YOUR_GEMINI_API_KEY' in chat to set it."

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
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
            return f"API Connection Error: HTTP {e.code}. Check if your API Key is valid."
        except Exception as e:
            return f"Neural Matrix Core Error -> {str(e)}"
