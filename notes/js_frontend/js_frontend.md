# JavaScript Frontend Frameworks

* [React – A JavaScript library for building user interfaces](https://reactjs.org/)
* [AngularJS — Superheroic JavaScript MVW Framework](https://angularjs.org/)
* [Vue.js](https://vuejs.org/)
* Dozens of others

## Vue

While Angular and react have support of Google and Facebook respectively, Vue is a community-driven framework.

## Example

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Vue Hello World</title>
    </head>
    <body>
        <div id="app">
            {{ message }}
        </div>
        <script src="https://vuejs.org/js/vue.min.js"></script>
        <script>
            new Vue({
                el: "#app",
                data: {
                    message: "Hello from Vue"
                }
            });
        </script>
    </body>
</html>
```

## Vue and Jinja

```javascript
var app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
        message: "Hello from Vue"
    }
})
```

## References

* [A Real-World Comparison of Front-End Frameworks with Benchmarks (2018 update)](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962)

* [gothinkster/realworld: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more 🏅](https://github.com/gothinkster/realworld)

* [Vue.js Is Good, But Is It Better Than Angular Or React?](https://www.valuecoders.com/blog/technology-and-apps/vue-js-comparison-angular-react/)

* [Introduction — Vue.js](https://vuejs.org/v2/guide/)

* [Full-stack single page application with Vue.js and Flask](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)

* [yymm/flask-vuejs: Example & Tips, Flask with Vue.js.](https://github.com/yymm/flask-vuejs)
