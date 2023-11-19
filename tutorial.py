import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a psychologist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Personal Psychologist")

demo.launch()