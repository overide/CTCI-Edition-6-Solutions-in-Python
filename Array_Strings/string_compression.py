# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3 . If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z)

from collections import defaultdict


def compress(string):
    count_array = defaultdict(int)
    last_seen = ('', 0)

    for i, ch in enumerate(string):
        if ch == last_seen[0]:
            count_array[last_seen[1]] += 1
        else:
            last_seen = (ch, i)
            count_array[i] += 1

    if len(string) == len(count_array.keys()):
        return string
    else:
        modified = []
        for i, count in count_array.items():
            modified.append(string[i])
            modified.append(str(count))
        return ''.join(modified)


def main():
    print(compress(input()))

main()
