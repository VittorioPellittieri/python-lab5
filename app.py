from flask import Flask, render_template, redirect, url_for, request, session
import database

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        """CON POST"""
        task = request.form["newTask"]
        database.newTask(task)

    tasks = database.showtasks()
    print(tasks)
    """RITORNA UN HTML"""
    return render_template('main_page.html', tasks=tasks)


@app.route('/remove_task')
def remove_task():
    """ CON GET"""
    id = request.args.get("id")
    database.removeTask(id)
    return redirect(url_for('main_page'))


if __name__ == '__main__':
    app.run()
