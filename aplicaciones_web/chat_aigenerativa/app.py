import web
import requests
import json

urls = (
    "/","Generate"
)

render = web.template.render("templates")
app = web.application(urls,globals())


class Generate:

    def __init__(self):
        pass

    def ollama(self,prompt):
        try:
            data = {
                "prompt" : prompt,
                "model" : "gemma3:1b",
                "stream": False
            }

            url = "http://localhost:11434/api/generate"
            response = requests.post(url,json=data)
            response = json.loads(response.text)
            return response["response"]
        except Exception as error:
            response = f"ERROR 001: {error.args[0]}"
            print(response)
            return response

    def GET(self):
        return render.generate()
    
    def POST(self):
        try:
            formulario = web.input()
            prompt = formulario.prompt
            print(f"PROMPT: {prompt}")
            response = self.ollama(prompt)
            return render.generate(response)
        except Exception as error:
            response = f"ERROR 002: {error.args[0]}"
            print(response)
            return render.generate(response)

if __name__ == "__main__":
    app.run()
