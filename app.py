import connexion

app = connexion.App(__name__, specification_dir='./', options={"swagger_ui": False})
app.add_api('api.yaml')

@app.route('/')
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)