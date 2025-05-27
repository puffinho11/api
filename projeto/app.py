from flask import Flask, render_template, request
import pywhatkit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    msg_status = ''
    if request.method == 'POST':
        meu_numero = request.form.get('meu_numero')
        numero_destino = request.form['numero_destino']
        mensagem = request.form['mensagem']
        enviar_agora = request.form.get('enviar_agora')

        try:
            if enviar_agora:
                pywhatkit.sendwhatmsg_instantly(numero_destino, mensagem, wait_time=10, tab_close=True)
                msg_status = "Mensagem enviada imediatamente!"
            else:
                hora = int(request.form['hora'])
                minuto = int(request.form['minuto'])
                pywhatkit.sendwhatmsg(numero_destino, mensagem, hora, minuto)
                msg_status = f"Mensagem agendada para {hora:02d}:{minuto:02d} com sucesso!"
        except Exception as e:
            msg_status = f"Erro: {e}"

    return render_template('index.html', status=msg_status)

if __name__ == '__main__':
    app.run(debug=True)

