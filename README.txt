
Villa’s Bot - Guía rápida

1. Crear archivo `.env` con tu clave de OpenAI.
2. Subir esta carpeta a GitHub (o conectarla a Render).
3. En Render:
   - Build command: pip install -r requirements.txt
   - Start command: gunicorn app:app
4. Agregar OPENAI_API_KEY como variable de entorno.
5. En Twilio sandbox, pegá la URL pública + /webhook
6. ¡Probalo desde WhatsApp!
