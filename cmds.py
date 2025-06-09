py -3.11 -m venv snowpark-env
.\snowpark-env\Scripts\Activate.ps1
pip install --upgrade pip setuptools wheel
pip install snowflake-snowpark-python
python test_snowpark.py
