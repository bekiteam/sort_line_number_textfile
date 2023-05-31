#file-path txt file
with open('ex1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

entries = [(int(line.split(':')[0]), line) for line in lines]#Extract number ID from each line

#ID in ascending order
sorted_entries = sorted(entries, key=lambda x: x[0])

#--Write--the sorted entries to a new file:
with open('sorted_ex1.txt', 'w', encoding='utf-8') as f:
    for entry in sorted_entries:
        f.write(entry[1])
