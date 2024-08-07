from flask import Flask

server = Flask(__name__)

@server.route('/') 

def saludo():
    return 'hola'

if __name__ == '__main__':
 server.run(host= "0.0.0.0", port=5000)
