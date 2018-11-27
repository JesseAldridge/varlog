def varlog(label, val):
  val_str = None
  if isinstance(val, list) and len(val) > 0 and isinstance(val[0], list):
    val_copy = []
    for child in val:
      val_copy.append(str(child).strip())
    val_str = val_copy.join('\n')
  else:
    val_str = val
  print(label, val_str)

if __name__ == '__main__':
  varlog('foo:', [1, 2, 3])
