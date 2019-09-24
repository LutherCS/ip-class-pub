# Storing data on the client side

[html5 - What is the difference between localStorage, sessionStorage, session and cookies? - Stack Overflow](https://stackoverflow.com/questions/19867599/what-is-the-difference-between-localstorage-sessionstorage-session-and-cookies)

[cookies vs localStorage vs sessionStorage - Beau teaches JavaScript - YouTube](https://www.youtube.com/watch?v=AwicscsvGLg)

Property | Cookies | Local storage | Session storage
---------|---------|---------------|----------------
Capacity | 4 KB | 10 MB | 5 MB
Location | Client and **server** | Client | Client
Support  | HTML 4/5 | HTML 5 | HTML 5
Accessibility | Window | Window | Same tab
Expiration | Manual | Never | On tab close
In request | Yes | No | No
Visibility | Path | Domain | Domain

## Cookies

One downside is that cookies are sent to the server with **each** request. Can be made server-readable only, so the client could not alter the values. Cookie token can be used to authenticat a user to a server.

```
Set-Cookie: name=value; Expires=Wed, 09 Jun 2021 07:21:14 GMT; Path=/
```

## Local storage

New way to store data on the client side. Can be used as a (large) dictionary (key-value pairs). Editable.

* Add a value

```
window.localStorage.setItem('course', 'CS330')
```

* Retrieve a value

```
window.localStorage.getItem('course')
```

* Delete a value

```
window.localStorage.removeItem('course')
```

* Clear local storage

```
window.localStorage.clear()
```

## Session storage

Similar to *local storage* but limited to a tab and expire automatically on tab close.

```
window.sessionStorage.setItem('course', 'CS330')
```
