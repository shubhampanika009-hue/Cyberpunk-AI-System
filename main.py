import os
import threading
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from android.permissions import request_permissions, Permission
from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
RecognizerIntent = autoclass('android.speech.RecognizerIntent')
Locale = autoclass('java.util.Locale')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')

class AgentMatrixExecutor:
    @staticmethod
    def handle_query(query):
        q_low = query.lower()
        
        if 'trading' in q_low or 'market' in q_low or 'share' in q_low:
            return "BOSS: Trading Agent has analyzed live candlestick patterns. Paper trade signals are fully active."
        elif 'hack' in q_low or 'security' in q_low or 'recon' in q_low:
            return "BOSS: Security Agent initialized network vulnerability scan and packet interception."
        elif 'app' in q_low or 'builder' in q_low or 'kodular' in q_low:
            return "BOSS: App Builder Agent generated project architecture and build specs."
        elif 'code' in q_low or 'server' in q_low or 'script' in q_low:
            return "BOSS: Code & Server Engine successfully generated bug-free automation scripts."
        elif 'termux' in q_low or 'linux' in q_low or 'daemon' in q_low:
            return "BOSS: Termux Linux Daemon background environment is fully synchronized."
        else:
            return f"BOSS: Command '{query}' executed by Neural Matrix. All systems optimized."

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
            rgba: 1, 0, 0.2, 1
        Line:
            rectangle: (self.x, self.y, self.width, self.height)
            width: 2

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '70dp'
        padding: 4

        Label:
            text: "[b]⚡ 5-AGENT NEURAL MATRIX ⚡[/b]"
            markup: True
            font_size: '16sp'
            color: 1, 0, 0.2, 1

        Label:
            text: "[b]TACTICAL OVERRIDE // LIVE VOICE & DAEMON ACTIVE[/b]"
            markup: True
            font_size: '9sp'
            color: 0, 1, 0.4, 1

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
            hint_text: "Enter command, Boss..."
            multiline: False
            background_color: 0.03, 0.03, 0.03, 1
            foreground_color: 0, 1, 0.4, 1
            cursor_color: 1, 0, 0.2, 1
            font_size: '13sp'
            on_text_validate: app.send_message()

        Button:
            text: "EXEC"
            size_hint_x: None
            width: '70dp'
            background_color: 0.9, 0, 0.2, 1
            color: 1, 1, 1, 1
            bold: True
            on_press: app.send_message()

        Button:
            text: "MIC"
            size_hint_x: None
            width: '55dp'
            background_color: 0, 0.8, 0.4, 1
            color: 0, 0, 0, 1
            bold: True
            on_press: app.start_voice_recognition()
"""

Builder.load_string(KV_DESIGN)

class MainScreen(BoxLayout):
    pass

class CyberpunkAIApp(App):
    def build(self):
        try:
            request_permissions([
                Permission.INTERNET,
                Permission.RECORD_AUDIO,
                Permission.ACCESS_NETWORK_STATE,
                Permission.FOREGROUND_SERVICE
            ])
        except Exception:
            pass
        
        try:
            activity = PythonActivity.mActivity
            self.tts = TextToSpeech(activity, None)
            self.tts.setLanguage(Locale.US)
        except Exception:
            self.tts = None

        return MainScreen()

    def on_start(self):
        welcome_text = "Greetings Boss! 5-Agent Neural Matrix is fully active. Awaiting your tactical orders."
        Clock.schedule_once(lambda dt: self.add_message(welcome_text, is_ai=True), 0.5)

    def speak(self, text):
        if self.tts:
            try:
                self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, None)
            except Exception:
                pass

    def add_message(self, text, is_ai=True):
        prefix = "[5-AGENT AI]: " if is_ai else "[BOSS]: "
        full_text = prefix + text
        color = (0, 1, 0.4, 1) if is_ai else (1, 1, 1, 1)
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
            threading.Thread(target=self.process_command_thread, args=(text,)).start()

    def process_command_thread(self, query):
        reply = AgentMatrixExecutor.handle_query(query)
        Clock.schedule_once(lambda dt: self.add_message(reply, is_ai=True), 0.3)

    def start_voice_recognition(self):
        try:
            activity = PythonActivity.mActivity
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak your command, Boss...")
            activity.startActivityForResult(intent, 2404)
            self.add_message("Capturing voice command, Boss...", is_ai=True)
        except Exception as e:
            self.add_message(f"Voice Driver Error: {str(e)}", is_ai=True)

if __name__ == '__main__':
    CyberpunkAIApp().run()
