import json


# TODO - how to cope with optional parameters?
# TODO - from as Parameter name is not a good choice as the mapping here leads to an invalid code syntax ? 
# TODO -    how to map parameters in API to handler parameters?
# - 
# changed from to fromP because from is a reserved word in Python
def bookings_options_get(fromP, to, startTime):
    # do something
    print("/bookings/options/ GET")
    return 'Message: {}'.format(to), 200


# -----------------
# /bookings GET
#
def bookings_get(state):
    # do something
    print("/bookings GET - " + state)
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
