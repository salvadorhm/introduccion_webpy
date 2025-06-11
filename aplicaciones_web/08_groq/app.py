import web
import requests
import json
import os

urls = (
    '/', 'Groq',
)

render = web.template.render('templates')

app = web.application(urls, globals())

class Groq:
    def GET(self):
        return render.groq()

    def POST(self):
        input_data = web.input()
        prompt = input_data.get('prompt', 'No prompt provided')
        model = "default-model"
        stream = False

        GROQ_API_KEY = os.getenv('GROQ_API_KEY')

        data = {
            'prompt': prompt,
            'model': model,
            'stream': stream,
        }

        response = requests.post(
            'https://api.groq.com/v1/generate',
            json=data,
            headers={
                "Authorization" : f"Bearer {GROQ_API_KEY}", 
                "Content-Type": "application/json"
                }
        )

        response = json.dumps(response)

        return render.groq(response)

if __name__ == "__main__":
    app.run()