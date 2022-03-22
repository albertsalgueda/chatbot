prompt = """
Input: Create Directory
Output: mkdir dir

Input: clone oktopus directory
Output: git clone https://github.com/albertsalgueda/oktopus

Input: push to github x
Outpu: git add . & git commit -m'x' & git push origin main
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
