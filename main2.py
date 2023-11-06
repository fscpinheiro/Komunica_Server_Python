from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from tkinter import Tk, Button, Label, Listbox, Scrollbar
import threading
from datetime import datetime

app = Flask(__name__)
CORS(app) # Habilita o CORS
socketio = SocketIO(app, cors_allowed_origins="*") # Habilita CORS para o SocketIO

# Variável para controlar se o app Python está escutando o app React
escutando = False

# Lista para armazenar as ações recebidas do app React
acoes = []

@socketio.on('code')
def handle_code(data):
    print('Recebeu código: ' + str(data))
    emit('response', {'message': 'Código recebido: ' + str(data)})
    if escutando:
        t = threading.Thread(target=executar_acao, args=(data,))
        t.start()
    else:
        print('O app Python não está escutando o app React!')

def executar_acao(data):
    if data == '#54dfs53f':
        print('Executando ação 1...')
        # Execute a tarefa aqui
        print('Ação 1 concluída!')
        socketio.emit('action_completed', {'message': 'Ação 1 concluída!'})
    elif data == '#28fh392f':
        print('Executando ação 2...')
        # Execute a tarefa aqui
        print('Ação 2 concluída!')
        socketio.emit('action_completed', {'message': 'Ação 2 concluída!'})
    elif data == '#83hd830d':
        print('Executando ação 3...')
        # Execute a tarefa aqui
        print('Ação 3 concluída!')
        socketio.emit('action_completed', {'message': 'Ação 3 concluída!'})
    else:
        print('Comando inválido!')
        socketio.emit('action_failed', {'message': 'Comando inválido!'})

    # Adiciona a ação à lista com a data e hora
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    acoes.append(f"[{data_hora}] {data}")

def ligar():
    global escutando
    escutando = True
    print('O app Python está escutando o app React!')
    acoes.append('O app Python está escutando o app React!')

def desligar():
    global escutando
    escutando = False
    print('O app Python não está escutando o app React!')
    acoes.append('O app Python não está escutando o app React!')

def criar_janela():
    janela = Tk()
    janela.geometry("400x600")

    # Botão para ligar
    botao_ligar = Button(janela, text="Ligar", command=ligar)
    botao_ligar.pack()

    # Botão para desligar
    botao_desligar = Button(janela, text="Desligar", command=desligar)
    botao_desligar.pack()

    # Label para exibir as ações disparadas
    label_acoes = Label(janela, text="Ações:")
    label_acoes.pack()

    # Listbox para exibir as ações recebidas
    listbox_acoes = Listbox(janela, width=50)
    listbox_acoes.pack()

    # Scrollbar para rolar a lista de ações
    scrollbar = Scrollbar(janela)
    scrollbar.pack(side="right", fill="y")

    # Associa a scrollbar ao listbox
    listbox_acoes.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox_acoes.yview)

    def atualizar_lista_acoes():
        # Limpa a lista de ações
        listbox_acoes.delete(0, "end")

        # Adiciona as ações à lista
        for acao in acoes:
            listbox_acoes.insert("end", acao)

        # Rola a lista para mostrar o último item adicionado
        listbox_acoes.see("end")

        # Chama a função novamente após 100ms
        janela.after(100, atualizar_lista_acoes)

    # Inicia a atualização da lista de ações
    atualizar_lista_acoes()

    janela.mainloop()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=socketio.run, args=(app, '0.0.0.0', 5000))
    flask_thread.start()
    criar_janela()
