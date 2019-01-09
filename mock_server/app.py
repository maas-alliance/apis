import connexion

app = connexion.App(__name__, specification_dir='../specifications/')
app.add_api('booking.yaml')
app.run(port=8080)

if __name__ == "__main__":
    app.run()
