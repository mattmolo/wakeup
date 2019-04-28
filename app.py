import string

from flask import Flask

from wakeonlan import send_magic_packet

app = Flask(__name__, static_url_path="")


@app.route('/wake/<addr>')
def wake(addr):
    addr = addr.replace(":", "")

    if len(addr) != 12:
        return "address does not have 12 digits", 400

    if any(c not in string.hexdigits for c in addr):
        return "not a hexadecimal address", 400

    try:
        send_magic_packet(addr)
        return "success", 200
    except Exception:
        return "error", 500


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True, host="0.0.0.0", port=5000)
