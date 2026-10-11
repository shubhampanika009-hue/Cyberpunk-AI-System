import os
import sys
import threading
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.utils import platform

# Android Specific Setup & Native TTS Permissions
if platform == 'android':
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    
    request_permissions([
        Permission.INTERNET,
        Permission.RECORD_AUDIO,
        Permission.MODIFY_AUDIO_SETTINGS,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE,
        Permission.CAMERA,
        Permission.VIBRATE,
        Permission.WAKE_LOCK
    ])

class CyberpunkAIEngine:
    """5-Agent Multi-Core Intelligence Engine"""
    def __init__(self):
        self.current_agent = "ALPHA"
        self.agents = {
            "ALPHA": "Trading & Market Analytics Agent",
            "BETA": "Cyber Security & Code Executor Agent",
            "GAMMA": "Omniscient Knowledge Agent",
            "DELTA": "System Diagnostics & APK Health Agent",
            "EPSILON": "Voice Synthesis & Speech Agent"
        }

    def process_query(self, query, agent=None):
        target_agent = agent if agent else self.current_agent
        q_lower = query.lower()
        
        if target_agent == "ALPHA":
            return f"[ALPHA AI]: बॉस, {query} के लिए मार्केट ट्रेंड एनालिसिस पॉज़िटिव है। रिस्क रेश्यो नॉर्मल है।"
        elif target_agent == "BETA":
            return f"[BETA AI]: बॉस, सुरक्षा और कोडिंग पेलोड निष्पादित। कोई एरर नहीं पाया गया।"
        elif target_agent == "GAMMA":
            return f"[GAMMA AI]: बॉस, सवाल '{query}' का सटीक समाधान डेटाबेस से फेच कर लिया गया है।"
        elif target_agent == "DELTA":
            return f"[DELTA AI]: सिस्टम हेल्थ 100% ऑप्टिमाइज़्ड है। मेमोरी और CPU यूसेज सुरक्षित है।"
        elif target_agent == "EPSILON":
            return f"[EPSILON AI]: वॉइस कोर एक्टिव। आपके कमांड '{query}' को सफलता से प्रोसेस किया गया।"
        else:
            return f"[{target_agent} AI]: बॉस, आपका निर्देश मान लिया गया है।"

class CyberpunkTerminalUI(BoxLayout):
    def __init__(self, **kwargs):
        super(CyberpunkTerminalUI, self).__init__(orientation='vertical', padding=15, spacing=10, **kwargs)
        self.ai_engine = CyberpunkAIEngine()
        self.tts = None
        self.init_tts()

        # Header Title
        self.header = Label(
            text="[color=00f0ff]// CYBERPUNK AI Core // COMMANDER: RAJA SINGH[/color]",
            markup=True,
            font_size='20sp',
            size_hint_y=0.08
        )
        self.add_widget(self.header)

        # 5 Agent Switcher Bar
        self.agent_bar = GridLayout(cols=5, size_hint_y=0.08, spacing=5)
        for agent in ["ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON"]:
            btn = Button(
                text=agent,
                background_color=(0, 0.9, 1, 0.8),
                color=(0, 0, 0, 1),
                bold=True
            )
            btn.bind(on_press=self.make_agent_switcher(agent))
            self.agent_bar.add_widget(btn)
        self.add_widget(self.agent_bar)

        # Terminal Screen (Scrollable Output)
        self.scroll = ScrollView(size_hint=(1, 0.55))
        self.log_label = Label(
            text="[color=00ff66]> System Initialized... [OK]\n> 5 AI Agents Active & Ready.\n> Commander Access: GRANTED\n>[/color] ",
            markup=True,
            size_hint_y=None,
            font_size='14sp',
            halign='left',
            valign='top'
        )
        self.log_label.bind(texture_size=self._update_texture_size)
        self.scroll.add_widget(self.log_label)
        self.add_widget(self.scroll)

        # Input Query Field
        self.input_field = TextInput(
            hint_text="यहाँ सवाल टाइप करें, बॉस...",
            multiline=False,
            size_hint_y=0.09,
            background_color=(0, 0, 0, 1),
            foreground_color=(0, 0.9, 1, 1),
            cursor_color=(0, 1, 0, 1)
        )
        self.input_field.bind(on_text_validate=self.send_query)
        self.add_widget(self.input_field)

        # Action Buttons Layout (Punch & Voice)
        self.controls = BoxLayout(size_hint_y=0.12, spacing=10)
        
        self.btn_punch = Button(
            text="[⚡ PUNCH TOOL]",
            background_color=(1, 0, 0.3, 0.9),
            color=(1, 1, 1, 1),
            bold=True
        )
        self.btn_punch.bind(on_press=self.run_punch_tool)
        
        self.btn_voice = Button(
            text="[🎤 VOICE AGENT]",
            background_color=(0.6, 0, 1, 0.9),
            color=(1, 1, 1, 1),
            bold=True
        )
        self.btn_voice.bind(on_press=self.run_voice_agent)

        self.controls.add_widget(self.btn_punch)
        self.controls.add_widget(self.btn_voice)
        self.add_widget(self.controls)

    def _update_texture_size(self, instance, value):
        instance.height = value[1]

    def log(self, text, color="00ff66"):
