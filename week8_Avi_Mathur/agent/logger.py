import json
from datetime import datetime
from pathlib import Path

class Logger:
    def __init__(self):
        self.log_file = Path("agent_logs.json")

    def log_execution(
        self,
        query,
        validation_status,
        intent,
        tool_name,
        output,
        verification_status,
        execution_time=None
    ):
        log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "query": query,
            "validation": validation_status,
            "intent": intent,
            "tool": tool_name,
            "output": output,
            "verification": verification_status,
            "execution_time": execution_time,
            "status": "Completed"
        }
        print("\n========== AGENT LOG ==========")
        for key, value in log.items():
            print(f"{key:15}: {value}")
        print("=" * 35)
        if self.log_file.exists():
            with open(self.log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []
        logs.append(log)
        with open(self.log_file, "w") as f:
            json.dump(logs, f, indent=4)