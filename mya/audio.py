from __future__ import annotations

import logging

import pyttsx3
import speech_recognition as sr

from .config import Settings

LOGGER = logging.getLogger(__name__)


class Speaker:
    def __init__(self, rate: int = 165) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)

    def say(self, message: str) -> None:
        print(f"MYA: {message}")
        self.engine.say(message)
        self.engine.runAndWait()


class MicrophoneListener:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = settings.dynamic_energy_threshold

    def listen(self) -> str | None:
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=self.settings.ambient_duration)
            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=self.settings.listen_timeout,
                    phrase_time_limit=self.settings.phrase_time_limit,
                )
                return self.recognizer.recognize_google(audio).strip()
            except sr.WaitTimeoutError:
                LOGGER.info("No speech detected")
            except sr.UnknownValueError:
                LOGGER.info("Speech was not understood")
            except sr.RequestError as exc:
                LOGGER.warning("Speech service unavailable: %s", exc)
        return None
