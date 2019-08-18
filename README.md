# Installation 

Install python 3.7 with your preferred env management (conda/venv)
Install packages: 
pip install requirements.txt 

Create db: 
flask db init
flask db migrate 
flask db upgrade 

Run:
flask run

#Usage 

You can register a user. Then you can use upload check (vulnerable to command injection), and view check status (vulnerable to reflected and stored XSS, via check_id and message respectively) 


