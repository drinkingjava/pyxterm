from app import app, socketio
# from app import main

# When the app is run in uwsgi without args, it will fail.
app.config['cmd'] = 'bash'
if __name__ == "__main__":
    # app.run()
    # app.main()
    socketio.run(app)
