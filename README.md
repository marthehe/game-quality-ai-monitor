# 🎮 AI-Powered Game Quality Monitoring System

This project is a lightweight quality monitoring system designed to simulate real-time crash telemetry, detect anomalies, and generate AI-powered summaries to support software testing workflows.

It demonstrates a practical blend of automation, monitoring, and AI integration, showing how engineering teams can use intelligent tooling to improve application reliability and debugging efficiency.

---

## 🔍 What It Does

- **Simulates game telemetry**: crash events, performance issues, and platform-specific behaviors.
- **Detects anomalies**: flags high crash rates over rolling time windows.
- **Generates AI insights**: uses GPT to summarize issues and suggest test steps.
- **Saves QA summaries**: auto-generates clean, timestamped markdown reports.
- *(Optional coming soon)* Visualizes everything in a Power BI or Streamlit dashboard.

---
## 📁 Folder Structure

```
game-quality-ai-monitor/
├── telemetry_simulator/       # Real-time crash log generator
│   └── telemetry_generator.py
├── alerting/                  # Crash anomaly detection
│   └── detect_crash_anomalies.py
├── ai_insights/               # GPT QA assistant + summary output
│   └── generate_ai_summary.py
├── .env                       # Contains your OpenAI API key (excluded from Git)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Set Up Environment

Make sure you have Python installed (preferably with Anaconda). Then:

```bash
conda create -n saucedata python=3.10
conda activate saucedata
pip install -r requirements.txt
```

---

## 🔐 Create `.env` File

In the root folder, create a `.env` file with your OpenAI key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🧪 How to Use

### ▶ 1. Generate Simulated Game Crashes

```bash
cd telemetry_simulator
python telemetry_generator.py
```

### ▶ 2. Detect Crash Anomalies

```bash
cd ../alerting
python detect_crash_anomalies.py
```

### ▶ 3. Generate GPT-Based QA Summary

```bash
cd ../ai_insights
python generate_ai_summary.py
```

Results will appear in the console and also be saved to:

```bash
ai_insights/crash_summary.md
```

---

## ✨ Why This Project Matters

This project demonstrates:

- ✅ Real-time log processing  
- ✅ Cloud-scale monitoring patterns  
- ✅ Integration of AI for enhanced QA workflows  
- ✅ Strong understanding of automation, testing, and insights  

It also shows initiative, structure, and a passion for building tools that help engineers ship better software — especially in gaming.

---

Made with ☕ and 💙  
by Marta Hendel
