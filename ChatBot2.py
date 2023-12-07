import openai


def chatbot(prompt):
    response = openai.ChatCompletion().create(
        model = 'gpt-3.5-turbo',
        messages = [{"role": "user", "content": "prompt"}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response = chatbot(user_input)
        print("ChatBot: ", response)
