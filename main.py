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
        # माइक और इंटरनेट की परमिशन मांगें
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
        
        # वेबव्यू सेटिंग्स (JavaScript और Audio/Mic सपोर्ट के लिए)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)
        settings.setMediaPlaybackRequiresUserGesture(False)
        
        webview.setWebViewClient(WebViewClient())
        webview.setWebChromeClient(WebChromeClient())
        
        # यहाँ अपनी वेबसाइट का URL या लोकल सर्वर एड्रेस डालें
        webview.loadUrl('http://127.0.0.1:5000') 
        
        Activity.setContentView(webview)

if __name__ == '__main__':
    CyberpunkAIApp().run()
