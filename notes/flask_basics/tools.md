# Modern Web Development Tools

This guide is written for Ubuntu. Users of Windows, macOS, FreeBSD, and other systems should refer to each tool's documentation.

## virtualenv

Initialize a new virtual environment in the current directory

```bash
python3 -m venv .venv
```

If the previous command does not work, you may have to install `virtualenv`

```bash
pip install virtualenv
```

Activate the environment

```bash
source .venv/bin/activate
```

Update `pip`

```bash
pip install -U pip
```

Install the `flask` package and it dependencies

```bash
pip install flask
```

Save currently installed packages to a file

```bash
pip freeze > requirements.txt
```

Installed required packages from a file

```bash
pip install -r requirements.txt
```

Deactivate the environment

```bash
deactivate
```

## Git

Check repository status

```bash
git status
```

Add (stage) new file(s)

```bash
git add [filename]
```

Commit changes (write them to the repository history)

```bash
git commit -m 'Message'
```

Upload your local repository copy to the server (GitHub, GitLab, Bitbucket etc.)

```bash
git push
```

Download updated code from the server

```bash
git fetch
```

Merge the updates into your local codebase

```bash
git merge
```

`fetch` and `merge` can be run together

```bash
git pull
```

## ssh

Generate ssh keys

```bash
$ ssh-keygen -t rsa -C "your_email@example.com"

Your identification has been saved in /home/yasiro01/.ssh/id_rsa.
Your public key has been saved in /home/yasiro01/.ssh/id_rsa.pub.
```

Add you **public** key to GitHub account

## pythonanywhere

* Use a **pythonanywhere** console to clone your repository
* Deploy your app as a Web app on *username.pythonanywhere.com*

## References

* [python - What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc? - Stack Overflow](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
* [venv — Creation of virtual environments — Python 3.7.3 documentation](https://docs.python.org/3/library/venv.html)
* [Virtualenv — virtualenv 16.4.4.dev0 documentation](https://virtualenv.pypa.io/en/latest/)
* [Pipenv: Python Dev Workflow for Humans](https://pipenv.readthedocs.io/en/latest/)
* [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)
* [Pipenv & Virtual Environments — The Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/)
* [GitHub Guides](https://guides.github.com/)
* [git - the simple guide](http://rogerdudler.github.io/git-guide/)
* [Learn Git- Git tutorials, workflows and commands | Atlassian Git Tutorial](https://www.atlassian.com/git)
* [Creating SSH keys - Atlassian Documentation](https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html)
* [Connecting to GitHub with SSH - User Documentation](https://help.github.com/articles/connecting-to-github-with-ssh/)
* [Web app setup : yasiro01 : PythonAnywhere](https://www.pythonanywhere.com/user/yasiro01/webapps/)
