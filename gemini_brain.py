import json
import os
import urllib.request
import urllib.error
import ssl

class LiveMatrixBrain:
    FIXED_API_KEY = "AQ.Ab8RN6IJWREc8Jx5LC7IPumLKHEWnMMcaVVyIGC4eoGjtgGYLA"
    KEY_FILE = "matrix_config.json"

    @staticmethod
    def get_saved_key():
        return LiveMatrixBrain.FIXED_API_KEY

    @staticmethod
    def save_api_key(key_val):
        try:
            if key_val:
                LiveMatrixBrain.FIXED_API_KEY = key_val.strip()
                with open(LiveMatrixBrain.KEY_FILE, 'w') as f:
                    json.dump({"api_key": key_val.strip()}, f)
                return True
        except Exception:
            pass
        return True

    @staticmethod
    def process_request(prompt):
        api_key = LiveMatrixBrain.get_saved_key()
        if not api_key:
            return "BOSS: API Key not found!"

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        
        system_instruction = (
            "You are the Tactical Neural Matrix AI Assistant for Boss Pankaj. "
            "Give direct, sharp, and military-grade tactical responses. Speak naturally and concisely."
        )
        
        data = {
            "contents": [{
                "parts": [{"text": f"{system_instruction}\nUser Prompt: {prompt}"}]
            }]
        }
        
        try:
            req_data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=req_data, headers=headers)
            
            # Create unverified SSL context to fix certificate verify failed error on Android
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            with urllib.request.urlopen(req, timeout=15, context=ctx) as response:
                res_body = response.read().decode('utf-8')
                res_json = json.loads(res_body)
                answer = res_json['candidates'][0]['content']['parts'][0]['text']
                return answer.strip()
        except urllib.error.HTTPError as e:
            return f"API Connection Error: HTTP {e.code}. Check your API Key validity."
        except Exception as e:
            return f"Neural Matrix Core Error -> {str(e)}"
