import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# साइबबरपंक थीम के लिए डार्क बैकग्राउंड सेट करना
Window.clearcolor = (0.05, 0.05, 0.1, 1)

class CyberpunkAIApp(App):
    def build(self):
        # मुख्य वर्टिकल लेआउट
        layout = BoxLayout(orientation='vertical', padding=15, spacing=12)
        
        # एडवांस्ड हेडर टाइटल (साइबरपंक स्टाइल)
        self.title_label = Label(
            text="[b][color=00ffcc]⚡ CYBERPUNK AI COMMAND CENTER ⚡[/color][/b]",
            markup=True,
            font_size='20sp',
            size_hint_y=None,
            height=45,
            halign='center'
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        layout.add_widget(self.title_label)
        
        # आउटपुट कंसोल के लिए स्क्रॉलव्यू
        self.scroll = ScrollView(size_hint=(1, 0.65), do_scroll_x=False)
        
        self.output_label = Label(
            text="[color=00ff99]>> System Initialized Successfully.\n>> AI Core Online. Ready for multi-agent execution.\n>> Type commands below (e.g., hack, trade, termux, status).[/color]",
            markup=True,
            valign='top',
            halign='left',
            font_size='14sp'
        )
        self.output_label.bind(size=self.output_label.setter('text_size'))
        self.scroll.add_widget(self.output_label)
        layout.add_widget(self.scroll)
        
        # यूजर इनपुट टेक्स्ट बॉक्स
        self.input_box = TextInput(
            text='',
            hint_text='Enter command here...',
            hint_text_color=(0.5, 0.5, 0.5, 1),
            size_hint_y=None,
            height=50,
            multiline=False,
            background_color=(0.1, 0.1, 0.18, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 1, 0.8, 1)
        )
        self.input_box.bind(on_text_validate=self.execute_command_event)
        layout.add_widget(self.input_box)
        
        # बटन लेआउट (रन और क्लियर)
        btn_layout = BoxLayout(size_hint_y=None, height=55, spacing=15)
        
        run_btn = Button(
            text='[b]RUN COMMAND[/b]',
            markup=True,
            background_color=(0, 0.7, 0.7, 1),
            color=(1, 1, 1, 1)
        )
        run_btn.bind(on_press=self.execute_command_event)
        btn_layout.add_widget(run_btn)
        
        clear_btn = Button(
            text='[b]CLEAR[/b]',
            markup=True,
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        clear_btn.bind(on_press=self.clear_screen)
        btn_layout.add_widget(clear_btn)
        
        layout.add_widget(btn_layout)
        return layout

    def execute_command_event(self, instance):
        cmd = self.input_box.text.strip().lower()
        if not cmd:
            return
            
        response = f"\n\n[color=ff00ff]> {cmd}[/color]\n"
        if cmd == 'exit':
            response += "[color=ff5555]Session terminated safely, Raja.[/color]"
        elif 'hack' in cmd or 'scan' in cmd:
            response += "[color=ffaa00][Agent 3 - Hacking]: Executing vulnerability & port scan protocols...[/color]"
        elif 'trade' in cmd or 'market' in cmd:
            response += "[color=00ff00][Agent 4 - Trading]: Fetching live stock analytics & trends...[/color]"
        elif 'termux' in cmd or 'automation' in cmd:
            response += "[color=00bfff][Agent 2 - Termux]: Executing background automation scripts...[/color]"
        elif 'code' in cmd or 'git' in cmd:
            response += "[color=ffff00][Agent 5 - Dev]: Managing repository code modules...[/color]"
        else:
            response += f"[color=00ffff][Agent 1 - Master]: Processing command -> '{cmd}' successfully.[/color]"
            
        self.output_label.text += response
        self.input_box.text = ''
        
        # आटोमेटिक नीचे स्क्रॉल करने के लिए
        self.scroll.scroll_y = 0

    def clear_screen(self, instance):
        self.output_label.text = "[color=00ff99]>> Console cleared. Ready for next command.[/color]"

if __name__ == '__main__':
    CyberpunkAIApp().run()
