from flask import Flask,request,redirect,render_template,url_for
from contact_management.contact import contact_management 

app=Flask(__name__)

contact=contact_management()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_contact',methods=['POST'])
def add_contact():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['contact']
    contact.insert(name,phone,email)
    return redirect(url_for('home'))

@app.route('/display_contact',methods=['GET'])
def display_contact():
    contacts=contact.display()
    return render_template('display_contacts.html',contacts=contacts)

@app.route('/search_contact',methods=['GET'])
def search_contact():
    name=request.args.get('searchName')
    match=contact.search(name)
    return render_template('search_contacts.html',match=match)

@app.route('/update_contact',methods=['POST'])
def update_contact():
    name=request.form['updateName']
    email=request.form['updateEmail']
    phone=request.form['updateContact']
    updated_contact=contact.update(name,email,phone)
    return redirect(url_for('home'))

@app.route('/delete_contact',methods=['POST'])
def delete_contact():
    name=request.form['deleteName']
    deleted_contact=contact.delete(name)
    return redirect(url_for('home'))    

if __name__ == '__main__':
    app.run(debug=True)
