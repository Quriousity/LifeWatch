# 실행
```
uvicorn main:app --reload
```

# 종료
```
sudo lsof -t -i tcp:8000 | xargs kill -9
```