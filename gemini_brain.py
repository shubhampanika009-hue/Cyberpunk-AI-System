import json
import os
import urllib.request
import urllib.error
import ssl

class LiveMatrixBrain:
    KEY_FILE = "matrix_config.json"
    # डिफ़ॉल्ट/फॉलबैक एपीआई की
    DEFAULT_API_KEY = "AQ.Ab8RN6LttionW8VjuHP3l8T2CPxWuocIHs9XyFGpsl0n-GTM4Q"

    @classmethod
    def get_saved_key(cls):
        """लोकल फाइल से सेव की गई API Key पढ़ता है या फॉलबैक इस्तेमाल करता है।"""
        if os.path.exists(cls.KEY_FILE):
            try:
                with open(cls.KEY_FILE, 'r') as f:
                    data = json.load(f)
                    saved_key = data.get("api_key", "").strip()
                    if saved_key:
                        return saved_key
            except Exception:
                pass
        return cls.DEFAULT_API_KEY

    @classmethod
    def save_api_key(cls, key_val):
        """इनपुट/क्लिपबोर्ड से आई नई API Key को लोकल फाइल में परमानेंट सेव करता है।"""
        try:
            if key_val:
                clean_key = key_val.strip()
                with open(cls.KEY_FILE, 'w') as f:
                    json.dump({"api_key": clean_key}, f)
                return True
        except Exception:
            pass
        return False

    @classmethod
    def process_request(cls, prompt):
        api_key = cls.get_saved_key()
        if not api_key:
            return "BOSS: API Key missing or not configured!"

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
            
            # एंड्रॉइड पर SSL वेरिफिकेशन एरर से बचने के लिए
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
