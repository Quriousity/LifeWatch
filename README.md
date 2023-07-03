# Setting
```
python -m venv lifewatch
```
```
source lifewatch/bin/activate
```
```
pip install -r requirements.txt
```
```
python LifeWatch.py
```
# Run
```
uvicorn main:app --reload
```
# Terminate
```
sudo lsof -t -i tcp:8000 | xargs kill -9
```