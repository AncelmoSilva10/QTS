from urllib import response

import requests

advice = requests.get('https://api.adviceslip.com/advice')

idAdvice = advice.json()['slip']['id']
msgAdvice = advice.json()['slip']['advice']

print(idAdvice)
print(msgAdvice)