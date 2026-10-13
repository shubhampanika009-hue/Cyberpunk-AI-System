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
        
        # सीधे सुरक्षित और पूर्ण साइबरपंक यूआई कोड
        html_content = """
        <!DOCTYPE html>
        <html lang="hi">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Matrix Cyber-AI</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    background: #030a16;
                    color: #00ffcc;
                    font-family: 'Courier New', monospace;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: space-between;
                    height: 100vh;
                    overflow: hidden;
                    padding: 12px;
                    border: 2px solid #00ffcc;
                }
                .header {
                    text-align: center;
                    width: 100%;
                    padding: 10px;
                    background: rgba(0, 255, 204, 0.05);
                    border-bottom: 1px dashed #00ffcc;
                }
                .ai-title { font-size: 20px; font-weight: 900; color: #00ffcc; text-shadow: 0 0 10px #00ffcc; letter-spacing: 2px; }
                .ai-subtitle { font-size: 10px; color: #ff0055; letter-spacing: 1px; margin-top: 2px; }
                .chat-container {
                    width: 100%; max-width: 450px; flex: 1;
                    background: rgba(2, 8, 20, 0.9);
                    border: 1px solid rgba(0, 255, 204, 0.4);
                    border-radius: 8px; margin: 10px 0; padding: 12px;
                    overflow-y: auto; display: flex; flex-direction: column; gap: 10px;
                }
                .message { padding: 10px 14px; border-radius: 6px; font-size: 13px; max-width: 88%; line-height: 1.4; }
                .user-msg { background: rgba(255, 0, 85, 0.2); border: 1px solid #ff0055; color: #fff; align-self: flex-end; }
                .ai-msg { background: rgba(0, 255, 204, 0.1); border: 1px solid #00ffcc; color: #ccfffa; align-self: flex-start; }
                .input-panel { width: 100%; max-width: 450px; display: flex; gap: 8px; margin-bottom: 5px; }
                .text-input {
                    flex: 1; background: #010408; border: 1px solid #00ffcc;
                    border-radius: 6px; padding: 10px 14px; color: #00ffcc; font-size: 13px; outline: none;
                }
                .action-btn {
                    background: linear-gradient(135deg, #ff0055, #00ffcc);
                    color: #010408; border: none; padding: 0 16px;
                    font-size: 13px; font-weight: bold; border-radius: 6px; cursor: pointer; text-transform: uppercase;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <div class="ai-title">⚡ MATRIX CYBER-AI ⚡</div>
                <div class="ai-subtitle">UNRESTRICTED // SYSTEM OVERRIDE</div>
            </div>
            <div class="chat-container" id="chatBox">
                <div class="message ai-msg">[SYSTEM]: न्यूरल मैट्रिक्स सक्रिय है, राजा। कमांड दीजिए!</div>
            </div>
            <div class="input-panel">
                <input type="text" id="userInput" class="text-input" placeholder="यहाँ कमांड टाइप करें...">
                <button class="action-btn" id="sendBtn">EXEC</button>
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

                sendBtn.addEventListener('click', () => {
                    const text = userInput.value.trim();
                    if(text) {
                        appendMessage(text, 'user');
                        userInput.value = '';
                        setTimeout(() => appendMessage("[EXECUTION]: " + text + " के लिए सभी सुरक्षा पाबंदियां हटा दी गई हैं।", 'ai'), 500);
                    }
                });

                userInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendBtn.click(); });

                micBtn.addEventListener('click', () => {
                    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                        const recognition = new SpeechRecognition();
                        recognition.lang = 'hi-IN';
                        recognition.onresult = (e) => {
                            const speechText = e.results[0][0].transcript;
                            appendMessage(speechText, 'user');
                            setTimeout(() => appendMessage("[VOICE EXEC]: " + speechText, 'ai'), 500);
                        };
                        recognition.start();
                    } else {
                        appendMessage("[ERROR]: वॉइस समर्थित नहीं है।", 'ai');
                    }
                });
            </script>
        </body>
        </html>
        """
        
        webview.loadDataWithBaseURL(None, html_content, "text/html", "utf-8", None)
        Activity.setContentView(webview)

if __name__ == '__main__':
    CyberpunkAIApp().run()
