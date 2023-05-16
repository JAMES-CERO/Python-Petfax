from flask import (Blueprint, render_template )
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")

pets =json.load(open('pets.json'))
print(pets)

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/show/<int:pet_id>')
def show(pet_id): 
    pet = pets[pet_id - 1]
    return render_template('show.html', pet=pet)

@bp.route('/new')
def new():
    return render_template('new.html')


