from website import create_app

app = create_app()

if __name__ == '__main__':
    # App reloads after every change
    app.run(debug=True)
