import web

urls = (
    '/', 'Index'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def __init__(self):
        self.message = "Hola mundo desde el Index"

    def GET(self):
        #return render.index(self.message)
        return render.index()

if __name__ == "__main__":
    app.run()
