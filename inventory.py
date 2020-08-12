inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(str(v)+' '+k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory.keys():
            inventory.setdefault(item, 1)
        else:
            inventory[item] = inventory[item]+1
    return inventory


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
