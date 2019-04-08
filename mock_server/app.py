import connexion

app = connexion.FlaskApp(__name__, specification_dir='../specifications/')
app.add_api('booking.yaml')
#app.add_api('maas-api.yaml')

app.run(port=8080)

if __name__ == "__main__":
    app.run()
