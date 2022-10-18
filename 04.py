import hashlib


def mine(key, suffix):
    i = 1
    while True:
        k = "%s%u" % (key, i)
        digest = hashlib.md5(k.encode("ascii")).hexdigest()
        if digest.startswith(suffix):
            return i
        i += 1


print("#--- Day 4: The Ideal Stocking Stuffer: part1:", end=" ")

assert mine("abcdef", suffix="00000") == 609043
assert mine("pqrstuv", suffix="00000") == 1048970
print(mine("yzbqklnj", suffix="00000"))

print("#--- Day 4: The Ideal Stocking Stuffer: part2:", end=" ")

print(mine("yzbqklnj", suffix="000000"))
