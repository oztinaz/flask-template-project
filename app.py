from flask import Flask
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is not None:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/health', methods=['get'])
    def health():
        return 'OK', 200

    return app

app = create_app()

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_RUN_HOST'),
        port=int(os.getenv('FLASK_RUN_PORT')),
        debug=True,
    )