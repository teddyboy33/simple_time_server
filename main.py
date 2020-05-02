import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/epoch')
def get_epoch():
    current_time = datetime.now()
    return current_time.strftime('%s')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
