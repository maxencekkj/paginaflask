from flask import Flask, jsonify

app = Flask(__name__)

# Lista de alunos
alunos = ['kleber', 'joao', 'zezinho', 'lucas']

# Lista de reprovados
reprovados = ['lucas', 'joao']

@app.route('/resultados', methods=['GET'])
def resultados():
    resultados = []

    for aluno in alunos:
        status = 'Reprovado' if aluno in reprovados else 'Aprovado'
        resultados.append({'nome': aluno, 'status': status})

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)