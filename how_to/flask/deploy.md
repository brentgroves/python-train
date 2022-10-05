Flask is a WSGI application. A WSGI server is used to run the application, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses.
https://flask.palletsprojects.com/en/2.2.x/deploying/

There are many WSGI servers and HTTP servers, with many configuration possibilities. The pages below discuss the most common servers, and show the basics of running each one. The next section discusses platforms that can manage this for you.

Gunicorn
https://flask.palletsprojects.com/en/2.2.x/deploying/gunicorn/
Gunicorn should not be run as root because it would cause your application code to run as root, which is not secure. However, this means it will not be possible to bind to port 80 or 443. Instead, a reverse proxy such as nginx or Apache httpd should be used in front of Gunicorn.

You can bind to all external IPs on a non-privileged port using the -b 0.0.0.0 option. Don’t do this when using a reverse proxy setup, otherwise it will be possible to bypass the proxy.

$ gunicorn -w 4 -b 0.0.0.0 'hello:create_app()'
Listening at: http://0.0.0.0:8000 (x)
0.0.0.0 is not a valid address to navigate to, you’d use a specific IP address in your browser.



Waitress
mod_wsgi
uWSGI
gevent
eventlet
ASGI
WSGI servers have HTTP servers built-in. However, a dedicated HTTP server may be safer, more efficient, or more capable. Putting an HTTP server in front of the WSGI server is called a “reverse proxy.”

Tell Flask it is Behind a Proxy
nginx
Apache httpd