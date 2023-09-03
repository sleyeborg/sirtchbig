from flask import Flask, request, render_template, redirect, url_for
from search import search_bp
from specify import specify_bp
from login import login_bp

app = Flask(__name__)
app.register_blueprint(search_bp)
app.register_blueprint(specify_bp, url_prefix='/specify')
app.register_blueprint(login_bp, url_prefix="/login")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['q']
        tomogatchi = 'tomogatchi' in request.form
        specify = 'specify' in request.form
        functionC = 'functionC' in request.form
        specOrFuncC = request.form.get('checkboxGroupA')
        print(specOrFuncC, '010101010100119090909009')
        if specOrFuncC == 'functionC':
            search_url = url_for('search.search', q=query, tomogatchi=tomogatchi, specOrFuncC=specOrFuncC)
            return redirect(search_url)
        if specOrFuncC == 'specify':
            search_url1 = url_for('specify.specify', q=query, tomogatchi=tomogatchi, specOrFuncC=specOrFuncC)
            return redirect(search_url1)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_success():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']

        # Perform login logic here

        return redirect(url_for('login_success'))

    return render_template('loginsuccess.html')



if __name__ == '__main__':
    app.run(debug=True)
