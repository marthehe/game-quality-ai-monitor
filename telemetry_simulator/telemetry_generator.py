import random
import time
import json
from datetime import datetime

# Optional: write to local log file
log_file = "telemetry_log.json"

# Sample data
crash_codes = ["NULL_PTR", "STACK_OVERFLOW", "GPU_TIMEOUT", "MEM_LEAK"]
platforms = ["Xbox One", "Series X", "PC"]
event_types = ["info", "warning", "crash", "performance"]

def generate_event():
    event_type = "crash"



    
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "platform": random.choice(platforms),
        "event_type": event_type,
        "code": random.choice(crash_codes) if event_type == "crash" else None,
        "fps": round(random.uniform(10, 60), 2),
        "latency": round(random.uniform(20, 250), 2),
        "level": f"Level-{random.randint(1, 10)}"
    }

def stream_telemetry():
    while True:
        event = generate_event()
        with open(log_file, "a") as f:
            f.write(json.dumps(event) + "\n")
        print(f"[LOGGED] {event['timestamp']} - {event['event_type']}")
        time.sleep(2)  # adjust for faster or slower simulation

if __name__ == "__main__":
    print("Starting telemetry simulator...")
    stream_telemetry()
