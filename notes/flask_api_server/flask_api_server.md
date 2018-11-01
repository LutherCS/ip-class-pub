# Building an API

1. Build a simple API that takes two numbers (`num1` and `num2`) as URL arguments and returns their sum as JSON.

2. Start the server

```
export FLASK_APP=flask_api_server.py
export FLASK_ENV=development
flask run
```

3. Test the application

```
curl --request GET 'http://localhost:5000/add?num1=1&num2=2'
```
