import threading
from app import app
from taupunkt_scanner import main

if __name__ == '__main__':
    t = threading.Thread(target=main)
    t.daemon = True
    t.start()
    app.run(host="0.0.0.0", port=5000, debug=True) # vorord nochmal testen
