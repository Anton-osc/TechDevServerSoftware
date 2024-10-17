from app import app

@app.route("/healthcheck")
def healthcheck():
    return "<p> Hello, World!</p>"
