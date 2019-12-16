from eml_parser import eml_parser
from os import listdir
from os.path import isfile, join
import json
import datetime
import sys
import getopt

def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

def print_help():
  print(__file__ + " [-b] [file ...]")

def print_eml(filename, raw_body):
  if filename.endswith('.eml'):
    with open(filename, 'rb') as e:
      print(json.dumps(eml_parser.decode_email_b(e.read(), include_raw_body=raw_body), default=json_serial))

def main(argv):
  try:
    opts, _ = getopt.getopt(argv,"hi:b",["input="])
  except getopt.GetoptError:
    print_help()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print_help()
    elif opt in ("-i", "--input", "-b"):
      print_eml(arg, True)
    elif opt in ("-i", "--input"):
      print_eml(arg, False)

if __name__ == "__main__":
    main(sys.argv[1:])