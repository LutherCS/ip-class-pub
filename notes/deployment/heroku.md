# Deploying Flask application to Heroku

1. Create an account on [Heroku](https://id.heroku.com/login)
2. (Optional) Add your **public** SSH key to Heroku account to enable key-based authentication

    ```bash
    $ cat ~/.ssh/id_rsa.pub
    ssh-rsa ...
    ```

3. Install Heroku command line interface

    ```bash
    $ sudo snap install heroku --classic
    heroku v7.35.0 from Heroku✓ installed
    ```

4. Use Heroku CLI to login (you'll authenticate in a browser)

    ```bash
    $ heroku login
    heroku: Press any key to open up the browser to login or q to exit:
    Opening browser to https://cli-auth.heroku.com/auth/browser/abcd1234-abcd-abcd-abcd-abcd1234
    Logging in... done
    Logged in as boo@hoo.foo
    ```

5. Initialize the repository in the application directory

    ```bash
    $ git init
    Initialized empty Git repository in /home/abc/.git/
    ```

6. Create virtual environment

    ```bash
    $ python3 -m venv .venv
    ```

7. Activate virtual environment

    ```bash
    $ source .venv/bin/activate
    ```

8. Install *flask* and *gunicorn*

    ```bash
    $ pip install flask gunicorn
    Successfully installed Jinja2-2.10.3 MarkupSafe-1.1.1 Werkzeug-0.16.0 click-7.0 flask-1.1.1 itsdangerous-1.1.0 gunicorn-20.0.0
    ```

9. Generate *requirements.txt*

    ```bash
    $ pip freeze > requirements.txt
    ```

    Don't forget to delete *pkg-resources==0.0.0* from *requirements.txt*

10. Copy *.gitignore* from *ip-class-pub*

    ```bash
    $ cp ../../.gitignore .
    ```

11. Create the *app.py* file

    ```python
    #!/usr/bin/env python3

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    if __name__ == "__main__":
        app.run()

    ```

12. Stage your changes

    ```bash
    $ git add .gitignore requirements.txt app.py
    ```

13. Commit your changes

    ```bash
    $ git commit -m "Initial commit"
    [master (root-commit) dceb985] Initial commit
    3 files changed, 152 insertions(+)
    create mode 100644 .gitignore
    create mode 100644 app.py
    create mode 100644 requirements.txt
    ```

14. Create Heroku app

    ```bash
    $ heroku create hello-ry
    https://hello-ry.herokuapp.com/ | https://git.heroku.com/hello-ry.git
    ```

15. Check that the remote is properly configured

    ```bash
    $ git remote -v
    heroku  https://git.heroku.com/hello-ry.git (fetch)
    heroku  https://git.heroku.com/hello-ry.git (push)
    ```

16. Push your app to Heroku

    ```bash
    $ git push heroku master
    Counting objects: 11, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (11/11), done.
    Writing objects: 100% (11/11), 1.96 KiB | 1.96 MiB/s, done.
    Total 11 (delta 3), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote: 
    remote: -----> Python app detected
    remote: -----> Installing python-3.6.9
    remote: -----> Installing pip
    remote: -----> Installing SQLite3
    remote: -----> Installing requirements with pip
    remote:        Collecting Click==7.0 (from -r /tmp/build_87752ea1ef99eff93e7fa23456f817c9/requirements.txt (line 1))
    remote:          Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
    remote:        Collecting Flask==1.1.1 (from -r /tmp/build_87752ea1ef99eff93e7fa23456f817c9/requirements.txt (line 2))
    remote:          Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
    remote:        Collecting gunicorn==20.0.0 (from -r /tmp/build_87752ea1ef99eff93e7fa23456f817c9/requirements.txt (line 3))
    remote:          Downloading https://files.pythonhosted.org/packages/60/0d/3dbda0324f5bf007f3274e5ea09f0f3bcbf0ca01a75b80ff4f1ff9f8ecfd/gunicorn-20.0.0-py2.py3-none-any.whl (77kB)
    remote:        Collecting itsdangerous==1.1.0 (from -r /tmp/build_87752ea1ef99eff93e7fa23456f817c9/requirements.txt (line 4))
    remote:          Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
    remote:        Collecting Jinja2==2.10.3 (from -r /tmp/build_87752ea1ef99eff93e7fa23456f817c9/requirements.txt (line 5))
    remote:          Downloading https://files.pythonhosted.org/packages/65/e0/eb35e762802015cab1ccee04e8a277b03f1d8e53da3ec3106882ec42558b/Jinja2-2.10.3-py2.py3-none-any.whl (125kB)
    remote:        Collecting MarkupSafe==1.1.1 (from -r /tmp/build_87752ea1ef99eff93e7fa23456f817c9/requirements.txt (line 6))
    remote:          Downloading https://files.pythonhosted.org/packages/b2/5f/23e0023be6bb885d00ffbefad2942bc51a620328ee910f64abe5a8d18dd1/MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl
    remote:        Collecting Werkzeug==0.16.0 (from -r /tmp/build_87752ea1ef99eff93e7fa23456f817c9/requirements.txt (line 7))
    remote:          Downloading https://files.pythonhosted.org/packages/ce/42/3aeda98f96e85fd26180534d36570e4d18108d62ae36f87694b476b83d6f/Werkzeug-0.16.0-py2.py3-none-any.whl (327kB)
    remote:        Installing collected packages: Click, MarkupSafe, Jinja2, itsdangerous, Werkzeug, Flask, gunicorn
    remote:        Successfully installed Click-7.0 Flask-1.1.1 Jinja2-2.10.3 MarkupSafe-1.1.1 Werkzeug-0.16.0 gunicorn-20.0.0 itsdangerous-1.1.0
    remote: 
    remote: -----> Discovering process types
    remote:        Procfile declares types -> (none)
    remote: 
    remote: -----> Compressing...
    remote:        Done: 45M
    remote: -----> Launching...
    remote:        Released v3
    remote:        https://hello-ry.herokuapp.com/ deployed to Heroku
    remote: 
    remote: Verifying deploy... done.
    To https://git.heroku.com/hello-ry.git
     * [new branch]      master -> maste
    ```

17. Your app is deployed but it's not working yet and the error log says something like this:

    ```bash
    $ heroku logs --tail
    2019-11-14T16:53:18.782233+00:00 heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/"
    ```

18. . Create *Procfile* in the app directory.

    ```text
    web: gunicorn app:app
    ```

    You need to stage, commit, and push your code to *heroku master*

19. Ensure that at least one instance of the app is running.

    ```bash
    $ heroku ps:scale web=1
    ```

20. Install PostgreSQL addon

    ```bash
    $ heroku addons:create heroku-postgresql
    Creating heroku-postgresql on ⬢ hello-ry... free
    Database has been created and is available
    ! This database is empty. If upgrading, you can transfer
    ! data from another database with pg:copy
    Created postgresql-lively-88632 as DATABASE_URL
    Use heroku addons:docs heroku-postgresql to view documentation
    ```

## References

* [Getting Started on Heroku with Python | Heroku Dev Center](https://devcenter.heroku.com/articles/getting-started-with-python)
* [PyBites – Step-by-Step Guide on Deploying a Simple Flask App to Heroku](https://pybit.es/deploy-flask-heroku.html)
* [Deploying a Python Flask app on Heroku - The Andela Way - Medium](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)
* [Scaling Your Dyno Formation | Heroku Dev Center](https://devcenter.heroku.com/articles/scaling)
* [Containerise your Python Flask using Docker and deploy it onto Heroku](https://medium.com/@ksashok/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43)
