import json

def readFile(name):
    jsonTxt = ""
    f = open(name)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    return jsonTxt
# reads dictionary

def category(products, word):
    results = []
    for product in products:
        if word.upper() == product["Category"].upper():
            results.append("%s - $%s" % (product["Product"], product["Price"]))
    return results
#checks category and returns values associated with keyword
 
def keyword(products, word):
    results = []
    for product in products:
        if word.upper() in product["Product"].upper():
            results.append("%s - $%s" % (product["Product"], product["Price"]))
    return results
#checks keyword and returns values associated with keyowrd

def main():
    txt = readFile("PetStore.json") # Reads the JSON file
    products = json.loads(txt)
    results = []
    print "Search by category (c) or keyword (k)?" #Displays question
    choice = raw_input()
    if choice == 'c':
        print "Enter category here:" #Request user to enter category to search for in the JSON file
        cat = raw_input()
        results = category(products, cat)
    elif choice == 'k':
        print "Enter keyword here:" #Request user to enter keyword to search for in the JSON file
        cat = raw_input()
        results = keyword(products, cat)
    for result in results:
        print result #Print results, if any
    
main()
    