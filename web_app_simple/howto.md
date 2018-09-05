# Working with cgi-bin

1. Edit `cgi-bin/hello.py` and use `chmod` to make it executable

1. Start the server

    ```
    python3 -m http.server --cgi

    ```

1. Open static `hello.html` in a browser

    ```
    http://localhost:8000/hello.html
    
    ```

1. Open the generated page in a browser

    ```
    http://localhost:8000/cgi-bin/hello.py?name=Roman&n=5

    ```
