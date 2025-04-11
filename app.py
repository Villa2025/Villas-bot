from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body")
    print(f"Mensaje recibido: {incoming_msg}")

    response = MessagingResponse()
    msg = response.message()

    if "hola" in incoming_msg.lower():
        msg.body("¡Hola! Soy Villa’s Bot. ¿Sobre qué tema de ciencia o IA querés que te cuente?")
    else:
        msg.body("No te entendí. Escribime 'hola' para empezar.")

    return Response(str(response), mimetype="application/xml")
