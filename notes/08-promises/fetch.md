# Fetching data

[GitHub - MitanshiKshatriya/taylor-swift-api: get random lyrics/quotes of Taylor Swift](https://github.com/MitanshiKshatriya/taylor-swift-api)

## `fetch`

```javascript
> fetch("https://taylorswiftapi.onrender.com/get")

> Promise {<pending>}
```

## `fetch` JSON

```javascript
> fetch("https://taylorswiftapi.onrender.com/get").then(response => response.json())

> Promise {<pending>}
```

## `await fetch`

```javascript
> await fetch("https://taylorswiftapi.onrender.com/get")

> Response { type: "cors", url: "https://taylorswiftapi.onrender.com/get", redirected: false, status: 200, ok: true, statusText: "", headers: Headers(2), body: ReadableStream, bodyUsed: false }
```

## `await fetch` JSON

```javascript

> await fetch("https://taylorswiftapi.onrender.com/get").then(response => response.json())

> Object { quote: "You make me so happy it turns back to sad / There's nothing I hate more than what I can't have / And you are so gorgeous it makes me so mad", song: "Gorgeous", album: "Reputation" }
```
