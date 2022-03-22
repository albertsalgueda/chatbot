prompt = """
Input: Create Directory
Output: mkdir dir

Input: clone oktopus directory
Output: git clone https://github.com/albertsalgueda/oktopus

Input: commit to github x
Outpu: git commit -a -m'x' && git push origin main
"""

template = """
Input: {}
Output: """

import os, click, openai

openai.api_key = "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"

conversation = ""

while True:
    request = input(click.style('nlsh>','red',bold=True))
    prompt += template.format(request)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt = prompt,
        temperature=0.9, #closer to 0 means just one correct answer, closer 1 if you want more creativity
        max_tokens=150
    )
    #print(response)
    command = response.choices[0].text.strip()
    prompt += command
    #print(prompt)
    if click.confirm(f">>>Run: {click.style(command,'blue')}"):
        os.system(command)
