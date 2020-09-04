from ._globals import APP

@APP.route("/")
def webpage():
    return APP.send_static_file("index.html")



