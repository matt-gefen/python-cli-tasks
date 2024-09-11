# Task manager cli
# Should be able to:
# 1. Show tasks in tasks.json
# 2. Add new tasks
# 3. Delete specific tasks
# 4. Change task status (in progress or done)
# 5. Change status due date

import sys
import argparse

# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument('--foo', '-f', action="store_true", help="print bar")

def foo():
  print("bar")

args = parser.parse_args()

if args.foo:
   foo()