from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/api/generate', methods=['GET'])
def generate_qr():
    text_to_encode = request.args.get('text', 'https://github.com')
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text_to_encode)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    
    return send_file(buffered, mimetype='image/png')
