import threading
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard

try:
    from android.permissions import request_permissions, Permission
    ANDROID_MODE = True
except ImportError:
    ANDROID_MODE = False

try:
    from voice_engine import VoiceEngine
except Exception:
    VoiceEngine = None

try:
    from gemini_brain import LiveMatrixBrain
except Exception:
    LiveMatrixBrain = None


# --- Button-Free Clean Live Neural Interface ---
KV_DESIGN = """
<MainScreen>:
    orientation: 'vertical'
    padding: 15
    spacing: 15
    canvas.before:
        Color:
            rgba: 0.01, 0.02, 0.01, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0, 1, 0.3, 1
        Line:
            rectangle: (self.x, self.y, self.width, self.height)
            width: 2

    # Status Header
    Label:
        id: status_label
        text: "TACTICAL NEURAL MATRIX // LIVE PROCESSING ENGINE"
        size_hint_y: None
        height: '40dp'
        font_size: '13sp'
        color: 0, 1, 0.3, 1
        bold: True

    # Live Real-time Process & Output Display Area
    BoxLayout:
        orientation: 'vertical'
        padding: 12
        canvas.before:
            Color:
                rgba: 0.03, 0.06, 0.03, 1
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: 0, 0.6, 0.2, 1
            Line:
                rectangle: (self.x, self.y, self.width, self.height)
                width: 1

        ScrollView:
            Label:
                id: live_output_label
                text: "Initializing Neural Core...\\nSystem is live and listening to commands.\\nTo configure API Key, paste or type '/key YOUR_API_KEY'."
                markup: True
                font_size: '14sp'
                color: 0, 1, 0.45, 1
                size_hint_y: None
                height: self.texture_size[1] + 30
                halign: 'left'
                valign: 'top'

    # Minimal Command Input (Keyboard only when typing/command given)
    TextInput:
        id: command_input
        hint_text: "Type command or paste text here (Press Enter to execute)..."
        size_hint_y: None
        height: '55dp'
        multiline: False
        background_color: 0.05, 0.05, 0.05, 1
        foreground_color: 0, 1, 0.3, 1
        cursor_color: 0, 1, 0.3, 1
        font_size: '13sp'
        on_text_validate: app.handle_command()
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
        
        try:
            self.voice = VoiceEngine() if VoiceEngine else None
        except Exception:
            self.voice = None
            
        return MainScreen()

    def on_start(self):
        self.update_screen("Neural Core Active, Boss. Ready for execution.", "STATUS: ONLINE & SECURE")
        # Check clipboard automatically on start for any quick copied command/key
        Clock.schedule_once(lambda dt: self.auto_check_clipboard(), 2.0)

    def update_screen(self, log_text, status_str=None):
        def refresh(dt):
            try:
                self.root.ids.live_output_label.text = log_text
                if status_str:
                    self.root.ids.status_label.text = status_str
            except Exception:
                pass
        Clock.schedule_once(refresh, 0.1)

    def auto_check_clipboard(self):
        try:
            clip = Clipboard.paste().strip()
            if clip and (clip.startswith("/key") or len(clip) > 10):
                self.root.ids.command_input.text = clip
                self.update_screen(f"AUTO-LOADED FROM CLIPBOARD:\n{clip}\n\nPress Enter to execute.", "CLIPBOARD SYNCED")
        except Exception:
            pass

    def handle_command(self):
        try:
            cmd = self.root.ids.command_input.text.strip()
            if not cmd:
                return
            self.root.ids.command_input.text = ""
            
            # Show live process steps on screen
            process_steps = f"PROCESSING PIPELINE:\n1. Input Captured: [{cmd}]\n2. Routing to AI Engine...\n3. Fetching Live Response..."
            self.update_screen(process_steps, "STATUS: EXECUTING...")

            threading.Thread(target=self.execute_ai_task, args=(cmd,)).start()
        except Exception as e:
            self.update_screen(f"Error handling command: {str(e)}", "STATUS: ERROR")

    def execute_ai_task(self, query):
        try:
            response = ""
            if query.startswith("/key "):
                if LiveMatrixBrain:
                    key_val = query.replace("/key ", "").strip()
                    success = LiveMatrixBrain.save_api_key(key_val)
                    response = "API Key successfully saved in secure local storage, Boss!" if success else "Failed to save key."
                else:
                    response = "Gemini module missing."
            else:
                if LiveMatrixBrain:
                    response = LiveMatrixBrain.process_request(query)
                else:
                    response = "Gemini Brain module not loaded."

            # Final live display
            final_display = f"COMMAND:\n> {query}\n\nLIVE EXECUTION RESULT:\n{response}"
            self.update_screen(final_display, "STATUS: TASK COMPLETED")

            # Speak output via TTS if available
            if self.voice:
                try:
                    self.voice.speak(response)
                except Exception:
                    pass
        except Exception as e:
            self.update_screen(f"Core Execution Exception:\n{str(e)}", "STATUS: CRITICAL ERROR")

if __name__ == '__main__':
    NeuralMatrixApp().run()
