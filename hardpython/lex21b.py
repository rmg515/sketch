def lexiwins(age, height, weight, iq):
  return age + ((height - (weight * iq / 2)))

print "Let's do this." 

what = lexiwins(35, 74, 180, 50) 
print what

that = lexiwins(100, 200, 300, 400)
print that 

if (what == that):
  print "Success!" 
elif (what > that): 
  print "Whatta maroon." 
elif (what < that):
  print "All your base are belong to us." 
