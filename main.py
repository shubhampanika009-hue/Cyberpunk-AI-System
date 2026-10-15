from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line
from android.permissions import request_permissions, Permission
from jnius import autoclass
import threading
import json

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
RecognizerIntent = autoclass('android.speech.RecognizerIntent')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
Locale = autoclass('java.util.Locale')

class CyberpunkAIApp(App):
    def build(self):
        try:
            request_permissions([
                Permission.INTERNET,
                Permission.RECORD_AUDIO,
                Permission.ACCESS_NETWORK_STATE,
                Permission.FOREGROUND_SERVICE,
                Permission.WAKE_LOCK
            ])
        except Exception:
            pass

        # चैट हिस्ट्री और स्टेट इनिशियलाइजेशन
        self.chat_history = []
        self.daemon_active = True

        # मुख्य स्क्रीन लेआउट (मिलिट्री साइबरपंक थीम)
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        with root.canvas.before:
            Color(0.01, 0.01, 0.01, 1) # डीप ब्लैक बैकग्राउंड
            self.bg_rect = Rectangle(size=(3000, 3000), pos=(0, 0))
            
            # नियॉन रेड बॉर्डर
            Color(1.0, 0.0, 0.2, 1)
            self.border_line = Line(rectangle=(0, 0, root.width, root.height), width=2)
            
        root.bind(size=self._update_graphics, pos=self._update_graphics)

        # 1. टैक्टिकल हेडर और सेटिंग्स बार
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=75, padding=4)
        title_label = Label(
            text="[b]⚡ 5-AGENT NEURAL BRAIN MATRIX ⚡[/b]", 
            markup=True, 
            font_size=15, 
            color=(1, 0, 0.2, 1)
        )
        subtitle_label = Label(
            text="[b]AUTONOMOUS HUMAN BRAIN EMULATION // ACTIVE[/b]", 
            markup=True, 
            font_size=8.5, 
            color=(0, 1, 0.4, 1)
        )
        header.add_widget(title_label)
        header.add_widget(subtitle_label)
        root.add_widget(header)
        
        # 2. चैट कंसोल (हिस्ट्री सपोर्ट के साथ)
        self.chat_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=10)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.chat_layout)
        root.add_widget(scroll)
        
        # ऐप ऑन होते ही ह्यूमन-ब्रेन स्टाइल ऑटो-ग्रीटिंग ("बॉस" संबोधन के साथ)
        Clock.schedule_once(lambda dt: self.ai_speak_and_add("नमस्ते बॉस! 5-Agent Neural Matrix और ऑटोनॉमस बैकग्राउंड ब्रेन पूरी तरह एक्टिव हो चुका है। बताइए, आज ट्रेडिंग, हैकिंग, कोडिंग या टर्मक्स में से कौन सा ऑपरेशन संभालना है, बॉस?"), 0.6)
        
        # 3. इनपुट और कमांड पैनल
        input_panel = BoxLayout(size_hint_y=None, height=52, spacing=8)
        
        self.text_input = TextInput(
            hint_text="ऑर्डर दें, बॉस... (ट्रेडिंग, कोडिंग, हैकिंग, लिनक्स)", 
            multiline=False, 
            background_color=(0.03, 0.03, 0.03, 1), 
            foreground_color=(0, 1, 0.4, 1),
            cursor_color=(1, 0, 0.2, 1),
            font_size=13
        )
        
        send_btn = Button(
            text="EXEC", 
            size_hint_x=None, 
            width=70, 
            background_color=(0.9, 0, 0.2, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        send_btn.bind(on_press=self.send_message)

        mic_btn = Button(
            text="🎙️", 
            size_hint_x=None, 
            width=55, 
            background_color=(0, 0.8, 0.4, 1),
            color=(0, 0, 0, 1),
            bold=True
        )
        mic_btn.bind(on_press=self.start_voice_recognition)
        
        input_panel.add_widget(self.text_input)
        input_panel.add_widget(send_btn)
        input_panel.add_widget(mic_btn)
        root.add_widget(input_panel)
        
        # बैकग्राउंड ऑटोनॉमस थ्रेड शुरू करना (जो सर्वर/ब्रेन में लगातार नई जानकारी सीखेगा)
        threading.Thread(target=self.background_autonomous_daemon, daemon=True).start()

        return root

    def _update_graphics(self, instance, value):
        self.bg_rect.size = instance.
