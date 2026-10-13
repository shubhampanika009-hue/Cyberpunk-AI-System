import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from android.permissions import request_permissions, Permission
from android.runnable import run_on_ui_thread
from jnius import autoclass

# Android WebView सेटअप
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
WebChromeClient = autoclass('android.webkit.WebChromeClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class CyberpunkAIApp(App):
    def build(self):
        # माइक, स्टोरेज और इंटरनेट की परमिशन मांगें
        request_permissions([
            Permission.INTERNET,
            Permission.RECORD_AUDIO,
            Permission.MODIFY_AUDIO_SETTINGS,
            Permission.ACCESS_NETWORK_STATE,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE
        ])
        self.layout = BoxLayout()
        self.create_webview()
        return self.layout

    @run_on_ui_thread
    def create_webview(self):
        webview = WebView(Activity)
        
        # वेबव्यू सेटिंग्स (JavaScript, DOM स्टोरेज और ऑडियो/माइक सपोर्ट के लिए)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)
        settings.setMediaPlaybackRequiresUserGesture(False)
        
        webview.setWebViewClient(WebViewClient())
        webview.setWebChromeClient(WebChromeClient())
        
        # लोकल HTML फाइल या ऑनलाइन URL लोड करने का तरीका
        # यह आपके प्रोजेक्ट में मौजूद index.html फाइल को सीधे ऐप के अंदर खोल देगा
        base_path = os.path.dirname(os.path.abspath(__file__))
        index_file = os.path.join(base_path, 'index.html')
        
        if os.path.exists(index_file):
            webview.loadUrl(f'file://{index_file}')
        else:
            # अगर index.html न मिले, तो फॉલबॅक के लिए ऑनलाइन या डिफॉल्ट पेज लोड करें
            webview.loadUrl('https://www.google.com')
        
        Activity.setContentView(webview)

if __name__ == '__main__':
    CyberpunkAIApp().run()
