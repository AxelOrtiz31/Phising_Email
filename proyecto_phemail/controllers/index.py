import web

render = web.template.render("views", base="master")

# Index
class Index:
    def GET(self):
        return render.index()

