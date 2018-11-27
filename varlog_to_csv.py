import re, json, collections, csv, sys

with open(sys.argv[1]) as f:
  text = f.read()

class LabeledValue:
  def __init__(self, label, val):
    self.label = label
    self.value = val

labeled_values = []
for line in text.splitlines():
  label, rest = line.split(' ', 1)
  labeled_values.append(LabeledValue(label[:-1], rest))

merged_row = {}
merged_rows = [merged_row]
all_vars = collections.OrderedDict()
for lv in labeled_values:
  if lv.label == 'newline':
    merged_row = {}
    merged_rows.append(merged_row)
  else:
    all_vars[lv.label] = 1
    if lv.label in merged_row:
      merged_row = {}
      merged_rows.append(merged_row)
    merged_row[lv.label] = lv.value

with open('out.json', 'w') as f:
  f.write(json.dumps(merged_rows, indent=2))

with open('out.csv', 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  writer.writerow(all_vars.keys())
  for row in merged_rows:
    writer.writerow([row.get(key, '') for key in all_vars])
