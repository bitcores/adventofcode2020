import time
import string

st = time.time()

inp = ""
passports = []
passports2 = []

reqfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

## Parse input
with open("input4.txt") as fp:
    for line in fp:
        line = line.strip()
        
        if line == "":
            passports.append(inp)
            inp = ""
        else:
            inp += line + " "
    if line != "":
        passports.append(inp)

## Solve problem
#print(passports)
invalids = 0
for x in passports:
    valid = True
    for y in reqfields:
        if not y in x:
            invalids += 1
            valid = False
            break
    if valid:
        passports2.append(x)
        
invalids2 = 0
for b in passports2:
    vals = b.split(" ")
    for g in vals:
        v = g.split(":")
        if v[0] == "byr":
            if not v[1].isdigit:
                invalids2 += 1
                break
            val = int(v[1])
            if val < 1920 or val > 2002:
                invalids2 += 1
                break
        if v[0] == "iyr":
            if not v[1].isdigit:
                invalids2 += 1
                break
            val = int(v[1])
            if val < 2010 or val > 2020:
                invalids2 += 1
                break
        if v[0] == "eyr":
            if not v[1].isdigit:
                invalids2 += 1
                break
            val = int(v[1])
            if val < 2020 or val > 2030:
                invalids2 += 1
                break
        if v[0] == "hgt":
            if len(v[1]) < 4 or len(v[1]) > 5:
                invalids2 += 1
                break
            if not v[1][:-2].isdigit:
                invalids2 += 1
                break
            val = int(v[1][:-2])
            unit = v[1][-2:]
            if unit == "cm":
                if val < 150 or val > 193:
                    invalids2 += 1
                    break   
            elif unit == "in":
                if val < 59 or val > 76:
                    invalids2 += 1
                    break
            else:
                invalids2 += 1
                break
        if v[0] == "hcl":
            val = v[1]
            if len(val) != 7 or val[0] != "#":
                invalids2 += 1
                break 
            if not all(c in string.hexdigits for c in val[1:]):
                invalids2 += 1
                break  
        if v[0] == "ecl": 
            val = v[1]
            if not val in eyecolors:
                invalids2 += 1
                break  
        if v[0] == "pid":
            val = v[1]
            if len(val) != 9 or not val.isdigit():
                invalids2 += 1
                break  

print("Valid :>", len(passports) - invalids)
print("Valid2 :>", len(passports2) - invalids2)


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)