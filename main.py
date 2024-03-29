import base64
import json
import zlib
from flask import Flask, render_template, request
from markupsafe import Markup

app = Flask(__name__)

@app.route("/", methods=['get', 'post'])
def tarefas() -> str:
    return render_template('index.html', valor=get_valor, salvar_valor=estado_salvo)

def get_valor():
    if 'estado' in request.form:
        return desserializar(request.form['estado'])
    return {}

def estado_salvo(estado) -> str:
    return Markup(f'<input type="hidden" name="estado" value="{serializar(estado)}">')

@app.template_filter()
def serializar(valor) -> str:
    return base64.b64encode(zlib.compress(json.dumps(valor).encode())).decode()


@app.template_filter()
def desserializar(valor: str):
    return json.loads(zlib.decompress(base64.b64decode(valor)))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=88, debug=True)
