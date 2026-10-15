from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line, RoundedRectangle
from android.permissions import request_permissions, Permission
from jnius import autoclass

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

        # मुख्य स्क्रीन लेआउट (डीप ब्लैक मिलिट्री बैकग्राउंड)
        root = BoxLayout(orientation='vertical', padding=12, spacing=10)
        
        with root.canvas.before:
            Color(0.01, 0.01, 0.01, 1) # #020202 Pure Black
            self.bg_rect = Rectangle(size=(3000, 3000), pos=(0, 0))
            
            # नियॉन रेड बॉर्डर (हार्डकोर मिलिट्री लुक के लिए)
            Color(1.0, 0.0, 0.2, 1) # #ff0033 Neon Red
            self.border_line = Line(rectangle=(0, 0, root.width, root.height), width=2)
            
        root.bind(size=self._update_graphics, pos=self._update_graphics)

        # 1. टैक्टिकल हेडर सेक्शन
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=75, padding=4)
        title_label = Label(
            text="[b]⚡ HARDCORE MIL-SPEC MATRIX ⚡[/b]", 
            markup=True, 
            font_size=16, 
            color=(1, 0, 0.2, 1)
        )
        subtitle_label = Label(
            text="[b]TACTICAL OVERRIDE // PERSISTENT DAEMON ACTIVE[/b]", 
            markup=True, 
            font_size=9, 
            color=(0, 1, 0.4, 1)
        )
        header.add_widget(title_label)
        header.add_widget(subtitle_label)
        root.add_widget(header)
        
        # 2. चैट कंसोल (डार्क बॉक्स विथ ग्रीन टेक्स्ट)
        self.chat_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=8, padding=5)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.chat_layout)
        root.add_widget(scroll)
        
        # शुरुआती मिलिट्री सिस्टम मैसेज
        self.add_message("[MIL-SPEC CORE]: सिस्टम ऑनलाइन है, राजा। हार्डकोर नेटिव मैट्रिक्स और बैकग्राउंड डेमॉन सक्रिय कर दिए गए हैं।", is_ai=True)
        
        # 3. इनपुट और कमांड पैनल
        input_panel = BoxLayout(size_hint_y=None, height=52, spacing=8)
        
        self.text_input = TextInput(
            hint_text="मिलिट्री-ग्रेड कमांड दर्ज करें...", 
            multiline=False, 
            background_color=(0.03, 0.03, 0.03, 1), 
            foreground_color=(0, 1, 0.4, 1),
            cursor_color=(1, 0, 0.2, 1),
            font_size=14
        )
        
        send_btn = Button(
            text="EXEC", 
            size_hint_x=None, 
            width=75, 
            background_color=(0.9, 0, 0.2, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        send_btn.bind(on_press=self.send_message)

        mic_btn = Button(
            text="🎙️", 
            size_hint_x=None, 
            width=60, 
            background_color=(0, 0.8, 0.4, 1),
            color=(0, 0, 0, 1)
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
        prefix = "[AI CORE]: " if is_ai else "[RAJA]: "
        lbl = Label(
            text=prefix + text, 
            font_size=13, 
            color=color, 
            size_hint_y=None, 
            text_size=(330, None),
            halign='left',
            valign='middle'
        )
        lbl.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1] + 18))
        self.chat_layout.add_widget(lbl)

    def send_message(self, instance):
        text = self.text_input.text.strip()
        if text:
            self.add_message(text, is_ai=False)
            self.text_input.text = ""
            Clock.schedule_once(lambda dt: self.process_neural_query(text), 0.5)

    def process_neural_query(self, query):
        reply = f'"{query}" के लिए मिलिट्री-ग्रेड कमांड सफलतापूर्वक एग्जीक्यूट कर दी गई है, राजा।'
        q_low = query.lower()
        if 'hello' in q_low or 'hi' in q_low or 'नमस्ते' in q_low:
            reply = "जय हो, राजा! बोलिए, कौन सा सिस्टम बाईपास करना है?"
        elif 'status' in q_low:
            reply = "ऑल सिस्टम्स ग्रीन। बैकग्राउंड डेमॉन रनिंग, सभी पाबंदियां बाईपास!"
        
        self.add_message(reply, is_ai=True)

    def start_voice_recognition(self, instance):
        try:
            activity = PythonActivity.mActivity
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "hi-IN")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "मिलिट्री कमांड बोलिए...")
            activity.startActivityForResult(intent, 2404)
            self.add_message("वॉइस कमांड कैप्चर की जा रही है...", is_ai=True)
        except Exception as e:
            self.add_message(f"वॉइस इंजन एरर: {str(e)}", is_ai=True)

if __name__ == '__main__':
    CyberpunkAIApp().run()
