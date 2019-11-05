import connexion
import os

from flask import Response

app = connexion.App(__name__, specification_dir='./', options={"swagger_ui": False})
app.add_api('api.yaml')


@app.route('/')
def home():
    def stream_index_page():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "static/index.html"), "r") as index_page:
            for line in index_page:
                yield line

    return Response(stream_index_page(), mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
