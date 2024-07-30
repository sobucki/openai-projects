import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

def colored_prompt(prompt, color_code):
    return f"\033[{color_code}m{prompt}\033[0m"

def create_question(question, messages=[]):
  messages.append({'role':'user', 'content':question})
  response = client.chat.completions.create(
  messages=messages,
  model='gpt-4o',
  max_tokens=500,
  temperature=1,
  stream=True
  )

  print(colored_prompt('GPT-4o: ','34'), end='')
  all_content = ''
  for stream_response in response:
    content = stream_response.choices[0].delta.content
    if content:
      all_content += content
      print(content, end='')

  print()
  messages.append({'role':'assistant', 'content':all_content})
  return messages

if __name__ == '__main__':

  all_messages = []

# print(all_messages)
  while True:
    question = input(colored_prompt('Sua pergunta: ','32'))
    all_messages = create_question(question, all_messages)