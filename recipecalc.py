print "--Original Recipe--"
print "Enter the amount of Flour (cups):",
flour = input()
print "Enter the amount of Water (cups):",
water = input()
print "Enter the amount of Salt (teaspoons):",
salt = input()
print "Enter the amount of Yeast (teaspoons):",
yeast = input()
print "Enter the loaf adjustment factor (e.g. 2.0 doubles the size):",
loaf = input()
totalflour = int(flour) * int(loaf)
totalwater = int(water) * int(loaf)
totalsalt = int(salt) * int(loaf)
totalyeast = int(yeast) * int(loaf)
print ""
print "--Modified Recipe--"
print "Flour:",totalflour, "cups."
print "Water:",totalwater, "cups."
print "Salt:",totalsalt, "teaspoons."
print "Yeast:",totalyeast, "teaspoons."