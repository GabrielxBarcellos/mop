from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
from functools import wraps
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import os
import json
import controle
import controle_seletor
import importas
import user

app = Flask(__name__, static_url_path='/static')

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
app.secret_key = 'lady'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('MATRICULA') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
    
def nvl_adm(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if int(session.get('NV')) != 10:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
    
@app.route('/', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        try:
            usuario = controle.logar(request.form['user'],request.form['password'])
            session['MATRICULA'] = usuario['MATRICULA']
            session['NV'] = usuario['NV']
            return render_template('home.html')
        except:
            flash('problema ao logar')
            return render_template('login.html')



@app.route('/logout')
def logout():
    session['MATRICULA'] = None
    session['NV'] = None
    return redirect(url_for('login'))

@app.route('/funcoes', methods=['POST'])
def funcoes():
    setor = request.form['dado']
    print(setor)
    print(controle.funcao(setor))
    return  jsonify( controle.funcao(setor))

@app.route('/cargos', methods=['POST'])
def cargos():
    setor = request.form['dado']
    funcao = request.form['dado2']
    return jsonify(controle.cargo(setor,funcao))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/agentes', methods=['POST','GET'])
@login_required
def agentes():

    setores = controle.setor()
    ccs = controle.cc()
    gestores = controle.gestor()
    jornadas = controle.jornada()
    meses = controle.mes()

    if request.method =='GET' :
        mop = controle.mop()
        return render_template('agentes.html',mop = mop , keys = mop[0].keys(), setores =setores, ccs=ccs , gestores = gestores , jornadas = jornadas, meses=meses, status= controle.status(), cargos = controle.cargo_(), funcoes = controle.funcao_())
    
    mop = controle.agente(
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
        request.form['mes'],
        request.form['adm'],
        request.form['dms'],
        request.form['status']
    ).filtrar()

    headers = {'':''}

    if len(mop):
       headers  = mop[0].keys()

    return render_template('agentes.html',mop = mop , keys = headers, setores =setores, ccs=ccs , gestores = gestores , jornadas = jornadas, meses=meses, cargos = controle.cargo_(), funcoes = controle.funcao_(), status= controle.status() )


@app.route('/deletar_agente', methods=['POST'])
@nvl_adm
def deletar_agente():
        id = request.form['id']
        controle.agente.deletar(id)
        flash('Operador deletado')

        return redirect(url_for("agentes"))

@app.route('/atualizar_agente', methods=['POST','GET'])
@nvl_adm
def atualizar_agente():
        if request.method == "GET":
            agente = controle.agente.buscar_por_id(request.args.get('id'))
            setores = controle.setor()
            ccs = controle.cc()
            gestores = controle.gestor()
            jornadas = controle.jornada()
            meses = controle.mes()
            status = controle.status()
            return render_template('agente_atualizar.html',id = request.args.get('id'), status = status,agente = agente, setores =setores, ccs=ccs , gestores = gestores , jornadas = jornadas, meses=meses)

        if request.method == "POST":
            id = request.form['id']
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
            request.form['mes'],
            request.form['adm'],
            request.form['dms'],
            request.form['status']
        ).atualizar(id)
            return redirect(url_for("agentes"))

@app.route('/cadastrar_operador')
@nvl_adm
def cadastrar_operador():
    setores = controle.setor()
    ccs = controle.cc()
    gestores = controle.gestor()
    jornadas = controle.jornada()
    meses = controle.mes()
    status = controle.status()
    return render_template('agente_cadastro.html' , setores =setores, ccs=ccs , gestores = gestores , jornadas = jornadas, meses=meses , status= status)

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
        request.form['mes'],
        request.form['adm'],
        request.form['dms'],
        request.form['status']
    ).cadastrar()
    return redirect(url_for('agentes'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/importar', methods=['POST','GET'])
@nvl_adm
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        endereco = app.config['UPLOAD_FOLDER']
        importas.backup_mop(endereco)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            arquivo = os.path.join(endereco, filename)
            file.save(arquivo)
            importas.importar_agentes(arquivo)
    return redirect(url_for('agentes')) 

@app.route('/setor_select',methods=['POST','GET'])
@nvl_adm
def setor_select():
    if request.method =='GET' :
        setores = controle_seletor.setor()
        return render_template('setor.html', keys = setores[0].keys(),setores = setores )
    if request.method =='POST' :
        setor = json.loads(request.form['data'])
        controle_seletor.setor_novo_update(setor)
    return "Setor incluído/modificado"

@app.route('/setor_delete',methods=['POST'])
def setor_delete():
    setor = json.loads(request.form['data'])
    print(setor)
    controle_seletor.deletar_setor(setor)
    return "Setor deletado"

@app.route('/usuarios',methods=['POST','GET'])
@nvl_adm
def usuarios():
    if request.method =='GET':
        users = user.users()
        return render_template('user.html', users  = users)
    if request.method =='POST':
        reposta = json.loads(request.form['data'])
        user.user_novo_update(reposta)
    return 'Usuario atualizado'

@app.route('/usuario_deletar',methods=['POST'])
@nvl_adm
def usuario_deletar():
        reposta = json.loads(request.form['data'])
        user.delete_user(reposta)
        return 'Usuario deletado'
@app.route('/trocar_senha',methods=['POST'])
def trocar_senha():
    user.trocar_senha(session.get('MATRICULA'),request.form['data'])
    return "Senha trocada :)"
if __name__ == "__main__":
    app.run(debug=True)