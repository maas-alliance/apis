import connexion
import flask

app = connexion.FlaskApp(__name__, specification_dir='../specifications/')
app.add_api('booking.yaml', base_path='/booking')
app.add_api('staticfile.yaml', base_path='/redoc')
#app.add_api('maas-api.yaml')

app.run(port=8080)

if __name__ == "__main__":
    app.run()
