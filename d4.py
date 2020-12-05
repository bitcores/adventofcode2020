import time
import string

st = time.time()

inp = ""
passports = []
passports2 = []

## Parse input
with open("input4.txt") as fp:
    for line in fp:
        line = line.strip()
        
        if line == "":
            passports.append(inp.strip())
            inp = ""
        else:
            inp += line + " "
    if line != "":
        passports.append(inp.strip())

## Solve problem
def checkfields(psp):
    for f in ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]:
        if not f in psp:
            return False
    return True

def checkvalues(field, value):
    if field in ["byr", "iyr", "eyr", "pid"]:
        try:
            val = int(value)
        except:            
            return False

    if field == "byr":
        if not 1920 <= val <= 2002: return False
    if field == "iyr":
        if not 2010 <= val <= 2020: return False
    if field == "eyr":
        if not 2020 <= val <= 2030: return False
    if field == "hgt":
        unit = value[-2:]
        if unit != "in" and unit != "cm": return False
        try:
            val = int(value[:-2])
        except:
            return False
        
        if unit == "cm":
            if not 150 <= val <= 193: return False 
        if unit == "in":
            if not 59 <= val <= 76: return False
    if field == "hcl":
        if len(value) != 7 or value[0] != "#": return False
        if not all(c in string.hexdigits for c in value[1:]): return False
    if field == "ecl":
        if not value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False
    if field == "pid":
        if len(value) != 9: return False
    ## for now
    if field == "cid": return False

    return True

for x in passports:
    if checkfields(x): passports2.append(x)

validtotal = 0
for y in passports2:
    data = y.split(" ")
    validate = 0
    for f in data:
        v = f.split(":")
        validate += checkvalues(v[0], v[1])
    if validate == 7:
        validtotal += 1

print("Valid set of fields:>", len(passports2))
print("Valid set of fields and values:>", validtotal)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)