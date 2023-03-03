##cd webtacc  
##. Tacc/bin/activate
##export FLASK_APP=main.py
## flask run 
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)