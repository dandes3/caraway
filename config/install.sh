#Handle dependencies and add relevant packages to PYTHONPATh

echo Installing flask;
pip install flask --user;
echo Installing flask sqlalchemy
pip install flask-sqlalchemy --user;
echo Installing yahoo_finance
pip install yahoo_finance --user;


python3 path.py
