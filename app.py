from flask import Flask, render_template
from routes import bp

app = Flask(__name__)
app.register_blueprint(bp)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html'), 500

if __name__ == '__main__':
    app.run()