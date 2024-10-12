from flask import Flask, render_template, request, redirect, url_for
from graphviz import Digraph

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        process = request.form['process']
        decision = request.form['decision']
        outcome1 = request.form['outcome1']
        outcome2 = request.form['outcome2']
        
        # Create a flowchart
        dot = Digraph(comment=title)
        dot.node("A", process)
        dot.node("B", decision)
        dot.node("C", outcome1)
        dot.node("D", outcome2)
        
        dot.edge("A", "B")
        dot.edge("B", "C", "Yes")
        dot.edge("B", "D", "No")
        
        # Save the flowchart
        dot.render('static/flowchart', format='png')

        return redirect(url_for('result'))

    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
