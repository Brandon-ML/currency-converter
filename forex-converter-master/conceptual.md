### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Python is a dynamically typed language often used for server side development, data analysis, artificial intelligence and scientific computing.
  Javascript is known as the scripting language for web pages. Javascript offers more flexibility but can be more complex.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.
  Using get method: dict.get("c", default_value) - Returns default_value if "c" is not in the dictionary.
  Using try-except block:
  try:
  value = dict["c"]
  except KeyError:
  value = default_value

- What is a unit test?
  A unit test is a kind of software testing where individual units or componens of a software are tested.

- What is an integration test?
  An integration test is a kind of software testing where units are combined and tested as a group. This is used to show problems in the interaction between integrated units.

- What is the role of web application framework, like Flask?
  Flask provides development tools, libraries, and technologies. Flask manages URL routing, HTTP requests and responses, and integrates with databases and web services.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Choosing Between URL Path Parameters and Query Parameters in Flask:

URL Path Parameters ('/foods/pretzel'): Best suited for essential or hierarchical data that defines the resource being requested. It's part of the URL's structure, indicating a clear and RESTful path to the resource.
Query Parameters ('foods?type=pretzel'): Ideal for optional, non-hierarchical data that's used to modify or filter the request, like sorting, searching, or pagination. It does not define the resource but rather customizes the request

- How do you collect data from a URL placeholder parameter using Flask?
  You can define a route with a placeholder parameter using <> brackets in the route URL.

- How do you collect data from the query string using Flask?
  To collect data from the query string, use the request object provided by Flask. You can access query string parameters using request.args.

- How do you collect data from the body of the request using Flask?
  Flask allows you to access data sent in POST or PUT requests. This can be achieved using request.form for form-encoded data, or request.json for JSON-encoded data.

- What is a cookie and what kinds of things are they commonly used for?
  A cookie is a small piece of data sent from a website and stored on the user's computer by the user's web browser. Common uses include session management (logins, shopping carts), personalization (user preferences), and tracking (analyzing user behavior).

- What is the session object in Flask?
  The session object is used to store information across requests. Each user gets a unique session, and data stored in a session is accessible across multiple requests from the same user.

- What does Flask's `jsonify()` do?
  jsonify() in Flask is used to return JSON responses from a Flask view function.
