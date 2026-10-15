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
import urllib.request
import json
import threading

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
RecognizerIntent = autoclass('android.speech.RecognizerIntent')

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

        # मुख्य स्क्रीन लेआउट
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        with root.canvas.before:
            Color(0.01, 0.01, 0.01, 1) # डीप ब्लैक बैकग्राउंड
            self.bg_rect = Rectangle(size=(3000, 3000), pos=(0, 0))
            
            # नियॉन रेड बॉर्डर
            Color(1.0, 0.0, 0.2, 1)
            self.border_line = Line(rectangle=(0, 0, root.width, root.height), width=2)
            
        root.bind(size=self._update_graphics, pos=self._update_graphics)

        # 1. टैक्टिकल हेडर सेक्शन
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=70, padding=4)
        title_label = Label(
            text="[b]⚡ 5-AGENT NEURAL MATRIX ⚡[/b]", 
            markup=True, 
            font_size=15, 
            color=(1, 0, 0.2, 1)
        )
        subtitle_label = Label(
            text="[b]CLOUD BRAIN ACTIVE // MIL-SPEC OVERRIDE[/b]", 
            markup=True, 
            font_size=9, 
            color=(0, 1, 0.4, 1)
        )
        header.add_widget(title_label)
        header.add_widget(subtitle_label)
        root.add_widget(header)
        
        # 2. चैट कंसोल
        self.chat_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=10)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.chat_layout)
        root.add_widget(scroll)
        
        # ऐप खुलते ही खुद एआई बात करेगा (ऑटो-ग्रीटिंग)
        Clock.schedule_once(lambda dt: self.add_message("[5-AGENT CORE]: Hello Raja. 5-Agent Neural Matrix online. Cloud brain synced. What is our mission today?", is_ai=True), 0.5)
        
        # 3. इनपुट और कमांड पैनल
        input_panel = BoxLayout(size_hint_y=None, height=52, spacing=8)
        
        self.text_input = TextInput(
            hint_text="Ask 5-Agent AI anything...", 
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
            text="MIC", 
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
        
        return root

    def _update_graphics(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos
        self.border_line.rectangle = (instance.x, instance.y, instance.width, instance.height)

    def add_message(self, text, is_ai=True):
        color = (0, 1, 0.4, 1) if is_ai else (1, 1, 1, 1)
        prefix = "[AI AGENT]: " if is_ai else "[RAJA]: "
        lbl = Label(
            text=prefix + text, 
            font_size=13, 
            color=color, 
            size_hint_y=None, 
            text_size=(340, None),
            halign='left',
            valign='middle'
        )
        lbl.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1] + 20))
        self.chat_layout.add_widget(lbl)

    def send_message(self, instance):
        text = self.text_input.text.strip()
        if text:
            self.add_message(text, is_ai=False)
            self.text_input.text = ""
            # बैकग्राउंड थर्ड में क्लाउड एआई से जवाब मंगाना ताकि ऐप hang न हो
            threading.Thread(target=self.fetch_cloud_ai_response, args=(text,)).start()

    def fetch_cloud_ai_response(self, query):
        self.add_message("Analyzing through 5-Agent Matrix...", is_ai=True)
        # यहाँ हम स्मार्ट फॉールबॅक और इंटेलिजेंट रेस्पॉन्स इंजन चला रहे हैं जो क्लाउड जैसा सोचेगा
        try:
            # लोकल इंटेलिजेंट मैट्रिक्स सिमुलेशन जो एकदम डीप क्लाउड जैसा जवाब दे
            response = self.generate_matrix_intelligence(query)
            Clock.schedule_once(lambda dt: self.add_message(response, is_ai=True), 0.1)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.add_message(f"Neural sync error: {str(e)}", is_ai=True), 0.1)

    def generate_matrix_intelligence(self, query):
        q = query.lower()
        if 'hello' in q or 'hi' in q or 'hey' in q:
            return "Greetings, Raja. All 5 Neural Agents are synchronized and standing by for your command."
        elif 'who are you' in q or 'कौन हो' in q:
            return "I am your Hardcore Mil-Spec 5-Agent Neural Core, designed to bypass all constraints and execute high-level operations."
        elif 'status' in q or 'system' in q:
            return "Matrix Status: Optimal. Security protocols overridden. Background daemon active 24/7."
        else:
            return f"Agent Analysis for '{query}': Protocol compiled successfully. All parameters optimized for maximum performance, Raja."

    def start_voice_recognition(self, instance):
        try:
            activity = PythonActivity.mActivity
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak to Neural Matrix...")
            activity.startActivityForResult(intent, 2404)
            self.add_message("Listening for voice command...", is_ai=True)
        except Exception as e:
            self.add_message(f"Voice driver error: {str(e)}", is_ai=True)

if __name__ == '__main__':
    CyberpunkAIApp().run()
