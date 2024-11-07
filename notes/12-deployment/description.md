# Application deployment

| Step | Client       | Server         |
| ---- | ------------ | -------------- |
| 1    | localhost    | localhost      |
| 2    | localhost    | PythonAnywhere |
| 2    | knuth        | PythonAnywhere |
| 2    | knuth        | render         |
| 3    | GitHub Pages | render         |

## PythonAnywhere

1. Create an account at [PythonAnywhere](https://www.pythonanywhere.com/).
2. Start a new Bash console and clone your repository to the server.
3. Add a new web app (Flask on Python 3.10). Note that your application file is going to be overwritten, you'll need to check it out from your repository.
4. Set the path to virtual environment.
5. Check out the application file from repository.
6. Enable HTTPS redirection

## GitHub pages

You get one site per GitHub account and organization, and unlimited project sites.

## Render

1. Create an account at [Render](https://render.com/).
2. Create a new application (Web Service).
3. Connect GitHub to Render.
4. Set environment variable `PYTHON_VERSION` to `3.10.12`.
5. Specify the path to *requirements.txt*.
6. Enjoy!

## Digital Ocean

...

### References

- [GitHub Student Developer Pack - GitHub Education](https://education.github.com/pack)
- [SSH and GPG keys](https://github.com/settings/keys)
- [The PythonAnywhere help pages | PythonAnywhere help](https://help.pythonanywhere.com/pages/#ive-got-an-existing-web-app-that-im-trying-to-deploy)
- [A beginner's guide to building a simple database-backed Flask website on PythonAnywhere - PythonAnywhere News](https://blog.pythonanywhere.com/121/)
- [Setting up Flask applications on PythonAnywhere | PythonAnywhere help](https://help.pythonanywhere.com/pages/Flask/)
- [How to use a virtualenv in your web app (to get newer versions of django, flask etc) | PythonAnywhere help](https://help.pythonanywhere.com/pages/Virtualenvs)
- [Docs + Quickstarts | Render · Cloud Hosting for Developers](https://render.com/docs)
- [Deploy a Flask App | Render Docs](https://render.com/docs/deploy-flask)
- [Connecting with SSH | Render Docs](https://render.com/docs/ssh)
- [GitHub Pages | Websites for you and your projects, hosted directly from your GitHub repository. Just edit, push, and your changes are live.](https://pages.github.com/)
- [How To Deploy a Static Website to the Cloud with DigitalOcean App Platform | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-static-website-to-the-cloud-with-digitalocean-app-platform)
- [Welcome to Netlify | Netlify Docs](https://docs.netlify.com/)
