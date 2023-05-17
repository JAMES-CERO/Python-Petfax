from flask import (Blueprint, render_template )
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")

pets =json.load(open('pets.json'))
print(pets)

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/show/<int:pet_id>')
def show(pet_id): 
    pet = pets[pet_id - 1]
    return render_template('pets/show.html', pet=pet)


