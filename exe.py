from flask import Flask, redirect, url_for, escape


app = Flask(__name__)


@app.route('/checkstatus/<name>')
def status_page(name):
    if name == 'Vuyani':
        return redirect(url_for('admin', name=name))
    else:
        return redirect(url_for('studentUser', name=name))


@app.route('/students/<name>')
def studentuser(name):
    return "I am the guest. My name is {}".format(escape(name))


@app.route('/admin/<name>')
def admin(name):
    return "I am the admin. My name is {}".format(escape(name))


if __name__ == '__main__':
    app.debug = True
    app.run()
