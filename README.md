# NOTE: This readme is a work in progress, will get back to it when there is time.
# pyxterm.js (Customized for TSN BOX Web application)

## How does this work?
See [pyxterm](https://github.com/cs01/pyxterm.js/blob/master/README.md)

In summary:
* A [Flask](http://flask.pocoo.org/) server is running
* The Flask server uses [flask-socketio](https://flask-socketio.readthedocs.io/en/latest/), a websocket library for Flask and socketio
* A [pty](https://docs.python.org/3/library/pty.html) ("pseudo-terminal") is spawned that runs bash.
  * You can think of a pty as a way to serialize/deserialize a terminal session. The Python docs describe it as "starting another process and being able to write to and read from its controlling terminal programmatically".

On the frontend:
* [Xterm.js](https://xtermjs.org/) is used to render [Xterm](https://en.wikipedia.org/wiki/Xterm) output data in the browser.
  * This means [escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) used by terminals to control the cursor location, color, and other options can be passed directly to Xterm.js and Xterm.js will faithfully render them as a terminal would.
  * Output from the pty process on the backend is fed into it.
  * Input from the browser is passed via websocket to the pty's input

## Nginx uwsgi Deployment


### Option 2 (Quickest but not recommended)
Clone this repository, enter the `pyxtermjs` directory, create a virtual environment (`python3 -m venv venv`), activate it (`source venv/bin/activate`) then run
```
pip install -r requirements.txt
python -m pyxtermjs
```

## Documentation
```
>> pyxtermjs --help
usage: pyxtermjs [-h] [-p PORT] [--debug] [--version] [--command COMMAND]
                 [--cmd-args CMD_ARGS]

A fully functional terminal in your browser.
http://gitsrv/algerchen/pyxtermjs

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port to run server on (default: 5000)
  --debug               debug the server (default: False)
  --version             print version and exit (default: False)
  --command COMMAND     Command to run in the terminal (default: bash)
  --cmd-args CMD_ARGS   arguments to pass to command (i.e. --cmd-args='arg1
                        arg2 --flag') (default: )

```
