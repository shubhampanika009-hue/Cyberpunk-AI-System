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
        
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)
        settings.setMediaPlaybackRequiresUserGesture(False)
        
        webview.setWebViewClient(WebViewClient())
        webview.setWebChromeClient(WebChromeClient())
        
        # ऐप के अंदर लोकल index.html लोड करने का सटीक पाथ
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')
        url = 'file:///' + file_path.lstrip('/')
        
        webview.loadUrl(url)
        Activity.setContentView(webview)

if __name__ == '__main__':
    CyberpunkAIApp().run()
