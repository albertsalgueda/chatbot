prompt = """
Input: Create Directory dir
Output: mkdir dir

Input: clone oktopus 
Output: git clone https://github.com/albertsalgueda/oktopus

Input: clone sentiment 
Output: git clone https://github.com/albertsalgueda/sentiment

Input: clone crypto bot 
Output: git clone https://github.com/albertsalgueda/trade

Input: clone detection 
Output: git clone https://github.com/albertsalgueda/detection

Input: push repo x
Outpu: git commit -a -m'x' && git push origin main

Input: update repo
Output: git pull origin main

Input: create test 
Output: git checkout -b test && git commit -a -m'x' && git push origin test

Input: test repo 
Output: git checkout test && git commit -a -m'x' && git push origin test
"""

template = """
Input: {}
Output: """

import os, click, openai

with open('key.txt', 'r') as file:
    OPENAI_API_KEY = file.read().rstrip()


openai.organization = "org-loyyMW35uINGPaiOuTAd0zq8"
openai.api_key = str(OPENAI_API_KEY)
openai.Engine.list()

conversation = ""

while True:
    request = input(click.style('nlsh>','red',bold=True))
    if request.upper() == 'EXIT':
        print('Thank you for using the Oktopus command line!')
        break
    prompt += template.format(request)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt = prompt,
        temperature=0.0, #closer to 0 means just one correct answer, closer 1 if you want more creativity
        max_tokens=150
    )
    #print(response)
    command = response.choices[0].text.strip()
    prompt += command
    #print(prompt)
    if click.confirm(f">>>Run: {click.style(command,'blue')}"):
        os.system(command)
