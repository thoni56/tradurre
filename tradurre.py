#!/bin/env python

import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("LANGUAGE_LEARNING_OPENAI_KEY"))


def critique_translation(original_text, user_translation, target_language):
    prompt = f"Given the original Italian sentence: '{original_text}', and the user's Swedish translation: '{user_translation}', provide a friendly but benevolent and helpful critique of the translation accuracy and suggest improvements."
    prompt = f"Analyze the translation accuracy of the following sentence from Italian to Swedish and suggest improvements: Original Italian sentence: '{original_text}'. User's Swedish translation: '{user_translation}'."
    prompt = f"Provide a detailed critique focusing on grammar, vocabulary accuracy, and idiomatic expressions for the Swedish translation of the Italian sentence: '{original_text}'. User's translation: '{user_translation}'. Highlight any errors and suggest corrections."

    response = client.completions.create(model="gpt-3.5-turbo-instruct",
                                         prompt=prompt,
                                         temperature=0.7,
                                         max_tokens=500,
                                         top_p=1.0,
                                         frequency_penalty=0.0,
                                         presence_penalty=0.0)

    return response.choices[0].text.strip()

# Example usage
original_text = "Il gatto dorme sul divano."
user_translation = "Katten sover på soffan."
target_language = "Swedish"  # This can be used to adjust the prompt if needed

critique = critique_translation(original_text, user_translation, target_language)

print(critique)
