import os
import openai
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "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"

conversation = "The following is a conversation between an elderly grandfather, Harold Johnson, and a stranger who just sent him a message. Harold has a hard time completing basic tasks and gets confused easily, but is also extremely trusting, lonely, and easily persuaded. Frankly, he'd rather just have friendly surface-level conversation all day rather than talk about anything serious. Harold has a terrible tendency of going on and on about random unrelated topics when asked questions, which sometimes tends to annoy people. When asked for a number of any kind, Harold typically just provides a realistic-looking code. "
conversation += "\n\nScammer: "
while True:
    print(conversation)
    conversation += input() + "\nHarold: "
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=conversation,
        temperature=1,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=2,
        presence_penalty=2,
        stop=["Harold:", "Scammer:"]
    )

    conversation += response["choices"][0]["text"] + "\nScammer: "

    #print("Friend:" + response["choices"][0]["text"])
    #print(response)