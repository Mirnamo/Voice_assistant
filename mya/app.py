from __future__ import annotations

import argparse
import logging

from .assistant import Assistant
from .audio import MicrophoneListener, Speaker
from .config import Settings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the MYA voice assistant")
    parser.add_argument("--text", action="store_true", help="use keyboard input instead of a microphone")
    parser.add_argument("--once", action="store_true", help="handle one command and exit")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    settings = Settings.from_env()
    logging.basicConfig(level=settings.log_level, format="%(levelname)s %(message)s")
    speaker = Speaker(rate=settings.speech_rate)
    listener = None if args.text else MicrophoneListener(settings)
    assistant = Assistant(speaker=speaker)

    speaker.say("MYA is ready. How can I help?")
    while True:
        try:
            text = input("You: ") if args.text else listener.listen()
        except (EOFError, KeyboardInterrupt):
            break
        if not text:
            continue
        result = assistant.handle(text)
        if result.reply:
            speaker.say(result.reply)
        if result.should_exit or args.once:
            break


if __name__ == "__main__":
    main()
