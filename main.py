import threading
import traceback
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

# एंड्रॉइड परमिशन और मॉड्यूल्स को सुरक्षित तरीके से लोड करना
try:
    from android.permissions import request_permissions, Permission
    ANDROID_MODE = True
except ImportError:
    ANDROID_MODE = False

# मॉड्यूल्स को सेफ इम्पोर्ट करना ताकि ऐप कभी क्रैश न हो
try:
    from voice_engine import VoiceEngine
except Exception:
    VoiceEngine = None

try:
    from gemini_brain import LiveMatrixBrain
except Exception:
    LiveMatrixBrain = None

try:
    from trading_module import TradingMarketBrain
except Exception:
    TradingMarketBrain = None

try:
    from command_daemon import CommandDaemon
except Exception:
    CommandDaemon = None


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
            text: "[b]STATUS: STABLE MATRIX ONLINE[/b]"
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
            if ANDROID_MODE:
                request_permissions([
                    Permission.INTERNET,
                    Permission.RECORD_AUDIO,
                    Permission.ACCESS_NETWORK_STATE,
                    Permission.MODIFY_AUDIO_SETTINGS
                ])
        except Exception:
            pass
        
        # वॉइस इंजन को सुरक्षित रूप से इनिशियलाइज करना
        try:
            if VoiceEngine:
                self.voice = VoiceEngine()
            else:
                self.voice = None
        except Exception:
            self.voice = None
            
        return MainScreen()

    def on_start(self):
        welcome_text = "Tactical Neural Matrix online, Boss. System is secure."
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
        try:
            self.root.ids.chat_layout.add_widget(lbl)
        except Exception:
            pass
        
        # वॉइस स्पीच को बैकग्राउंड में चलाना ताकि ऐप हैंग न हो
        if is_ai and self.voice:
            try:
                threading.Thread(target=self.voice.speak, args=(text,)).start()
            except Exception:
                pass

    def send_message(self):
        try:
            text_input = self.root.ids.user_input
            text = text_input.text.strip()
            if text:
                self.add_message(text, is_ai=False)
                text_input.text = ""
                threading.Thread(target=self.process_router, args=(text,)).start()
        except Exception as e:
            self.add_message(f"Input Error: {str(e)}", is_ai=True)

    def process_router(self, query):
        try:
            q_lower = query.lower()
            response = ""
            
            # /key कमांड से सीधे ऐप के अंदर API Key सेट करने का फीचर
            if query.startswith("/key "):
                if LiveMatrixBrain:
                    key_value = query.replace("/key ", "").strip()
                    success = LiveMatrixBrain.save_api_key(key_value)
                    if success:
                        response = "COMMAND SUCCESS: Gemini API Key securely saved in local storage, Boss!"
                    else:
                        response = "ERROR: Failed to save API Key."
                else:
                    response = "ERROR: Gemini module not loaded."
            elif "trade" in q_lower or "candlestick" in q_lower or "market" in q_lower:
                if TradingMarketBrain:
                    response = TradingMarketBrain.analyze_market_query(query)
                else:
                    response = "Trading module unavailable."
            elif "build" in q_lower or "apk" in q_lower or "termux" in q_lower:
                if CommandDaemon:
                    response = CommandDaemon.execute_command_action(query)
                else:
                    response = "CommandDaemon module unavailable."
            else:
                if LiveMatrixBrain:
                    response = LiveMatrixBrain.process_request(query)
                else:
                    response = "Gemini Brain module unavailable."

            Clock.schedule_once(lambda dt: self.add_message(response, is_ai=True), 0.2)
        except Exception as e:
            err_msg = f"Neural Matrix Core Error -> {str(e)}"
            Clock.schedule_once(lambda dt: self.add_message(err_msg, is_ai=True), 0.2)

    def start_voice_action(self):
        try:
            if self.voice:
                success = self.voice.start_listening()
                if not success:
                    self.add_message("Voice input initialization failed.", is_ai=True)
            else:
                self.add_message("Voice engine not available.", is_ai=True)
        except Exception as e:
            self.add_message(f"Voice Exception: {str(e)}", is_ai=True)

if __name__ == '__main__':
    NeuralMatrixApp().run()
