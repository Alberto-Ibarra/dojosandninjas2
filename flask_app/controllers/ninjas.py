from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.ninja import Ninja



# @app.route('/dashboard')
# def dashboard():
#     ninjas = Ninja.get_all()
#     return render_template('/result.html', ninjas=ninjas)

@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos=dojos)


@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)