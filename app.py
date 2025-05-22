from flask import Flask, render_template, request, send_file, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import os
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

def get_aes_key(key_str):
    """Chuyển khóa bất kỳ thành 32 bytes (AES-256)"""
    return SHA256.new(key_str.encode('utf-8')).digest()

def encrypt_file(file_data, key_str):
    key = get_aes_key(key_str)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(file_data, AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return iv + encrypted  # Lưu IV ở đầu file

def decrypt_file(file_data, key_str):
    key = get_aes_key(key_str)
    iv = file_data[:16]
    encrypted = file_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    try:
        return unpad(decrypted, AES.block_size)
    except ValueError:
        return decrypted  # Trả về dữ liệu thô nếu sai khóa

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Không có file được chọn'}), 400
    file = request.files['file']
    key = request.form.get('key', '')
    operation = request.form.get('operation')
    if not file or file.filename == '':
        return jsonify({'error': 'Không có file được chọn'}), 400
    if not key:
        return jsonify({'error': 'Chưa nhập khóa'}), 400
    try:
        file_data = file.read()
        if operation == 'encrypt':
            processed_data = encrypt_file(file_data, key)
            output_filename = f'encrypted_{file.filename}'
        else:
            processed_data = decrypt_file(file_data, key)
            output_filename = f'decrypted_{file.filename}'
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        with open(output_path, 'wb') as f:
            f.write(processed_data)
        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_filename
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)