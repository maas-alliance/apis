import connexion

app = connexion.FlaskApp(__name__, port = 8080, specification_dir='../specifications/')
app.add_api('maas-api.yaml', base_path='/maas')
app.add_api('booking.yaml', base_path='/booking')

# @app.route('/routes', methods=['GET'])
# def list_routes():
#     return ['%s' % rule for rule in app.url_map.iter_rules()]

if __name__ == "__main__":
    app.run()
