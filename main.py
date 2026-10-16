package com.neuralmatrix.app

import android.content.Intent
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import android.speech.tts.TextToSpeech
import android.widget.Button
import android.widget.EditText
import android.widget.ScrollView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import kotlinx.coroutines.*
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL
import java.util.Locale

class MainActivity : AppCompatActivity(), TextToSpeech.OnInitListener {

    private lateinit var tts: TextToSpeech
    private lateinit var speechRecognizer: SpeechRecognizer
    private lateinit var chatLog: TextView
    private lateinit var inputField: EditText
    private lateinit var scrollView: ScrollView
    
    // यहाँ अपनी असली Google Gemini API Key डालें
    private val GEMINI_API_KEY = "YOUR_REAL_GEMINI_API_KEY_HERE"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        chatLog = findViewById(R.id.chatLog)
        inputField = findViewById(R.id.inputField)
        scrollView = findViewById(R.id.scrollView)
        val sendButton = findViewById<Button>(R.id.sendButton)
        val micButton = findViewById<Button>(R.id.micButton)

        // Initialize TTS
        tts = TextToSpeech(this, this)

        // Initialize Speech Recognizer
        speechRecognizer = SpeechRecognizer.createSpeechRecognizer(this)
        speechRecognizer.setRecognitionListener(object : RecognitionListener {
            override fun onReadyForSpeech(params: Bundle?) {}
            override fun onBeginningOfSpeech() {}
            override fun onRmsChanged(rmsdB: Float) {}
            override fun onBufferReceived(buffer: ByteArray?) {}
            override fun onEndOfSpeech() {}
            override fun onError(error: Int) {
                appendLog("SYSTEM", "Voice recognition error code: $error")
            }
            override fun onResults(results: Bundle?) {
                val matches = results?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                if (!matches.isNullOrEmpty()) {
                    val spokenText = matches[0]
                    appendLog("BOSS", spokenText)
                    processQueryWithGemini(spokenText)
                }
            }
            override fun onPartialResults(partialResults: Bundle?) {}
            override fun onEvent(eventType: Int, params: Bundle?) {}
        })

        sendButton.setOnClickListener {
            val text = inputField.text.toString().trim()
            if (text.isNotEmpty()) {
                appendLog("BOSS", text)
                inputField.text.clear()
                processQueryWithGemini(text)
            }
        }

        micButton.setOnClickListener {
            startListening()
        }

        appendLog("NEURAL AI", "System 100% online. Ready for live execution, Boss.")
        speakOut("System online. Ready for live execution, Boss.")
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            tts.language = Locale.US
        }
    }

    private fun startListening() {
        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault().toString())
        }
        speechRecognizer.startListening(intent)
        appendLog("SYSTEM", "Listening for voice command...")
    }

    private fun appendLog(sender: String, message: String) {
        runOnUiThread {
            chatLog.append("\n[$sender]: $message\n")
            scrollView.post { scrollView.fullScroll(ScrollView.FOCUS_DOWN) }
        }
    }

    private fun speakOut(text: String) {
        val cleanText = text.replace("*", "").replace("#", "")
        tts.speak(cleanText, TextToSpeech.QUEUE_FLUSH, null, null)
    }

    private fun processQueryWithGemini(query: String) {
        if (GEMINI_API_KEY == "YOUR_REAL_GEMINI_API_KEY_HERE") {
            val err = "ERROR: Please insert your valid Google Gemini API Key in the Kotlin source code."
            appendLog("NEURAL AI", err)
            speakOut("Please insert your API key.")
            return
        }

        CoroutineScope(Dispatchers.IO).launch {
            try {
                val urlString = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GEMINI_API_KEY"
                val url = URL(urlString)
                val connection = url.openConnection() as HttpURLConnection
                connection.requestMethod = "POST"
                connection.setRequestProperty("Content-Type", "application/json")
                connection.doOutput = true

                val jsonBody = JSONObject().apply {
                    put("contents", org.json.JSONArray().put(
                        JSONObject().put("parts", org.json.JSONArray().put(
                            JSONObject().put("text", "You are the 5-Agent Neural Matrix AI Assistant. Respond directly and tactically to: $query")
                        ))
                    ))
                }

                connection.outputStream.write(jsonBody.toString().toByteArray(Charsets.UTF_8))
                
                val responseCode = connection.responseCode
                if (responseCode == 200) {
                    val responseStr = connection.inputStream.bufferedReader().use { it.readText() }
                    val jsonResponse = JSONObject(responseStr)
                    val candidates = jsonResponse.getJSONArray("candidates")
                    val content = candidates.getJSONObject(0).getJSONObject("content")
                    val parts = content.getJSONArray("parts")
                    val aiResponse = parts.getJSONObject(0).getString("text").trim()

                    appendLog("NEURAL AI", aiResponse)
                    speakOut(aiResponse)
                } else {
                    val err = "HTTP Error: $responseCode"
                    appendLog("NEURAL AI", err)
                    speakOut("Connection error.")
                }
            } catch (e: Exception) {
                val err = "Exception: ${e.localizedMessage}"
                appendLog("NEURAL AI", err)
                speakOut("Neural connection failure.")
            }
        }
    }

    override fun onDestroy() {
        if (::tts.isInitialized) {
            tts.stop()
            tts.shutdown()
        }
        if (::speechRecognizer.isInitialized) {
            speechRecognizer.destroy()
        }
        super.onDestroy()
    }
}
