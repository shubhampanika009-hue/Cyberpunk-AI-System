from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from android.permissions import request_permissions, Permission

class CyberpunkAIApp(App):
    def build(self):
        # एंड्रॉइड परमिशंस लेना
        try:
            request_permissions([
                Permission.INTERNET,
                Permission.RECORD_AUDIO,
                Permission.ACCESS_NETWORK_STATE
            ])
        except Exception:
            pass

        # मुख्य लेआउट (डार्क साइबरपंक थीम)
        root = BoxLayout(orientation='vertical', padding=12, spacing=10)
        
        # हेडर सेक्शन
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=65, padding=4)
        title_label = Label(text="[b]⚡ MATRIX CYBER-AI ⚡[/b]", markup=True, font_size=18, color=(0, 1, 0.8, 1))
        subtitle_label = Label(text="[b]UNRESTRICTED // SYSTEM OVERRIDE[/b]", markup=True, font_size=9, color=(1, 0, 0.33, 1))
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
        self.add_message("[SYSTEM]: न्यूरल मैट्रिक्स सक्रिय है, राजा। कमांड दीजिए!", is_ai=True)
        
        # इनपुट और बटन पैनल
        input_panel = BoxLayout(size_hint_y=None, height=50, spacing=8)
        self.text_input = TextInput(
            hint_text="यहाँ कमांड टाइप करें...", 
            multiline=False, 
            background_color=(0.02, 0.06, 0.12, 1), 
            foreground_color=(0, 1, 0.8, 1)
        )
        
        send_btn = Button(
            text="EXEC", 
            size_hint_x=None, 
            width=80, 
            background_color=(0, 0.8, 0.6, 1)
        )
        send_btn.bind(on_press=self.send_message)
        
        input_panel.add_widget(self.text_input)
        input_panel.add_widget(send_btn)
        root.add_widget(input_panel)
        
        return root

    def add_message(self, text, is_ai=True):
        color = (0.7, 1, 0.9, 1) if is_ai else (1, 0.7, 0.9, 1)
        prefix = "AI: " if is_ai else "Raja: "
        lbl = Label(
            text=prefix + text, 
            font_size=13, 
            color=color, 
            size_hint_y=None, 
            text_size=(340, None),
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
            Clock.schedule_once(lambda dt: self.add_message(f"[EXECUTION]: {text} के लिए सभी सुरक्षा पाबंदियां हटा दी गई हैं।", is_ai=True), 0.4)

if __name__ == '__main__':
    CyberpunkAIApp().run()
