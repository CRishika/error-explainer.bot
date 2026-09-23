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

response = ollama.chat(model="gemma3",messages=[
{
"role":"System",
"content":SYSTEM
},
    {
        "role":"System",
        "content":"""python error:
        NameError: name 'x' is not defined"""
    }
])
print(response.message.content)