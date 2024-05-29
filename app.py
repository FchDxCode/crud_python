from flask import Flask, render_template
from config import Config
from extensions import db
from routes import register_blueprints
from routes.rumahsakit import get_rumahsakit  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    register_blueprints(app)
    
    @app.route('/')
    def dashboard():
        data = get_rumahsakit()
        return render_template('dashboard.html', data=data)  

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
