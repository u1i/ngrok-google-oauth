from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_email = request.headers.get('Ngrok-Auth-User-Email')
    user_name = request.headers.get('Ngrok-Auth-User-Name')
    if user_email and user_name:
        return f'Authenticated user: {user_name} ({user_email})'
    else:
        return 'No authenticated user found', 401

if __name__ == '__main__':
        app.run(port=8080)

