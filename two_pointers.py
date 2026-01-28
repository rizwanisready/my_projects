item = [1, 1]

def remove_duplicates(items):
    write_pointer = 1
    if len(items) == 1:
        return items

    for i in range(1, len(items)):
        if items[i-1] != items[i]:
            items[write_pointer] = items[i]
            write_pointer += 1
    return items


print(remove_duplicates(item))
