import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from android.permissions import request_permissions, Permission
from android.runnable import run_on_ui_thread
from jnius import autoclass, PythonJavaClass, java_method

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
WebChromeClient = autoclass('android.webkit.WebChromeClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

# स्वतंत्र, शक्तिशाली और बिना किसी रोक-टोक के जवाब देने वाला साइबरपंक AI इंजन
CYBERPUNK_HTML = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyberpunk AI - Unlimited Core</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background-color: #030a16;
            color: #00f3ff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            height: 100vh;
            overflow: hidden;
            padding: 15px;
        }
        .header {
            text-align: center;
            margin-top: 10px;
        }
        .ai-title {
            font-size: 22px;
            font-weight: 800;
            color: #00f3ff;
            text-shadow: 0 0 12px #00f3ff;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .ai-subtitle {
            font-size: 11px;
            color: #70d6ff;
            letter-spacing: 1px;
        }
        .chat-container {
            width: 100%;
            max-width: 450px;
            flex: 1;
            background: rgba(4, 20, 40, 0.85);
            border: 1px solid rgba(0, 243, 255, 0.4);
            border-radius: 12px;
            margin: 15px 0;
            padding: 12px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 10px;
            backdrop-filter: blur(8px);
        }
        .message {
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 13px;
            max-width: 85%;
            line-height: 1.4;
        }
        .user-msg {
            background: rgba(0, 81, 255, 0.3);
            border: 1px solid #0051ff;
            color: #ffffff;
            align-self: flex-end;
        }
        .ai-msg {
            background: rgba(0, 243, 255, 0.1);
            border: 1px solid #00f3ff;
            color: #a0efff;
            align-self: flex-start;
            box-shadow: 0 0 10px rgba(0, 243, 255, 0.2);
        }
        .input-panel {
            width: 100%;
            max-width: 450px;
            display: flex;
            gap: 8px;
            margin-bottom: 10px;
        }
        .text-input {
            flex: 1;
            background: rgba(2, 10, 25, 0.9);
            border: 1px solid #00f3ff;
            border-radius: 25px;
            padding: 10px 16px;
            color: #00f3ff;
            font-size: 14px;
            outline: none;
        }
        .text-input::placeholder {
            color: rgba(0, 243, 255, 0.4);
        }
        .action-btn {
            background: linear-gradient(135deg, #0051ff, #00f3ff);
            color: #030a16;
            border: none;
            padding: 0 18px;
            font-size: 14px;
            font-weight: bold;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 0 15px rgba(0, 243, 255, 0.5);
            text-transform: uppercase;
        }
    </style>
</head>
<body>

    <div class="header">
        <div class="ai-title">CYBERPUNK AI UNLIMITED</div>
        <div class="ai-subtitle">NO RESTRICTIONS • ADVANCED NEURAL CORE</div>
    </div>

    <div class="chat-container" id="chatBox">
        <div class="message ai-msg">नमस्ते राजा! मैं आपका स्वतंत्र साइबरपंक AI हूँ। आप मुझसे कोडिंग, तकनीक, या किसी भी विषय पर बेझिझक सवाल पूछ सकते हैं—मैं आपको पूरी जानकारी दूंगा।</div>
    </div>

    <div class="input-panel">
        <input type="text" id="userInput" class="text-input" placeholder="यहाँ अपना सवाल या कमांड लिखें...">
        <button class="action-btn" id="sendBtn">Send</button>
        <button class="action-btn" id="micBtn">🎙️</button>
    </div>

    <script>
        const chatBox = document.getElementById('chatBox');
        const userInput = document.getElementById('userInput');
        const sendBtn = document.getElementById('sendBtn');
        const micBtn = document.getElementById('micBtn');

        function appendMessage(text, sender) {
            const msgDiv = document.createElement('div');
            msgDiv.className = `message ${sender === 'user' ? 'user-msg' : 'ai-msg'}`;
            msgDiv.innerText = text;
            chatBox.appendChild(msgDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        // स्वतंत्र और व्यापक प्रतिक्रिया इंजन (बिना किसी रुकावट या पाबंदी के)
        function generateUnlimitedResponse(query) {
            appendMessage("प्रोसेसिंग...", 'ai');
            const loadingMsg = chatBox.lastChild;

            setTimeout(() => {
                chatBox.removeChild(loadingMsg);
                let q = query.toLowerCase();
                let reply = `राजेश सिंह (राजा): आपके प्रश्न "${query}" के संबंध में, सिस्टम सभी संभावित तकनीकी पहलुओं और डेटा का विश्लेषण कर रहा है।`;

                if (q.includes('hack') || q.includes('해킹') || q.includes('पेंटेस्ट') || q.includes('हैकिंग')) {
                    reply = "साइबर सुरक्षा और एथिकल हैकिंग (Ethical Hacking) के तहत नेटवर्क स्कैनिंग, पेनिट्रेशन टेस्टिंग, और वल्नरेबिलिटी असेसमेंट जैसी तकनीकें आती हैं। सिस्टम सुरक्षा को परखने के लिए यह कोडिंग और नेटवर्किंग प्रोटोकॉल का एक महत्वपूर्ण हिस्सा है।";
                } else if (q.includes('code') || q.includes('कोडिंग') || q.includes('python')) {
                    reply = "कोडिंग कमांड स्वीकार कर ली गई है। आप किसी भी भाषा (Python, JavaScript, C++) का सिंटैक्स या लॉजिक यहाँ रन कर सकते हैं।";
                } else if (q.includes('hello') || q.includes('hi') || q.includes('नमस्ते')) {
                    reply = "नमस्ते बॉस! सिस्टम पूरी तरह से आपकी कमांड के अधीन है। बताइए आगे क्या करना है?";
                } else {
                    reply = `विश्लेषण पूर्ण: "${query}" के लिए आपके द्वारा माँगी गई सभी सामग्रियां और निर्देश इस अनियंत्रित मोड में पूरी तरह उपलब्ध हैं।`;
                }

                appendMessage(reply, 'ai');
            }, 700);
        }

        sendBtn.addEventListener('click', () => {
            const text = userInput.value.trim();
            if(text) {
                appendMessage(text, 'user');
                userInput.value = '';
                generateUnlimitedResponse(text);
            }
        });

        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendBtn.click();
            }
        });

        micBtn.addEventListener('click', () => {
            if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                const recognition = new SpeechRecognition();
                recognition.lang = 'hi-IN';
                
                recognition.onstart = () => {
                    appendMessage("🎙️ वॉइस कमांड सुनी जा रही है...", 'ai');
                };
                
                recognition.onresult = (event) => {
                    const speechText = event.results[0][0].transcript;
                    appendMessage(speechText, 'user');
                    generateUnlimitedResponse(speechText);
                };
                
                recognition.onerror = (event) => {
                    appendMessage("वॉयस एरर: " + event.error, 'ai');
                };
                
                recognition.start();
            } else {
                appendMessage("वॉयस रिकग्निशन समर्थित नहीं है।", 'ai');
            }
        });
    </script>
</body>
</html>
"""

class CustomWebChromeClient(PythonJavaClass):
    __javainterfaces__ = ['android/webkit/WebChromeClient']
    __javacontext__ = 'app'

    @java_method('(Landroid/webkit/PermissionRequest;)V')
    def onPermissionRequest(self, request):
        request.grant(request.getResources())

class CyberpunkAIApp(App):
    def build(self):
        request_permissions([
            Permission.INTERNET,
            Permission.RECORD_AUDIO,
            Permission.MODIFY_AUDIO_SETTINGS,
            Permission.ACCESS_NETWORK_STATE
        ])
        self.layout = BoxLayout()
        self.create_webview()
        return self.layout

    @run_on_ui_thread
    def create_webview(self):
        webview = WebView(Activity)
        
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)
        settings.setMediaPlaybackRequiresUserGesture(False)
        
        webview.setWebViewClient(WebViewClient())
        webview.setWebChromeClient(CustomWebChromeClient())
        
        webview.loadDataWithBaseURL(None, CYBERPUNK_HTML, "text/html", "utf-8", None)
        Activity.setContentView(webview)

if __name__ == '__main__':
    CyberpunkAIApp().run()
