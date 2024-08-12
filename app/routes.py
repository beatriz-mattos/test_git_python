from flask import Blueprint, render_template
from data import df

# Define um blueprint chamado 'main' para dividir a aplicação e gerenciar as rotas, na medida em que a aplicação pode crescer.
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/table')
def table():
    # Ordena o dataframe pela coluna 'notas' em ordem decrescente
    sorted_df = df.sort_values(by='notas', ascending=False)

    # Converte o dataframe ordenado para html e passa como parâmetro para o template 'table'
    return render_template('table.html', table=sorted_df.to_html(classes='table table-custom'))
