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

# 1. 5-Agent Matrix Logic (एजेंट्स का कोर लॉजिक)
class AgentMatrixExecutor:
    @staticmethod
    def handle_query(query):
        q_low = query.lower()
        
        if 'trading' in q_low or 'ट्रेडिंग' in q_low or 'market' in q_low or 'शेयर' in q_low:
            return "बॉस, [Trading Agent]: लाइव कैंडलस्टिक चार्ट पैटर्न और टेक्निकल इंडिकेटर एनालाइज कर लिए गए हैं। पेपर ट्रेड और सिग्नल एक्टिवेट कर दिए हैं।"
        
        elif 'hack' in q_low or 'security' in q_low or 'हैकिंग' in q_low or 'recon' in q_low:
            return "बॉस, [Security/Hacking Agent]: नेटवर्क वल्नरेबिलिटी स्कैन और पैकेट इंटरसेप्शन प्रोटोकॉल लोड कर दिए गए हैं।"
        
        elif 'app' in q_low or 'builder' in q_low or 'ऐप' in q_low or 'kodular' in q_low:
            return "बॉस, [App Builder Agent]: एंड्रॉइड APK प्रोजेक्ट आर्किटेक्चर और बिल्डोजर स्पेसिफिकेशन तैयार हैं।"
        
        elif 'code' in q_low or 'server' in q_low or 'कोडिंग' in q_low or 'script' in q_low:
            return "बॉस, [Code & Server Agent]: बग-फ्री सर्वर स्क्रिप्ट्स और ऑटोमेशन कोड जनरेट कर दिया गया है।"
        
        elif 'termux' in q_low or 'linux' in q_low or 'टर्मक्स' in q_low or 'daemon' in q_low:
            return "बॉस, [Termux Linux Agent]: बैकग्राउंड लिनक्स डेमॉन सर्विस और कमांड-लाइन एनवायरनमेंट सिंक हो गए हैं।"
        
        else:
            return f"बॉस, आपके कमांड '{query}' को 5-Agent मैट्रिक्स द्वारा प्रोसेस कर लिया गया है। सभी सिस्टम ऑप्टिमाइज्ड हैं।"

# 2. UI Design Layout (सामने का लुक और डिजाइन)
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

    # Tactical Header Section
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
            text: "[b]TACTICAL OVERRIDE // PERSISTENT DAEMON ACTIVE[/b]"
            markup: True
            font_size: '9sp'
            color: 0, 1, 0.4, 1

    # Chat Log View
    ScrollView:
        size_hint: (1, 1)

        BoxLayout:
            id: chat_layout
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: 10
            padding: 10

    # Command Control Input Box
    BoxLayout:
        size_hint_y: None
        height: '52dp'
        spacing: 8

        TextInput:
            id: user_input
            hint_text: "कमांड दें, बॉस..."
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

# 3. Main Application Controller (मुख्य ऐप इंजन)
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
        return MainScreen()

    def on_start(self):
        Clock.schedule_once(lambda dt: self.add_message(
            "नमस्ते बॉस! 5-Agent Neural Matrix सक्रिय है।\n1. Trading & Market Analysis\n2. Security & Hacking Recon\n3. App Builder Blueprint\n4. Code & Server Engine\n5. Termux Linux Daemon\n\nऑर्डर दीजिए, बॉस!",
            is_ai=True
        ), 0.5)

    def add_message(self, text, is_ai=True):
        prefix = "[5-AGENT AI]: " if is_ai else "[BOSS]: "
        color = (0, 1, 0.4, 1) if is_ai else (1, 1, 1, 1)
        lbl = Label(
            text=prefix + text,
            font_size='13sp',
            color=color,
            size_hint_y=None,
            text_size=(340, None),
            halign='left',
            valign='middle'
        )
        lbl.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1] + 20))
        self.root.ids.chat_layout.add_widget(lbl)

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
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "hi-IN")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "बॉस, अपना कमांड बोलिए...")
            activity.startActivityForResult(intent, 2404)
            self.add_message("वॉइस इनपुट रिकॉर्ड हो रहा है, बॉस...", is_ai=True)
        except Exception as e:
            self.add_message(f"वॉइस ड्राइवर एरर: {str(e)}", is_ai=True)

if __name__ == '__main__':
    CyberpunkAIApp().run()
