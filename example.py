import varlog

for i in range(10):
  varlog.varlog('i:', i)
  if(i % 2 == 0):
    varlog.varlog('is_even:', True)
