# Validate data format just before sending it to graphql scalar
def coordinates_serializer(value):
  try:
    # print('Evaluating coordinates format...', value)
    if not type(value) == list:
      raise Exception('The value is not of type list')
    
    if not len(value) == 2:
      raise Exception('The length of the coordinate list is not equal to 2. It should be equal to 2 considering that it holds the longitude and latitude.')

    if not type(value[0]) == float:
      raise Exception('The longitude value is not of type float')

    if not type(value[1]) == float:
      raise Exception('The latitude value is not of type float')

    if value[0] < -180:
      raise Exception('The longitude is out of bound; less than -180')

    if value[0] > 180:
      raise Exception('The longitude is out of bound; greater than 180')

    if value[1] < -90:
      raise Exception('The latitude is out of bound; less than -90')

    if value[1] > 90:
      raise Exception('The latitude is out of bound; greater than 90')

    return value

  except Exception as error:
    return error

# Clean the value before passing it to the serializer
def coordinates_value_parser(value):
  try:
    print('VAL: ', value)
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