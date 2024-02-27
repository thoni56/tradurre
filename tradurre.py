#!/bin/env python

import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("LANGUAGE_LEARNING_OPENAI_KEY"))


def critique_translation(original_text, user_translation):
    prompt = f"You are a professional language coach specialized in providing detailed feedback on Italian translations from Swedish. Your feedback should include corrections, explanations for common mistakes, and suggestions for improvement without being overly positive. Here's the user's attempt at translation: Original Swedish sentence: '{original_text}' User's Italian attempt at translation: '{user_translation}'"

    response = client.completions.create(model="gpt-3.5-turbo-instruct",
                                         prompt=prompt,
                                         temperature=0.1,
                                         max_tokens=500,
                                         top_p=1.0,
                                         frequency_penalty=0.0,
                                         presence_penalty=0.0)

    return response.choices[0].text.strip()


original_texts = [
    "Katten sover på soffan.",
    "Mitt hus är stort.",
    "Finns det en polisstation i närheten?"
]

for original_text in original_texts:
    print(f"Översätt följande mening till italienska '{original_text}':")
    user_translation = input()
    critique = critique_translation(original_text, user_translation)
    print(critique)
    print()

print("Lektionen är över.")
