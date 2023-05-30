from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
        contact = Contact(name, phone_number)
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.phone_number
        return "Kontak tidak ditemukan"

address_book = AddressBook()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        address_book.add_contact(name, phone_number)
        return redirect('/')
    return render_template('index.html', contacts=address_book.contacts)

@app.route('/remove/<name>')
def remove(name):
    address_book.remove_contact(name)
    return redirect('/')

@app.route('/search', methods=['POST'])
def search():
    name = request.form['name']
    result = address_book.search_contact(name)
    return render_template('search_result.html', name=name, result=result)

if __name__ == '__main__':
    app.run(debug=True)
