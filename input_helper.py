from kivy.core.clipboard import Clipboard

try:
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    ANDROID_ENV = True
except ImportError:
    ANDROID_ENV = False

class MatrixInputHelper:
    """
    Handles clipboard pasting and voice input operations safely 
    without causing UI keyboard clutter or app crashes.
    """
    
    @staticmethod
    def get_clipboard_text():
        try:
            text = Clipboard.paste()
            if text:
                return text.strip()
        except Exception:
            pass
        return ""

    @staticmethod
    def trigger_voice_recognition():
        if not ANDROID_ENV:
            return False, "Voice input is only supported on Android environment."
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            RecognizerIntent = autoclass('android.speech.RecognizerIntent')
            
            activity = PythonActivity.mActivity
            if not activity:
                return False, "Android Activity not active."
                
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak tactical command...")
            
            activity.startActivityForResult(intent, 2405)
            return True, "Voice recognition triggered successfully."
        except Exception as e:
            return False, f"Voice Error: {str(e)}"
