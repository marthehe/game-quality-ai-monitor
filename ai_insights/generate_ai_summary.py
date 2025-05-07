import os
import json
from datetime import datetime, timedelta
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

LOG_FILE = "../telemetry_simulator/telemetry_log.json"
TIME_WINDOW_MINUTES = 5

def read_recent_crashes():
    now = datetime.utcnow()
    window_start = now - timedelta(minutes=TIME_WINDOW_MINUTES)

    try:
        with open(LOG_FILE, "r") as f:
            logs = [json.loads(line) for line in f.readlines()]
    except FileNotFoundError:
        print("[ERROR] Log file not found.")
        return []

    return [
        log for log in logs
        if log["event_type"] == "crash" and datetime.fromisoformat(log["timestamp"]) >= window_start
    ]

def build_prompt(crashes):
    prompt = (
        "You are a QA assistant at Xbox. Based on the following crash logs, "
        "summarize the issues, possible root causes, and suggest test steps to reproduce the issues.\n\n"
        f"Crash Logs:\n{json.dumps(crashes, indent=2)}\n\n"
        "Summary:"
    )
    return prompt

def get_ai_summary(crashes):
    if not crashes:
        return "[INFO] No recent crash data to summarize."

    prompt = build_prompt(crashes)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful QA assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"[ERROR] Failed to get AI response: {e}"

def main():
    crashes = read_recent_crashes()
    print(f"[DEBUG] Found {len(crashes)} crash logs in the last {TIME_WINDOW_MINUTES} minutes.")

    summary = get_ai_summary(crashes)

    print("\n--- AI QA Summary ---\n")
    print(summary)

    # Save to markdown
    if "No recent crash data" not in summary:
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        output_path = "crash_summary.md"

        with open(output_path, "a", encoding="utf-8") as f:
            f.write(f"## Crash Summary - {timestamp}\n\n")
            f.write(summary.strip() + "\n\n---\n\n")

        print(f"[INFO] Summary saved to {output_path}")
    else:
        print("[INFO] Nothing to save — no crash data.")

if __name__ == "__main__":
    main()

