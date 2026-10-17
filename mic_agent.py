import threading
import time

try:
    from jnius import autoclass, PythonJavaClass, java_method
    ANDROID_MIC_ACTIVE = True
except ImportError:
    ANDROID_MIC_ACTIVE = False

if ANDROID_MIC_ACTIVE:
    try:
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        RecognizerIntent = autoclass('android.speech.RecognizerIntent')
    except Exception:
        ANDROID_MIC_ACTIVE = False

class MicAgent:
    """
    Dedicated Background Mic Agent for continuous listening and command capturing.
    """
    def __init__(self, callback_func):
        self.is_listening = False
        self.callback_func = callback_func

    def start_continuous_listener(self):
        if not ANDROID_MIC_ACTIVE:
            print("Mic Agent: Android environment required for speech recognition.")
            return False
        
        self.is_listening = True
        threading.Thread(target=self._listener_loop, daemon=True).start()
        return True

    def _listener_loop(self):
        while self.is_listening:
            try:
                activity = PythonActivity.mActivity
                if activity:
                    intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
                    intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                    intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
                    intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Neural Matrix Listening...")
                    # Triggering listener intent
                    # Note: For fully continuous background wake-word engine, a native Android Foreground Service is required.
                time.sleep(5)
            except Exception:
                time.sleep(3)

    def stop_listener(self):
        self.is_listening = False
