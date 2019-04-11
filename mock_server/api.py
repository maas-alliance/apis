import json
import flask

# -----------------
# /bookings/options GET
# Parameter in: from, to, startTime
# "from" is mandatory
 
def bookings_options_get(**options):
    # you can get the parameters by options["from"]
    print("/bookings/options/ GET")
    return 'Message: {}'.format(options["from"]), 200

# -----------------
# /bookings GET
#
def bookings_get(state):
    # do something
    print("/bookings GET - " + state)
    # get static, manually defined JSON from a given folder
    with open("./mock_json/mock_data_bookings_get.json", "r") as read_file:
        json_string = json.load(read_file)
    #print(json_string)
    return json_string, 200 


def bookings_post(message):
    # do something
    return 'Message: {}'.format(message), 200


def bookings_id_get(message):
    # do something
    return 'Message: {}'.format(message), 200


def bookings_id_put(message):
    # do something
    return 'Message: {}'.format(message), 200


# #####################################
# add static part

# deliver a ReDoc based documentation
# ReDoc can be found here https://github.com/Rebilly/ReDoc
# MIT licence
def static_redoc():
    print("Deliver redoc")
    return flask.send_file('redoc.htm')
    