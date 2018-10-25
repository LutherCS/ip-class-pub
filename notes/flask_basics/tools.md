# Modern Web Development Tools

## pipenv

* [Pipenv: Python Dev Workflow for Humans](https://pipenv.readthedocs.io/en/latest/)

* [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)

* [python - What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc? - Stack Overflow](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)


Install 

```
python3 -m pip install -U pipenv
```

Get help

```
pipenv --help
```

Start a virual environmemnt (notice the command line prompt change)

```
pipenv shell
```

A new directory is created (XXXXXXXX are some hash), but you don't need to go there

```
/home/username/.local/share/virtualenvs/ip-class-prep-XXXXXXXX/
```

Install a package

```
pipenv install flask
```

See installed packages

```
pipenv graph
```

Generate *Pipfile* (improved version of *requirements.txt*)

```
pipenv lock
```

Install all packages specified in the *Pipfile.locl*

```
pipenv sync
```

Exit the virtual environment

```
exit
```

## Git

* [GitHub Guides](https://guides.github.com/)

* [git - the simple guide](http://rogerdudler.github.io/git-guide/)

* [Learn Git- Git tutorials, workflows and commands | Atlassian Git Tutorial](https://www.atlassian.com/git)

Check repository status

```
git status
```

Add (stage) new file(s)

```
git add [filename]
```

Commit changes (write them to the repository history)

```
git commit -m 'Message'
```

Upload your local repository copy to the server (GitHub, GitLab, Bitbucket etc.)

```
git push
```

Download updated code from the server

```
git fetch
```

Merge the updates into your local codebase

```
git merge
```

*fetch* and *merge* can be run together

```
git pull
```

## ssh

* [Creating SSH keys - Atlassian Documentation](https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html)

* [Connecting to GitHub with SSH - User Documentation](https://help.github.com/articles/connecting-to-github-with-ssh/)

* [Web app setup : yasiro01 : PythonAnywhere](https://www.pythonanywhere.com/user/yasiro01/webapps/)


Generate ssh keys

```
$ ssh-keygen -t rsa -C "your_email@example.com"

Your identification has been saved in /home/yasiro01/.ssh/id_rsa.
Your public key has been saved in /home/yasiro01/.ssh/id_rsa.pub.
```

Add you **public** key to GitHub account

## pythonanywhere

* Use a **pythonanywhere** console to clone your repository

* Deploy your app as a Web app on *username.pythonanywhere.com*
