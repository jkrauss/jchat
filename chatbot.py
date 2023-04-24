import openai



class ChatGPT:
    def __init__(self, api_key, role):
        openai.api_key = api_key
        self.dialogue = [{"role": "system", "content":role}]
    
    def ask(self, question):
        self.dialogue.append({"role": "user", "content": question})
        response = openai.Completion.create(
            model = 'gpt-3.5-turbo',
            prompt = question,
            max_tokens = 100,
            temperature = 0.7,
        )
        a= {"role": "system", "content": response.choices[0].message.content}
        self.dialogue.append(a)
        return a

if __name__=='__main__':
    openai.organization = "org-W62MnscL5GympAv8Aad9vTsD"
    with open('api.key') as f:
        api_key = f.read()
    chat_gpt = ChatGPT(api_key, "I am a chatbot. I can answer your questions about the world.")
    while ((question := input('\n> ')) != 'X'):
        answer  = chat_gpt.ask(question)
        print(answer)