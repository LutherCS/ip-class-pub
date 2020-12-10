# How to setup your development environment

This guide assumes you are using Ubuntu as your development OS and Visual Studio Code as an IDE. Other tools and technologies will be described as needed.

## Ubuntu

You should use the latest LTS version of Ubuntu, 20.04.1. If your current version is 18.04, do a system upgrade:

```bash
sudo do-release-upgrade
```

You should configure Ubuntu to check for updates automatically or do it periodically:

```bash
sudo apt update
sudo apt upgrade
```

## JavaScript

[Install nodejs to run JavaScript files from terminal](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04)

```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Install *jshint* (don't forget to install jshint extension in VS Code)

```bash
sudo npm install -g jshint
```

## Python

Check that you have Python 3.8+ installed.

```bash
python3 --version
```

## PostgreSQL

```bash
ssh -f student@knuth.luther.edu -L 2345:localhost:5432 -N
```

```python
c = connect(user='student', port=2345, dbname='world', host='localhost')
curs = c.cursor()
curs.execute('select * from country')
curs.fetchone()
# ('AFG', 'Afghanistan', 'Asia', 'Southern and Central Asia', 652090.0, 1919, 22720000, 45.9, Decimal('5976.00'), None, 'Afganistan/Afqanestan', 'Islamic Emirate', 'Mohammad Omar', 1, 'AF')
```

## Deployment on PythonAnywhere

1. Pull your repository to *pythonanywhere*

    ```bash
    git pull
    ```

2. Create a new virtual environment

    ```bash
    python3 -m venv .venv
    ```

3. Activate an existing virtual environment

    ```bash
    source .venv/bin/activate
    ```

4. Install required packages

    ```bash
    pip install flask records requests psycopg2
    pip list
    ```

5. Save the requirements for reuse.

    ```bash
    pip freeze > requirements.txt
    ```

6. Deactivate current virtual environment

    ```bash
    deactivate
    ```
