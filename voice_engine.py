from jnius import autoclass, PythonJavaClass, java_method

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
RecognizerIntent = autoclass('android.speech.RecognizerIntent')
Locale = autoclass('java.util.Locale')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')

class TTSOnInitListener(PythonJavaClass):
    __javainterfaces__ = ['android/speech/tts/TextToSpeech$OnInitListener']
    
    def __init__(self, voice_manager):
        super(TTSOnInitListener, self).__init__()
        self.voice_manager = voice_manager

    @java_method('(I)V')
    def onInit(self, status):
        if status == 0:
            try:
                self.voice_manager.tts.setLanguage(Locale.US)
                self.voice_manager.tts_ready = True
            except Exception:
                pass

class VoiceEngine:
    def __init__(self):
        self.tts_ready = False
        self.tts = None
        try:
            activity = PythonActivity.mActivity
            self.tts_listener = TTSOnInitListener(self)
            self.tts = TextToSpeech(activity, self.tts_listener)
        except Exception:
            pass

    def speak(self, text):
        try:
            if self.tts:
                clean_text = text.replace('*', '').replace('#', '')[:300]
                self.tts.speak(clean_text, TextToSpeech.QUEUE_FLUSH, None, None)
        except Exception:
            pass

    def start_listening(self):
        try:
            activity = PythonActivity.mActivity
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak to Matrix AI, Boss...")
            activity.startActivityForResult(intent, 2404)
            return True
        except Exception:
            return False
