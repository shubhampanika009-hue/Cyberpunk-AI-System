from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from android.permissions import request_permissions, Permission

# --- Tactical Army / Cyberpunk UI Design ---
KV_DESIGN = """
<MainScreen>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    canvas.before:
        Color:
            rgba: 0.02, 0.05, 0.02, 1  # Dark Military Tactical Green/Black Background
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0, 0.8, 0.2, 1  # Neon Military Green Border
        Line:
            rectangle: (self.x, self.y, self.width, self.height)
            width: 2

    # Top Header Status Bar
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
            text: "[b]⚔️ TACTICAL NEURAL MATRIX // V1.0 ⚔️[/b]"
            markup: True
            font_size: '14sp'
            color: 0, 1, 0.3, 1

        Label:
            text: "[b]STATUS: FRONT-END SECURE // AWAITING MODULE LINK[/b]"
            markup: True
            font_size: '9sp'
            color: 1, 0.5, 0, 1

    # Main Chat / Display Screen Area
    ScrollView:
        size_hint: (1, 1)
        BoxLayout:
            id: chat_layout
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: 10
            padding: 10

    # Bottom Control Panel (Input, Send, Mic)
    BoxLayout:
        size_hint_y: None
        height: '52dp'
        spacing: 8

        TextInput:
            id: user_input
            hint_text: "Enter tactical command, Boss..."
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

class TacticalFrontEndApp(App):
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
        return MainScreen()

    def on_start(self):
        welcome_text = "Tactical Front-End online, Boss. Ready to integrate modules."
        Clock.schedule_once(lambda dt: self.add_message(welcome_text, is_system=True), 1.0)

    def add_message(self, text, is_system=True):
        prefix = "[SYSTEM]: " if is_system else "[BOSS]: "
        full_text = prefix + text
        color = (0, 1, 0.3, 1) if is_system else (1, 1, 1, 1)
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

    def send_message(self):
        text_input = self.root.ids.user_input
        text = text_input.text.strip()
        if text:
            self.add_message(text, is_system=False)
            text_input.text = ""
            # यहाँ बाद में हम gemini_brain और agents मॉड्यूल जोड़ेंगे

    def start_voice_action(self):
        self.add_message("Voice module pending linkage...", is_system=True)

if __name__ == '__main__':
    TacticalFrontEndApp().run()
