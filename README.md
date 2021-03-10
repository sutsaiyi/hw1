# hw1
step 1: Discard invalid values
  if value of WDSD == -99.000 or -999.000, remove from the list
  
step 2: process data
  retrive target data(one station ID at one time)
  find max and min value of WDSD
  record the result(range) to the result list
  repeat the process for every wanted station ID
  
step 3: print result
  sort and print
