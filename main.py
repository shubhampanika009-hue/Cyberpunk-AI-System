import os
import sys

print("==================================================")
print("     🤖 MULTI-AGENT CYBERPUNK AI COMMAND CENTER     ")
print("==================================================")
print("Active Agents:")
print("1. Master Controller (Active)")
print("2. Termux & Automation Agent")
print("3. Ethical Hacking Agent")
print("4. Trading & Market Analyst Agent")
print("5. Git & Code Developer Agent")
print("--------------------------------------------------")

def main():
    while True:
        command = input("\n[AI Master] कमांड दर्ज करें (या 'exit' लिखें): ").strip()
        
        if command.lower() == 'exit':
            print("एआई सिस्टम बंद हो रहा है। अलविदा, राजा!")
            break
            
        elif "hack" in command.lower() or "scan" in command.lower():
            print("[Agent 3 - Hacking]: सुरक्षा स्कैन और टूल्स चलाए जा रहे हैं...")
            
        elif "trade" in command.lower() or "market" in command.lower():
            print("[Agent 4 - Trading]: कैंडलस्टिक पैटर्न और ट्रेड स्कोर एनालाइज किया जा रहा है...")
            
        elif "code" in command.lower() or "git" in command.lower():
            print("[Agent 5 - Dev]: गिट अप और कोडिंग मॉड्यूल एक्टिव है...")
            
        else:
            print(f"[Agent 1 - Master]: कमांड प्रोसेस हो रही है -> '{command}'")
            print("एआई आपके टर्मक्स और डिवाइस को कंट्रोल करने के लिए तैयार है।")

if __name__ == "__main__":
    main()
