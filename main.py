import ollama

#Get name from input
name = input("Enter your name: ")

branch = input("Enter your branch: ")
#print message - eg. Hi Rishi from CSE
print(f"Hi {name} from {branch}")

SYSTEM = '''
You explain programming error messages to a 2nd year engineering student.Reply in 3 parts.
1) What it means in plain English.
2) the likely cause
3) how to fix
4) keep it under 120 words.
'''

while True:
    data = input("Enter the error message or exit to stop: ").strip()
    if not data:
        print("Enter an error: ")
    elif data.lower() == "exit":
        break
    elif data.lower() == 'help':
        print("if you enter any error message,i'll resolve it")
        print("Enter 'exit' to stop.")
        print("Enter 'help' to see this message.")
    else:
        try:
            response = ollama.chat(model="gemma3:latest",
            messages=[
            {
                "role":"System",
                "content":SYSTEM
            },
            {
                "role":"System",
                "content":data
            }
        ])
            print(response.message.content)
        except Exception as e:
            print(f"could not reach the model: {e}")