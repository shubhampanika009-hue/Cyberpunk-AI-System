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
            Permission.ACCESS_NETWORK_STATE,
            Permission.FOREGROUND_SERVICE
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
        settings.setJavaScriptCanOpenWindowsAutomatically(True)
        
        webview.setWebViewClient(WebViewClient())
        webview.setWebChromeClient(CustomWebChromeClient())
        
        # हार्डकोर नियॉन रेड/ब्लैक साइबरपंक डिज़ाइन + बैकग्राउंड सर्विस सेटिंग टॉगल
        hardcore_html = """
        <!DOCTYPE html>
        <html lang="hi">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Matrix Cyber-AI Hardcore</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    background-color: #000000;
                    color: #00ff66;
                    font-family: 'Courier New', Courier, monospace;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: space-between;
                    height: 100vh;
                    overflow: hidden;
                    padding: 10px;
                    border: 2px solid #ff0033;
                    box-shadow: inset 0 0 20px rgba(255, 0, 51, 0.4);
                }
                .header {
                    text-align: center;
                    width: 100%;
                    padding: 8px;
                    background: rgba(255, 0, 51, 0.08);
                    border-bottom: 1px solid #ff0033;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    position: relative;
                }
                .ai-title { 
                    font-size: 18px; 
                    font-weight: 900; 
                    color: #ff0033; 
                    text-shadow: 0 0 12px #ff0033; 
                    letter-spacing: 2px; 
                }
                .ai-subtitle { 
                    font-size: 9px; 
                    color: #00ff66; 
                    letter-spacing: 1.5px; 
                    margin-top: 3px; 
                }
                .settings-bar {
                    width: 100%;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    background: rgba(0, 255, 102, 0.05);
                    border: 1px solid rgba(0, 255, 102, 0.3);
                    padding: 6px 12px;
                    border-radius: 4px;
                    margin-top: 6px;
                    font-size: 11px;
                }
                .toggle-switch {
                    position: relative;
                    display: inline-block;
                    width: 36px;
                    height: 20px;
                }
                .toggle-switch input { opacity: 0; width: 0; height: 0; }
                .slider {
                    position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
                    background-color: #111;
                    transition: .3s;
                    border: 1px solid #ff0033;
                    border-radius: 20px;
                }
                .slider:before {
                    position: absolute; content: ""; height: 12px; width: 12px; left: 3px; bottom: 3px;
                    background-color: #ff0033;
                    transition: .3s;
                    border-radius: 50%;
                }
                input:checked + .slider { background-color: rgba(0, 255, 102, 0.3); border-color: #00ff66; }
                input:checked + .slider:before { transform: translateX(16px); background-color: #00ff66; box-shadow: 0 0 8px #00ff66; }

                .chat-container {
                    width: 100%; 
                    max-width: 480px; 
                    flex: 1;
                    background: rgba(5, 5, 5, 0.95);
                    border: 1px solid rgba(0, 255, 102, 0.3);
                    border-radius: 6px; 
                    margin: 8px 0; 
                    padding: 12px;
                    overflow-y: auto; 
                    display: flex; 
                    flex-direction: column; 
                    gap: 10px;
                }
                .message { 
                    padding: 10px 14px; 
                    border-radius: 4px; 
                    font-size: 13px; 
                    max-width: 88%; 
                    line-height: 1.4; 
                }
                .user-msg { 
                    background: rgba(255, 0, 51, 0.15); 
                    border: 1px solid #ff0033; 
                    color: #ffffff; 
                    align-self: flex-end; 
                }
                .ai-msg { 
                    background: rgba(0, 255, 102, 0.08); 
                    border: 1px solid #00ff66; 
                    color: #ccffdd; 
                    align-self: flex-start;
                    box-shadow: 0 0 10px rgba(0, 255, 102, 0.1);
                }
                .input-panel { 
                    width: 100%; 
                    max-width: 480px; 
                    display: flex; 
                    gap: 8px; 
                    margin-bottom: 5px; 
                }
                .text-input {
                    flex: 1; 
                    background: #000000; 
                    border: 1px solid #00ff66;
                    border-radius: 4px; 
                    padding: 10px 16px; 
                    color: #00ff66; 
                    font-size: 13px; 
                    outline: none;
                }
                .text-input::placeholder { color: rgba(0, 255, 102, 0.3); }
                .action-btn {
                    background: linear-gradient(135deg, #ff0033, #99001f);
                    color: #ffffff; 
                    border: none; 
                    padding: 0 16px;
                    font-size: 13px; 
                    font-weight: bold; 
                    border-radius: 4px; 
                    cursor: pointer; 
                    box-shadow: 0 0 10px rgba(255, 0, 51, 0.4);
                    text-transform: uppercase;
                }
                .mic-btn {
                    background: linear-gradient(135deg, #00ff66, #008833);
                    color: #000000; 
                    border: none; 
                    width: 42px;
                    height: 42px;
                    font-size: 16px; 
                    border-radius: 4px; 
                    cursor: pointer; 
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: bold;
                    box-shadow: 0 0 10px rgba(0, 255, 102, 0.4);
                }
            </style>
        </head>
        <body>
            <div class="header">
                <div class="ai-title">⚡ HARDCORE MIL-SPEC AI ⚡</div>
                <div class="ai-subtitle">UNRESTRICTED // SECURE OVERRIDE ACTIVE</div>
                
                <div class="settings-bar">
                    <span>PERSISTENT BACKEND SERVICE</span>
                    <label class="toggle-switch">
                        <input type="checkbox" id="bgToggle" checked>
                        <span class="slider"></span>
                    </label>
                </div>
            </div>
            
            <div class="chat-container" id="chatBox">
                <div class="message ai-msg"><b>[MIL-SPEC SYSTEM]:</b> हार्डकोर न्यूरल मैट्रिक्स और बैकग्राउंड डेमॉन सक्रिय है, राजा। ऐप बंद होने पर भी सर्वर लिंक बना रहेगा।</div>
            </div>
            
            <div class="input-panel">
                <input type="text" id="userInput" class="text-input" placeholder="मिलिट्री-ग्रेड कमांड दर्ज करें...">
                <button class="action-btn" id="sendBtn">EXEC</button>
                <button class="mic-btn" id="micBtn">🎙️</button>
            </div>

            <script>
                const chatBox = document.getElementById('chatBox');
                const userInput = document.getElementById('userInput');
                const sendBtn = document.getElementById('sendBtn');
                const micBtn = document.getElementById('micBtn');
                const bgToggle = document.getElementById('bgToggle');

                bgToggle.addEventListener('change', () => {
                    if(bgToggle.checked) {
                        appendMessage("<b>[DAEMON]:</b> बैकग्राउंड परसिस्टेंट सर्विस इनेबल कर दी गई है।", 'ai');
                    } else {
                        appendMessage("<b>[DAEMON]:</b> बैकग्राउंड सर्विस बंद कर दी गई है।", 'ai');
                    }
                });

                function appendMessage(text, sender) {
                    const msgDiv = document.createElement('div');
                    msgDiv.className = `message ${sender === 'user' ? 'user-msg' : 'ai-msg'}`;
                    msgDiv.innerHTML = text;
                    chatBox.appendChild(msgDiv);
                    chatBox.scrollTop = chatBox.scrollHeight;
                }

                function processNeuralQuery(query) {
                    appendMessage("<b>[AI]:</b> मिलिट्री मैट्रिक्स स्कैनिंग जारी है...", 'ai');
                    let loadingMsg = chatBox.lastChild;

                    setTimeout(() => {
                        chatBox.removeChild(loadingMsg);
                        let responseText = `<b>[EXECUTION RESULT]:</b> "${query}" के लिए मिलिट्री-ग्रेड पाबंदियां बाईपास कर दी गई हैं। सर्वर बैकग्राउंड में सिंक हो रहा है, राजा!`;
                        appendMessage(responseText, 'ai');
                    }, 600);
                }

                sendBtn.addEventListener('click', () => {
                    const text = userInput.value.trim();
                    if(text) {
                        appendMessage(text, 'user');
                        userInput.value = '';
                        processNeuralQuery(text);
                    }
                });

                userInput.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') sendBtn.click();
                });

                micBtn.addEventListener('click', () => {
                    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                        const recognition = new SpeechRecognition();
                        recognition.lang = 'hi-IN';
                        
                        recognition.onstart = () => {
                            appendMessage("<b>[MIC]:</b> मिलिट्री वॉइस कमांड ग्रहण हो रहा है...", 'ai');
                        };
                        
                        recognition.onresult = (event) => {
                            const speechText = event.results[0][0].transcript;
                            appendMessage(speechText, 'user');
                            processNeuralQuery(speechText);
                        };
                        
                        recognition.start();
                    } else {
                        appendMessage("<b>[ERROR]:</b> वॉइस ड्राइवर अनुपलब्ध है।", 'ai');
                    }
                });
            </script>
        </body>
        </html>
        """
        
        webview.loadDataWithBaseURL(None, hardcore_html, "text/html", "utf-8", None)
        Activity.setContentView(webview)

if __name__ == '__main__':
    CyberpunkAIApp().run()
