from __future__ import annotations

import datetime as dt
import re
import webbrowser
from dataclasses import dataclass
from urllib.parse import quote_plus


@dataclass(frozen=True)
class Result:
    reply: str
    should_exit: bool = False


class Assistant:
    def __init__(self, speaker=None, opener=webbrowser.open) -> None:
        self.speaker = speaker
        self.opener = opener

    def handle(self, raw_text: str) -> Result:
        text = re.sub(r"\s+", " ", raw_text.strip().lower())
        if not text:
            return Result("I didn't hear a command.")

        if any(word in text for word in ("bye", "goodbye", "exit", "quit")):
            return Result("Goodbye!", should_exit=True)
        if "your name" in text:
            return Result("I'm MYA, your modular Python voice assistant.")
        if "time" in text:
            return Result(f"It is {dt.datetime.now():%I:%M %p}.")
        if "date" in text or "what day" in text:
            return Result(f"Today is {dt.date.today():%A, %B %d, %Y}.")
        if text.startswith("search for "):
            query = text.removeprefix("search for ").strip()
            self.opener(f"https://www.google.com/search?q={quote_plus(query)}")
            return Result(f"Searching for {query}.")
        for site, url in {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "spotify": "https://open.spotify.com",
        }.items():
            if text in {site, f"open {site}"}:
                self.opener(url)
                return Result(f"Opening {site.title()}.")
        return Result("I don't know that command yet. Try asking for the time, date, or a web search.")
