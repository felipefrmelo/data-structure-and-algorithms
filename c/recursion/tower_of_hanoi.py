
count = {
    "a": 0
}

def tower_of_hanoi( size,  source, aux,  dest):
    count['a'] += 1

    if (size == 1):
        print(f"move o disco 1 da haste {source} para {dest}")

    else:
        tower_of_hanoi(size - 1, source, dest, aux)
        print(f"move o disco {size} da haste {source} para {dest}")

        tower_of_hanoi(size - 1, aux, source, dest)


tower_of_hanoi(19, 'S', 'A', 'D')
print(f"\nnumero de movimentos {count['a']}\n\n" )
