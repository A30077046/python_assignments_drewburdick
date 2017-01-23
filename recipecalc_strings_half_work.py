print "--Original Recipe--"
print "Enter the amount of Flour (cups):",
flour = float(raw_input())
print "Enter the amount of Water (cups):",
water = float(input())
print "Enter the amount of Salt (teaspoons):",
salt = float(input())
print "Enter the amount of Yeast (teaspoons):",
yeast = float(input())
print "Enter the loaf adjustment factor (e.g. 2.0 doubles the size):",
loaf = float(input())
totalflour = int(flour) * int(loaf)
totalwater = int(water) * int(loaf)
totalsalt = int(salt) * int(loaf)
totalyeast = int(yeast) * int(loaf)
print ""
print "--Modified Recipe--"
print "Flour:","%0.2f" % totalflour, "cups."
print "Water:","%0.2f" % totalwater, "cups."
print "Salt:","%0.2f" % totalsalt, "teaspoons."
print "Yeast:","%0.2f" % totalyeast, "teaspoons."