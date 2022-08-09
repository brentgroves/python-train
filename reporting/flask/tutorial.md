https://code.visualstudio.com/docs/python/tutorial-flask
Flask is a lightweight Python framework for web applications that provides the basics for URL routing and page rendering.

Flask is called a "micro" framework because it doesn't directly provide features like form validation, database abstraction, authentication, and so on. Such features are instead provided by special Python packages called Flask extensions. The extensions integrate seamlessly with Flask so that they appear as if they were part of Flask itself. For example, Flask doesn't provide a page template engine, but installing Flask includes the Jinja templating engine by default. For convenience, we typically speak of these defaults as part of Flask.

In this Flask tutorial, you create a simple Flask app with three pages that use a common base template. Along the way, you experience a number of features of Visual Studio Code including using the terminal, the editor, the debugger, code snippets, and more.

The completed code project for this Flask tutorial can be found on GitHub: python-sample-vscode-flask-tutorial.

If you have any problems, feel free to file an issue for this tutorial in the VS Code documentation repository.

Use a template to render a page#
The app you've created so far in this tutorial generates only plain text web pages from Python code. Although it's possible to generate HTML directly in code, developers avoid such a practice because it opens the app to cross-site scripting (XSS) attacks. In the hello_there function of this tutorial, for example, one might think to format the output in code with something like content = "<h1>Hello there, " + clean_name + "!</h1>", where the result in content is given directly to a browser. This opening allows an attacker to place malicious HTML, including JavaScript code, in the URL that ends up in clean_name and thus ends up being run in the browser.

A much better practice is to keep HTML out of your code entirely by using templates, so that your code is concerned only with data values and not with rendering.

A template is an HTML file that contains placeholders for values that the code provides at run time. The templating engine takes care of making the substitutions when rendering the page. The code, therefore, concerns itself only with data values and the template concerns itself only with markup.
The default templating engine for Flask is Jinja, which is installed automatically when you install Flask. This engine provides flexible options including automatic escaping (to prevent XSS attacks) and template inheritance. With inheritance, you can define a base page with common markup and then build upon that base with page-specific additions.

