from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
from os.path import join, dirname, realpath
import json
import controle
app = Flask(__name__, static_url_path='/static')

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
app.secret_key = 'lady'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/funcoes', methods=['POST'])
def funcoes():
    setor = request.form['dado']
    return jsonify(controle.funcao(setor))

@app.route('/cargos', methods=['POST'])
def cargos():
    setor = request.form['dado']
    funcao = request.form['dado2']
    return jsonify(controle.cargo(setor,funcao))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/agentes')
def agentes():
    mop = controle.mop()
    return render_template('agentes.html',mop = mop , keys = mop[0].keys())

@app.route('/cadastrar_operador')
def cadastrar_operador():
    setores = controle.setor()
    ccs = controle.cc()
    gestores = controle.gestor()
    jornadas = controle.jornada()
    meses = controle.mes()
    return render_template('agente_cadastro.html' , setores =setores, ccs=ccs , gestores = gestores , jornadas = jornadas, meses=meses)

@app.route('/cadastrar_operador_post', methods=['POST'])
def cadastrar_operador_post():
    controle.agente(
        request.form['cadastro'],
        request.form['nome'],
        request.form['ramal'],
        request.form['pausa'],
        request.form['celular'],
        request.form['monitoria'],
        request.form['cc'],
        request.form['setor'],
        request.form['cargo'],
        request.form['funcao'],
        request.form['nvl'],
        request.form['gestor'],
        request.form['jornada'],
        request.form['sabado'],
        request.form['mes']
    ).cadastrar()
    return redirect(url_for('agentes'))

if __name__ == "__main__":
    app.run(debug=True)
