from flask import Flask

#factory
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:Bratva@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from . import models
    models.db.init_app(app)

    
    @app. route('/')
    def hello():
       return 'Hello, PetFax'
    
    #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)


        
    return app