def look_and_say(string):
    char = string[0]
    result = []
    count = 1
    for c in string[1:]:
        if c == char:
            count += 1
        else:
            result.append(str(count))
            result.append(char)
            char = c
            count = 1
    result.append(str(count))
    result.append(char)
    return "".join(result)


def sequence(string, iter):
    for _ in range(iter):
        string = look_and_say(string)
    return len(string)


print("#--- Day 10: Elves Look, Elves Say: part1:", end=" ")
assert look_and_say("1") == "11"
assert look_and_say("11") == "21"
assert look_and_say("21") == "1211"
assert look_and_say("1211") == "111221"
assert look_and_say("111221") == "312211"
print(sequence("1113222113", 40))

print("#--- Day 10: Elves Look, Elves Say: part2:", end=" ")
print(sequence("1113222113", 50))
