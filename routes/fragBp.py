# adiciona o , render_template
from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.fragment import Fragment
from datetime import date, datetime

#Instanciar o blueprint
fragBp = Blueprint('fragBp', __name__)

@fragBp.route('/fragmento')
def fr_list():
#    return "Teste"
    #adiciona isso
#    db.create_all()
#   Adiciona o acesso a banco e a chamada ao render_template
    frs_query = Fragment.query.all() 
    return render_template('fr_list.html', frags=frs_query)

@fragBp.route('/fragmento/create')
def create_fr():
    return render_template('fr_create.html')

@fragBp.route('/fragmento/add', methods=["POST"])
def add_fr():

    sFragmento = request.form["fragmento"]
    sTitulo = request.form["titulo"]
    dInicio = datetime.strptime(request.form["dt"], '%Y-%m-%d')    

    fr = Fragment(fragmento=sFragmento, titulo=sTitulo, dt=dInicio)
    db.session.add(fr)
    db.session.commit()

    return redirect(url_for("fragBp.fr_list"))

@fragBp.route('/fragmento/update/<fr_id>')
def update_fr(fr_id=0):
    frs_query = Fragment.query.filter_by(id = fr_id).first()
    return render_template('fr_update.html', frags=frs_query)

@fragBp.route('/fragmento/upd', methods=["POST"])
def upd_fr():

    iFr = request.form["id"]
    sFragmento = request.form["fragmento"]
    sTitulo = request.form["titulo"]
    dInicio = datetime.strptime(request.form["dt"], '%Y-%m-%d')
    

    frags = Fragment.query.filter_by(id = iFr).first()
    frags.fragmento = sFragmento
    frags.titulo = sTitulo
    frags.dt = dInicio    
    db.session.add(frags)
    db.session.commit()

    return redirect(url_for("fragBp.fr_list"))

@fragBp.route('/fragmento/delete/<fr_id>')
def delete_fr(fr_id=0):
    fr_query = Fragment.query.filter_by(id = fr_id).first()
    return render_template('fr_delete.html', fr=fr_query)

@fragBp.route('/fragmento/dlt', methods=["POST"])
def dlt_fr():

    iFr = request.form["id"]
    fr = Fragment.query.filter_by(id = iFr).first()
    db.session.delete(fr)
    db.session.commit()

    return redirect(url_for("fragBp.fr_list"))