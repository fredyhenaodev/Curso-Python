from flask import Flask, render_template, request
from contactModel import Contact
app = Flask(__name__)

@app.route(r'/', methods=['GET'])
def hola():
    return render_template('index.html')

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.form:
        contact = Contact(request.form.get('name'),
                         request.form.get('phone'),
                         request.form.get('email'))

        contact.put()

    return render_template('add_contact.html')


if __name__ == '__main__':
    app.run()