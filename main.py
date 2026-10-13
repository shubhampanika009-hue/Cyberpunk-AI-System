from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
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
                Permission.ACCESS_NETWORK_STATE
            ])
        except Exception:
            pass

        # मुख्य लेआउट (डार्क मिलिट्री ब्लैक बैकग्राउंड)
        root = BoxLayout(orientation='vertical', padding=12, spacing=10)
        
        # बैकग्राउंड कलर काला सेट करना
        with root.canvas.before:
            Color(0.01, 0.01, 0.01, 1)
            self.bg_rect = Rectangle(size=(1000, 2000), pos=(0, 0))
        root.bind(size=self._update_bg, pos=self._update_bg)

        # हेडर सेक्शन (मिलिट्री रेड और ग्रीन थीम)
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=75, padding=4)
        title_label = Label(text="[b]⚡ HARDCORE MIL-SPEC AI ⚡[/b]", markup=True, font_size=16, color=(1, 0, 0.2, 1))
        subtitle_label = Label(text="[b]UNRESTRICTED // BACKGROUND DAEMON ACTIVE[/b]", markup=True, font_size=8, color=(0, 1, 0.4, 1))
        header.add_widget(title_label)
        header.add_widget(subtitle_label)
        root.add_widget(header)
        
        # चैट बॉक्स (स्क्रॉल करने योग्य)
        self.chat_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=8, padding=5)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.chat_layout)
        root.add_widget(scroll)
        
        # शुरुआती सिस्टम मैसेज
        self.add_message("[MIL-SPEC SYSTEM]: हार्डकोर न्यूरल मैट्रिक्स सक्रिय है, राजा। बैकग्राउंड लिंक तैयार है!", is_ai=True)
        
        # इनपुट और बटन पैनल (टेक्स्ट इनपुट, EXEC और MIC बटन)
        input_panel = BoxLayout(size_hint_y=None, height=50, spacing=8)
        self.text_input = TextInput(
            hint_text="मिलिट्री-ग्रेड कमांड दर्ज करें...", 
            multiline=False, 
            background_color=(0.03, 0.03, 0.03, 1), 
            foreground_color=(0, 1, 0.4, 1)
        )
        
        send_btn = Button(
            text="EXEC", 
            size_hint_x=None, 
            width=70, 
            background_color=(0.8, 0, 0.2, 1)
        )
        send_btn.bind(on_press=self.send_message)

        mic_btn = Button(
            text="🎙️", 
            size_hint_x=None, 
            width=60, 
            background_color=(0, 0.8, 0.4, 1)
        )
        mic_btn.bind(on_press=self.start_voice_recognition)
        
        input_panel.add_widget(self.text_input)
        input_panel.add_widget(send_btn)
        input_panel.add_widget(mic_btn)
        root.add_widget(input_panel)
        
        return root

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def add_message(self, text, is_ai=True):
        color = (0, 1, 0.4, 1) if is_ai else (1, 1, 1, 1)
        prefix = "AI: " if is_ai else "Raja: "
        lbl = Label(
            text=prefix + text, 
            font_size=13, 
            color=color, 
            size_hint_y=None, 
            text_size=(320, None),
            halign='left',
            valign='middle'
        )
        lbl.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1] + 15))
        self.chat_layout.add_widget(lbl)

    def send_message(self, instance):
        text = self.text_input.text.strip()
        if text:
            self.add_message(text, is_ai=False)
            self.text_input.text = ""
            Clock.schedule_once(lambda dt: self.add_message(f"[EXECUTION]: {text} के लिए मिलिट्री पाबंदियां हटा दी गई हैं।", is_ai=True), 0.4)

    def start_voice_recognition(self, instance):
        try:
            activity = PythonActivity.mActivity
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "hi-IN")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "मिलिट्री कमांड बोलिए...")
            activity.startActivityForResult(intent, 2404)
            self.add_message("[MIC]: वॉइस कमांड रिकॉर्ड हो रहा है...", is_ai=True)
        except Exception as e:
            self.add_message(f"[ERROR]: वॉइस इंजन शुरू नहीं हुआ: {str(e)}", is_ai=True)

if __name__ == '__main__':
    CyberpunkAIApp().run()
