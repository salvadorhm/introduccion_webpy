import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo HTML y Python!'

if __name__ == "__main__":
    app.run()
