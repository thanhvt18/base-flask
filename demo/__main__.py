from . import init_app

if __name__ == '__main__':
    app = init_app()
    app.run(port=8080, debug=True)