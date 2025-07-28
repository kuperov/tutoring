# -*- coding: utf-8 -*-
"""Generate arithmetic problems
"""

from typing import List, Dict
import json
import google.generativeai as genai
from time import sleep
from dotenv import load_dotenv
import os
import argparse
import re  # Add this to imports at the top

# Load environment variables from .env file
load_dotenv()

# --- Configure the Gemini API ---
API_KEY = os.getenv('GOOGLE_API_KEY')
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")
genai.configure(api_key=API_KEY)

def generate_word_problems(problem_count: int, number_limit: int, api_attempts: int, temperature: float = 0.7) -> List[Dict]:
    prompt_text = f"""
Generate a JSON array containing exactly {problem_count} word problems designed for a primary school student learning basic addition and subtraction.

Each problem should be:
1.  An addition or subtraction problem.
2.  Use numbers (including the result) strictly within the range of 0 to {number_limit}.
3.  Feature very different and funny objects, scenarios, and characters to add variety.
4.  Spell numbers out as words in the question. Do not use digits. (For example, write "fifteen" not "15".)
5.  Don't repeat the same names or objects as in the examples in the prompt.

The output should be a JSON array where each element is an object with two keys:
-   `"question"`: The full text of the word problem.
-   `"answer"`: A concluding sentence for the problem with a blank space `____________` where the numerical answer should go. Do NOT include the actual number in the answer field.

Follow this JSON format exactly:
[
  {{"question": "Bob had five slap bands. His mum gave him one more. How many does he have now?", "answer": "Bob now has ____________ slap bands."}},
  {{"question": "Tom saw ten monkeys in a tree. Then, two monkeys ran away. How many monkeys are on the tree now?", "answer": "There are now ____________ monkeys on the tree."}},
  {{"question": "Mia picked six flowers then gave two of them to her sister. How many flowers does she have left?", "answer": "Mia has ____________ flowers left."}}
]
"""
    for _ in range(api_attempts):
        word_problems = []
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            generation_config = {
                "temperature": temperature,
                "top_p": 0.8,
                "top_k": 40
            }
            response = model.generate_content(
                prompt_text,
                generation_config=generation_config
            )
            response_text = response.text.strip()
            json_start = response_text.find('[')
            json_end = response_text.rfind(']') + 1

            if json_start != -1 and json_end != -1 and json_end > json_start:
                json_data_string = response_text[json_start:json_end]
                word_problems = json.loads(json_data_string)
                return word_problems
            else:
                print("Could not find valid JSON data in the API response.")
                print("API Response:", response_text)
        except Exception as e:
            print(f"An error occurred during the API call or JSON processing: {e}")
        sleep(30)
    return []

def make_worksheet(number: int, problem_count: int, number_limit: int, api_attempts: int, temperature: float = 0.8) -> str:
    word_problems = generate_word_problems(problem_count, number_limit, api_attempts, temperature)

    if not word_problems:
        raise Exception("Failed to generate word problems")

    lines = []
    lines.append(f'\\clearpage\\section{{Problem set \\textnumero {number}}}')
    lines.append('')
    lines.append(r'\begin{enumerate}')

    for i, problem in enumerate(word_problems):
        lines.append(f'\\item {problem["question"]}\\medskip\\par')
        lines.append(r'Number sentence: \dotfill\medskip\par')
        # widen the answer field
        sep = '\n' + r'\dotfill\medskip\par\mbox{}\dotfill\medskip\par\mbox{}\dotfill\bigskip' + '\n'
        ans = sep.join(re.split(r'_+', problem['answer']))
        lines.append(f'Answer: {ans}')
    lines.append(r'\end{enumerate}')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Generate arithmetic word problem worksheets',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'number',
        type=int,
        help='Worksheet number to generate'
    )
    parser.add_argument(
        '--problem-count',
        type=int,
        default=5,
        help='Number of problems to generate per worksheet'
    )
    parser.add_argument(
        '--number-limit',
        type=int,
        default=9999,
        help='Maximum number to use in problems'
    )
    parser.add_argument(
        '--api-attempts',
        type=int,
        default=3,
        help='Number of API attempts before giving up'
    )
    parser.add_argument(
        '--temperature',
        type=float,
        default=0.8,
        help='Temperature for LLM generation (0.0 to 1.0, higher means more creative)'
    )

    args = parser.parse_args()

    try:
        latex_text = make_worksheet(
            number=args.number,
            problem_count=args.problem_count,
            number_limit=args.number_limit,
            api_attempts=args.api_attempts,
            temperature=args.temperature,
        )
        print(latex_text)
    except Exception as e:
        print(f"Error generating worksheet: {e}")
        exit(1)

if __name__ == '__main__':
    main()
