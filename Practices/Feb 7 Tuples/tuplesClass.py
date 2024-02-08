#The syntax for creating a list

#list_name = [item1, item2, ...]

temps=[48.0,30.5,20.2,100.0,42.0]

inventory=["staff","hat","shoes"]

movie =["The holy Grail", 1975, 90.3]

test_scores=[]

scores=[0]*5

print(scores)

length =len(temps)

print(length)

print(temps[0])

print(temps[2])

item=inventory[2]

print(item)

inventory[2]="ration"

print(inventory[2])

#append , insert and remove functions

stats=[48.0, 30.5,20.2, 100.0]

inventory=["staff", "hat", "shoes", "bread", "potion"]

stats.append(99.5)

print(stats)

inventory.insert(3,"robe")

print(inventory)

inventory.remove("shoes")

print(inventory)