import os
import string

from flask import Flask, request

from wakeonlan import send_magic_packet

app = Flask(__name__, static_url_path="")


@app.route('/wake/<addr>')
def wake(addr):

    # check password against env var
    password = request.args.get("pass", "")
    if password != os.environ.get("WAKEUP_PASS", ""):
        return "bad auth", 403

    # ignoring colons
    addr = addr.replace(":", "")

    # Validate address by checking length and digits
    if len(addr) != 12:
        return "address does not have 12 digits", 400

    if any(c not in string.hexdigits for c in addr):
        return "not a hexadecimal address", 400

    # send request
    try:
        send_magic_packet(addr)
        return "success", 200
    except Exception:
        return "error", 500


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True, host="0.0.0.0", port=5000)
