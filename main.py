from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from android.permissions import request_permissions, Permission
from voice_engine import VoiceEngine
from gemini_brain import LiveMatrixBrain
import threading

# --- Tactical Military Cyberpunk UI Design ---
KV_DESIGN = """
<MainScreen>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    canvas.before:
        Color:
            rgba: 0.02, 0.05, 0.02, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0, 0.8, 0.2, 1
        Line:
            rectangle: (self.x, self.y, self.width, self.height)
            width: 2

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '70dp'
        padding: 4
        canvas.before:
            Color:
                rgba: 0.05, 0.1, 0.05, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: "[b]⚔️ TACTICAL NEURAL MATRIX // LIVE OS ⚔️[/b]"
            markup: True
            font_size: '14sp'
            color: 0, 1, 0.3, 1

        Label:
            text: "[b]STATUS: GEMINI AI LINKED & ACTIVE[/b]"
            markup: True
            font_size: '9sp'
            color: 1, 0.5, 0, 1

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
            background_color: 0.05, 0.05, 0.05, 1
            foreground_color: 0, 1, 0.3, 1
            cursor_color: 0, 1, 0.3, 1
            font_size: '13sp'
            on_text_validate: app.send_message()

        Button:
            text: "EXEC"
            size_hint_x: None
            width: '70dp'
            background_color: 0, 0.6, 0.2, 1
            color: 1, 1, 1, 1
            bold: True
            on_press: app.send_message()

        Button:
            text: "MIC"
            size_hint_x: None
            width: '60dp'
            background_color: 0.8, 0.1, 0.1, 1
            color: 1, 1, 1, 1
            bold: True
            on_press: app.start_voice_action()
"""

Builder.load_string(KV_DESIGN)

class MainScreen(BoxLayout):
    pass

class NeuralMatrixApp(App):
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
        
        self.voice = VoiceEngine()
        return MainScreen()

    def on_start(self):
        welcome_text = "Tactical Neural Matrix online, Boss. Gemini AI is ready."
        Clock.schedule_once(lambda dt: self.add_message(welcome_text, is_ai=True), 1.0)

    def add_message(self, text, is_ai=True):
        prefix = "[MATRIX AI]: " if is_ai else "[BOSS]: "
        full_text = prefix + text
        color = (0, 1, 0.3, 1) if is_ai else (1, 1, 1, 1)
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
            threading.Thread(target=self.voice.speak, args=(text,)).start()

    def send_message(self):
        text_input = self.root.ids.user_input
        text = text_input.text.strip()
        if text:
            self.add_message(text, is_ai=False)
            text_input.text = ""
            # सीधे Gemini Brain को कॉल करेगा और रिप्लाई लाएगा
            threading.Thread(target=self.process_ai_response, args=(text,)).start()

    def process_ai_response(self, query):
        response = LiveMatrixBrain.process_request(query)
        Clock.schedule_once(lambda dt: self.add_message(response, is_ai=True), 0.2)

    def start_voice_action(self):
        success = self.voice.start_listening()
        if success:
            self.add_message("Listening for voice...", is_ai=True)
        else:
            self.add_message("Voice module error.", is_ai=True)

if __name__ == '__main__':
    NeuralMatrixApp().run()
