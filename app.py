from groq import Groq
client = Groq(
    api_key="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" 
)

def chat_with_llama(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def main():
    print("Welcome to the Llama Chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = chat_with_llama(user_input)
        print("Llama:", response)
if __name__ == "__main__":
    main()
