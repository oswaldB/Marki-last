# utils/console_logger.py
import datetime

def setup_console_logger(page):
    def console_handler(msg):
        log_entry = {
            "type": msg.type,
            "text": msg.text,
            "location": {
                "url": msg.location.get("url", None),
                "line": msg.location.get("lineNumber", None),
                "column": msg.location.get("columnNumber", None)
            } if msg.location else None,
            "timestamp": datetime.datetime.now().isoformat()
        }
        print(f"[{log_entry['timestamp']}] {log_entry['type']}: {log_entry['text']}")
        if log_entry["location"]:
            print(f"  @ {log_entry['location']['url']}:{log_entry['location']['line']}:{log_entry['location']['column']}")

    page.on("console", console_handler)