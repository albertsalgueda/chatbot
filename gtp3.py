import openai

openai.api_key = "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"

conversation = ""

x=True

while x:
    question = input("Human: ")
    conversation += "\nHuman: " + question + "\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    answer = response.choices[0].text.strip()
    conversation += answer
    print('AI: ' + answer + "\n")
