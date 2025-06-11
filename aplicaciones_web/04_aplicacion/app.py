import web

urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:

    def __init__(self):
        self.message = "Página de inicio"


    def GET(self):
        return render.index(self.message)


class Clientes:

    def __init__(self):
        self.nombres_clientes = ["Dejah Thoris", "John Carter", "Carthoris", "Tars Tarkas"]


    def GET(self):
        return render.clientes(self.nombres_clientes)


if __name__ == "__main__":
    app.run()
