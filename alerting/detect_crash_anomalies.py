import json
from datetime import datetime, timedelta

LOG_FILE = "C:/Users/t-mahend/game-quality-ai-monitor/telemetry_simulator/telemetry_log.json"
TIME_WINDOW_MINUTES = 5
CRASH_THRESHOLD = 3

def read_telemetry_logs():
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            return [json.loads(line) for line in lines]
    except FileNotFoundError:
        print("[ERROR] Log file not found.")
        return []

def filter_recent_crashes(logs):
    now = datetime.utcnow()
    window_start = now - timedelta(minutes=TIME_WINDOW_MINUTES)

    recent_crashes = [
        log for log in logs
        if log["event_type"] == "crash" and datetime.fromisoformat(log["timestamp"]) >= window_start
    ]
    return recent_crashes

def main():
    print("[INFO] Reading logs...")
    logs = read_telemetry_logs()
    recent_crashes = filter_recent_crashes(logs)

    if len(recent_crashes) > CRASH_THRESHOLD:
        print(f"[ALERT] 🚨 High crash rate detected: {len(recent_crashes)} crashes in the last {TIME_WINDOW_MINUTES} minutes!")
        for crash in recent_crashes:
            print(f" - {crash['timestamp']} on {crash['platform']} with code: {crash['code']}")
    else:
        print(f"[INFO] Crash count normal: {len(recent_crashes)} crashes in the last {TIME_WINDOW_MINUTES} minutes.")

if __name__ == "__main__":
    main()
