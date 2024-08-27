from openai import OpenAI
from groq import Groq

import time

def create_completion_ollama(system_prompt, user_prompt, api_key, model="llama3.1:latest", max_tokens=3000, stream=False):
    print("generating llama completion")
    client = OpenAI(base_url="http://localhost:11434/v1", api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=max_tokens,
        stream=stream,
    )

    print("Completion with Llama 3 generated successfully!")
    return response.choices[0].message.content

def create_groq_completion(system_prompt, user_prompt, api_key, model="llama-3.1-70b-versatile", max_tokens=3048, max_retries=3):
    client = Groq(api_key=api_key)

    for attempt in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                model=model,
                max_tokens=max_tokens,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(1)
            else:
                raise e

def create_openai_completion(system_prompt, user_prompt, api_key, model="gpt-4o-mini", max_tokens=3048, temperature=0, stream=False):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
        stream=stream,
    )

    return response.choices[0].message.content
