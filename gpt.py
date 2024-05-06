import gradio as gr
import os
from groq import Groq  # Ensure Groq library supports this usage

def fetch_response(user_input):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "you are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False
    )
    return chat_completion.choices[0].message.content

iface = gr.Interface(fn=fetch_response, inputs="text", outputs="text", title="Groq Chatbot", description="Ask a question and get a response.")
iface.launch()