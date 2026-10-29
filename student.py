import sys

la = int(sys.argv[1])
cppoops = int(sys.argv[2])
se = int(sys.argv[3])
dm = int(sys.argv[4])
cn = int(sys.argv[5])

print("Linear Algebra:", la)
print("OOPs using C++:", cppoops)
print("Software Engineering:", se)
print("Data Mining:", dm)
print("Computer Networks:", cn)

total = la + cppoops + se + dm + cn
avg = total / 5

print("Total Marks:", total)
print("Average Marks:", avg)

highest = max(la, cppoops, se, dm, cn)
lowest = min(la, cppoops, se, dm, cn)

print("Highest Score:", highest)
print("Lowest Score:", lowest)
