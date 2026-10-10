# Termux & Automation Agent
import os
import subprocess

def run_termux_command(cmd):
    print(f"[Termux Agent] कमांड निष्पादित की जा रही है: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("त्रुटि:", result.stderr)
    except Exception as e:
        print(f"[Termux Agent Error]: {e}")

if __name__ == "__main__":
    print("🤖 Termux & Automation Agent एक्टिव है।")
    run_termux_command("uname -a")
