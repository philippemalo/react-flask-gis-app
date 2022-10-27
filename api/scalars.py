# Validate data format just before sending it to graphql scalar
def coordinates_serializer(value):
  try:
    if not type(value) == tuple:
      raise Exception('The value is not of type tuple')

    return value

  except Exception as error:
    return error

# Clean the value before passing it to the serializer
def coordinates_value_parser(value):
  try:
    return value
  except Exception as error:
    return error


def coordinates_literal_parser():
  try:
    return
  except:
    return

def json_serializer():
  try:
    return
  except:
    return

def json_value_parser():
  try:
    return
  except:
    return

def json_literal_parser():
  try:
    return
  except:
    return