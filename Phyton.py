from flask import Flask, request, jsonify
from supabase import create_client, Client

app = Flask(__name__)

# Configuração do Supabase
url: str = "https://zncobjtdaxcfsfbvpzgx.supabase.co"  # Substitua pelo URL do seu projeto
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpuY29ianRkYXhjZnNmYnZwemd4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjc4MzYwMTcsImV4cCI6MjA0MzQxMjAxN30.5fMgYDH99G1lR7z40pnBFGtCWaZvMzB5UDsk7hgCblI"  # Substitua pela sua chave API pública (anon key)
supabase: Client = create_client(url, key)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    # Verificar se o nome já está cadastrado
    result = supabase.table('CadastroUsuario').select("*").eq('nome', nome).execute()
    if result.data:
        return jsonify({'message': 'Este nome já está cadastrado no sistema.'}), 400

    # Inserir novo usuário
    supabase.table('CadastroUsuario').insert({"nome": nome, "email": email, "senha": senha}).execute()

    return jsonify({'message': 'Cadastro realizado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
from supabase import create_client, Client

app = Flask(__name__)

# Configuração do Supabase
url: str = "https://zncobjtdaxcfsfbvpzgx.supabase.co"  # Substitua pelo URL do seu projeto
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpuY29ianRkYXhjZnNmYnZwemd4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjc4MzYwMTcsImV4cCI6MjA0MzQxMjAxN30.5fMgYDH99G1lR7z40pnBFGtCWaZvMzB5UDsk7hgCblI"  # Substitua pela sua chave API pública (anon key)
supabase: Client = create_client(url, key)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    # Verificar se o nome já está cadastrado
    result = supabase.table('CadastroUsuario').select("*").eq('nome', nome).execute()
    if result.data:
        return jsonify({'message': 'Este nome já está cadastrado no sistema.'}), 400

    # Inserir novo usuário
    supabase.table('CadastroUsuario').insert({"nome": nome, "email": email, "senha": senha}).execute()

    return jsonify({'message': 'Cadastro realizado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
