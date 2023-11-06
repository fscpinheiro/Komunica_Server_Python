from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Habilita o CORS
socketio = SocketIO(app, cors_allowed_origins="*") # Habilita CORS para o SocketIO

@socketio.on('code')
def handle_code(data):
    print('Recebeu código: ' + str(data))
    emit('response', {'message': 'Código recebido: ' + str(data)})
    if data == '#54dfs53f':
        print('Executando ação 1...')
        # Execute a tarefa aqui
        print('Ação 1 concluída!')
    elif data == '#28fh392f':
        print('Executando ação 2...')
        # Execute a tarefa aqui
        print('Ação 2 concluída!')
    elif data == '#83hd830d':
        print('Executando ação 3...')
        # Execute a tarefa aqui
        print('Ação 3 concluída!')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)