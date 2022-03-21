source venv/bin/activate
python -m pip install --upgrade pip
source venv/bin/activate
pip install -r requirements.txt
pip freeze >> requirements.txt
