# Build and deploy an API

## Building an API

1. Return JSON

```python
return jsonify(name="Roman")
```

2. Enable CORS

```bash
pip install flask flask-cors
```

```python
CORS(app)
```

## Deploying

1. Create an account at [PythonAnywhere](https://www.pythonanywhere.com/)
2. Pull your repository to the server
3. Add a new web app (Flask on Python 3.6). Note that your application file is going to be overwritten, you'll need to check it out from your repository
4. Set the path to virtual environment
5. Check out the application file from repository
6. Enable HTTPS redirection
7. Copy client to *knuth*
8. Enjoy at [Fake news](http://knuth.luther.edu/~yasiro01/fake_api_client/index.html)

## References

* [API Design Guide — API Design Guide 0.1 documentation](https://apiguide.readthedocs.io/en/latest/)
* [Flask-CORS — Flask-Cors 3.0.7 documentation](https://flask-cors.readthedocs.io/en/latest/)
* [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
* [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
