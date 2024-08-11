from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


df = pd.DataFrame({
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

@app.route('/table')
def table():
    # Ordena o dataframe pela coluna 'notas' em ordem decrescente
    sorted_df = df.sort_values(by='notas', ascending=False)

    # Converte o dataframe ordenado para html e passa como parâmetro para o template table
    return render_template('table.html', table=sorted_df.to_html(classes='table table-custom'))
