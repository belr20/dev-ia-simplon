@ECHO ON
pwsh .\env\Scripts\activate.ps1
python -m pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
python manage.py fetch-data
python manage.py random-agent
