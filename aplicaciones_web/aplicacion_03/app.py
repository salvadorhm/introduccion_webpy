import web

urls = (
    '/', 'Index'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index("Hola desde python")

if __name__ == "__main__":
    app.run()
