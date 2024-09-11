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

parser.add_argument(
  '--list',
  '-l',
  # action="store_true",
  nargs='?',
  const='all',
  required=False,
  help='Prints tasks. Can filter by status.'
)

def list():
  tasks = tasks_data["tasks"]
  # print all tasks : default
  if str(args.list) == "all":
     for task in tasks:
      print(task)
  # print in-progress tasks
  elif str(args.list) == "in-progress":
     for task in tasks:
      if task["status"] == "in-progress":
        print(task)


args = parser.parse_args()

if args.list:
  list()