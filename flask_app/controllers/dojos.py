from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def all_dojos():
    dojos = Dojo.get_all()
    return render_template('/dojo.html', dojos=dojos)


@app.route('/create/dojo', methods=['post'])
def create_dojo():
    data = {
        "name": request.form["name"]
        }
    print(data)
    Dojo.save(data)
    return redirect('/')


@app.route('/show/<int:id>/dojo')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('show_dojo.html', dojo=Dojo.get_one_with_ninjas(data))