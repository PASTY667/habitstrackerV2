from app import app
from flask_sqlalchemy import SQLAlchemy

if __name__ == '__main__':
    app.run(debug=True)
    


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Exemple d'URI de base de données
db = SQLAlchemy(app)

 
