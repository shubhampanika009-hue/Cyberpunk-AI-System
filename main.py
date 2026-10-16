import os
import threading
import json
import urllib.request
import urllib.error
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from android.permissions import request_permissions, Permission
from jnius import autoclass, PythonJavaClass, java_method

PythonActivity = autoclass('org.ropy.android.PythonActivity') if 'org.ropy.android.PythonActivity' in globals() else autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
RecognizerIntent = autoclass('android.speech.RecognizerIntent')
Locale = autoclass('java.util.Locale')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')

class TTSOnInitListener(PythonJavaClass):
    __javainterfaces__ = ['android/speech/tts/TextToSpeech$OnInitListener']
    
    def __init__(self, app_instance):
        super(TTSOnInitListener, self).__init__()
        self.app_instance = app_instance

    @java_method('(I)V')
    def onInit(self, status):
        if status == 0:
            try:
                self.app_instance.tts.setLanguage(Locale.US)
                self.app_instance.tts_ready = True
            except Exception:
                pass

class RealAIConnector:
    # यहाँ अपनी असली Google Gemini API Key डालें
    API_KEY = "YAHAN_APNI_GEMINI_API_KEY_DALO"
    
    @staticmethod
    def ask_gemini(prompt):
        if RealAIConnector.API_KEY == "YAHAN_APNI_GEMINI_API_KEY_DALO":
            return "ERROR: Boss, please configure your real Google Gemini API Key in the source code to activate live AI intelligence."
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={RealAIConnector.API_KEY}"
        headers = {'Content-Type': 'application/json'}
        data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        try:
            req_data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=req_data, headers=headers, method='POST')
            with urllib.request.urlopen(req, timeout=15) as response:
                res_body = response.read().decode('utf-8')
                res_json = json.loads(res_body)
                # Parse Gemini response structure safely
                answer = res_json['candidates'][0]['content']['parts'][0]['text']
                return answer.strip()
        except urllib.error.HTTPError as e:
            return f"API HTTP Error: {e.code} - Check your API key or network."
        except Exception as e:
            return f"Neural Connection Error: {str(e)}"

KV_DESIGN = """
<MainScreen>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    canvas.before:
        Color:
            rgba: 0.01, 0.01, 0.01, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0, 1, 0.5, 1
        Line:
            rectangle: (self.x, self.y, self.width, self.height)
            width: 2

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '70dp'
        padding: 4

        Label:
            text: "[b]⚡ REAL NEURAL MATRIX // LIVE AI ⚡[/b]"
            markup: True
            font_size: '15sp'
            color: 0, 1, 0.5, 1

        Label:
            text: "[b]STATUS: CONNECTED TO REAL GEMINI ENGINE[/b]"
            markup: True
            font_size: '9sp'
            color: 1, 1, 1, 1

    ScrollView:
        size_hint: (1, 1)

        BoxLayout:
            id: chat_layout
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: 10
            padding: 10

    BoxLayout:
        size_hint_y: None
        height: '52dp'
        spacing: 8

        TextInput:
            id: user_input
            hint_text: "Ask anything, Boss... (Real AI)"
            multiline: False
            background_color: 0.03, 0.03, 0.03, 1
            foreground_color: 0, 1, 0.5, 1
            cursor_color: 0, 1, 0.5, 1
            font_size: '13sp'
            on_text_validate: app.send_message()

        Button:
            text: "SEND"
            size_hint_x: None
            width: '70dp'
            background_color: 0, 0.7, 0.3, 1
            color: 1, 1, 1, 1
            bold: True
            on_press: app.send_message()

        Button:
            text: "MIC"
            size_hint_x: None
            width: '55dp'
            background_color: 0.8, 0, 0.2, 1
            color: 1, 1, 1, 1
            bold: True
            on_press: app.start_voice_recognition()
"""

Builder.load_string(KV_DESIGN)

class MainScreen(BoxLayout):
    pass

class RealAIApp(App):
    def build(self):
        try:
            request_permissions([
                Permission.INTERNET,
                Permission.RECORD_AUDIO,
                Permission.ACCESS_NETWORK_STATE,
                Permission.MODIFY_AUDIO_SETTINGS
            ])
        except Exception:
            pass
        
        self.tts_ready = False
        self.tts = None
        try:
            activity = PythonActivity.mActivity
            self.tts_listener = TTSOnInitListener(self)
            self.tts = TextToSpeech(activity, self.tts_listener)
        except Exception:
            pass

        return MainScreen()

    def on_start(self):
        welcome_text = "Neural Matrix online. Real AI backend linked. Ask me anything, Boss."
        Clock.schedule_once(lambda dt: self.add_message(welcome_text, is_ai=True), 1.0)

    def speak(self, text):
        try:
            if self.tts and self.tts_ready:
                # Speak only clean text (avoiding markdown symbols for TTS)
                clean_txt = text.replace('*', '').replace('#', '')[:300]
                self.tts.speak(clean_txt, TextToSpeech.QUEUE_FLUSH, None, None)
        except Exception:
            pass

    def add_message(self, text, is_ai=True):
        prefix = "[REAL AI]: " if is_ai else "[BOSS]: "
        full_text = prefix + text
        color = (0, 1, 0.5, 1) if is_ai else (1, 1, 1, 1)
        lbl = Label(
            text=full_text,
            font_size='13sp',
            color=color,
            size_hint_y=None,
            text_size=(340, None),
            halign='left',
            valign='middle'
        )
        lbl.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1] + 20))
        self.root.ids.chat_layout.add_widget(lbl)
        
        if is_ai:
            threading.Thread(target=self.speak, args=(text,)).start()

    def send_message(self):
        text_input = self.root.ids.user_input
        text = text_input.text.strip()
        if text:
            self.add_message(text, is_ai=False)
            text_input.text = ""
            threading.Thread(target=self.process_api_thread, args=(text,)).start()

    def process_api_thread(self, query):
        reply = RealAIConnector.ask_gemini(query)
        Clock.schedule_once(lambda dt: self.add_message(reply, is_ai=True), 0.3)

    def start_voice_recognition(self):
        try:
            activity = PythonActivity.mActivity
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak to Real AI, Boss...")
            activity.startActivityForResult(intent, 2404)
            self.add_message("Listening for live voice input...", is_ai=True)
        except Exception as e:
            self.add_message(f"Voice Error: {str(e)}", is_ai=True)

if __name__ == '__main__':
    RealAIApp().run()
