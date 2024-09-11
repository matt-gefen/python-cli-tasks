# Task manager cli
# Should be able to:
# 1. Show tasks in tasks.json
# 2. Add new tasks
# 3. Delete specific tasks
# 4. Change task status (in progress or done)
# 5. Change status due date

import argparse
import json

with open('tasks.json') as data_json:
    tasks_data = json.load(data_json)

# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument('--foo', '-f', action="store_true", help="print bar")

def foo():
  print("bar")

args = parser.parse_args()

if args.foo:
   foo()
   print(tasks_data)