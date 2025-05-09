import random
import time
import json
from datetime import datetime

# 📄 Path to the local log file where events will be stored
log_file = "telemetry_log.json"

# 🧠 Sample data for simulation
# These are crash types the simulator will randomly choose from
crash_codes = ["NULL_PTR", "STACK_OVERFLOW", "GPU_TIMEOUT", "MEM_LEAK"]

# These represent the platforms the simulated game might be running on
platforms = ["Xbox One", "Series X", "PC"]

# Types of events (you can add others later if needed)
event_types = ["info", "warning", "crash", "performance"]

# 🔧 Generate a single fake telemetry event
def generate_event():
    # For testing crash detection, we force all events to be crashes here
    event_type = "crash"

    # 🎲 Return a simulated telemetry dictionary
    return {
        "timestamp": datetime.utcnow().isoformat(),  # Current time in ISO format
        "platform": random.choice(platforms),        # Random platform
        "event_type": event_type,                    # Currently fixed to "crash"
        "code": random.choice(crash_codes) if event_type == "crash" else None,  # Crash code or None
        "fps": round(random.uniform(10, 60), 2),     # Simulated frames per second
        "latency": round(random.uniform(20, 250), 2),# Simulated latency in ms
        "level": f"Level-{random.randint(1, 10)}"    # Simulated game level
    }

# 📡 Continuously stream telemetry data to the log file
def stream_telemetry():
    while True:
        event = generate_event()  # Create a fake event

        # Append the event as a JSON string to the log file
        with open(log_file, "a") as f:
            f.write(json.dumps(event) + "\n")

        # Print confirmation in the terminal
        print(f"[LOGGED] {event['timestamp']} - {event['event_type']}")

        # Wait 2 seconds before generating the next event
        time.sleep(2)

# ▶️ Run the telemetry stream if this script is executed directly
if __name__ == "__main__":
    print("Starting telemetry simulator...")  # Print intro
    stream_telemetry()  # Start logging events forever

