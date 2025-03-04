import web

render = web.template.render("views", base="master")

# Página de inicio
class Index:
    def GET(self):
        message = "Im looking forward to the journey ahead."
        return render.index(message)

