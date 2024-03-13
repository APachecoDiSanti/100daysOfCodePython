# Notes
1. `@app.route("/")` is a decorator function (`route(endpoint)`) that is defined inside an object (`app = Flask(__name__)`).
2. Flask routes can include variables in the URL that are specified between angled brackets (`@app.route(/user/<name>`). Those variables can be used later in the function code.
3. A Flask server can have automatic reload and debugger enabled if it is run using `debug=True` (`app.run(debug=True)`)
4. URL variables can have type hinting, e.g.: `/username/<int:id>`
5. Wrapper functions in decorators may receive both `*args` and `**kwargs` from the function that is being decorated.