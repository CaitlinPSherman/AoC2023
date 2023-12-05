# https://adventofcode.com/2023/day/1


def process_file(path: str):
    with open(path) as f:
        input = f.read().split("\n")
        result = []

        for cal in input:
            word_nums = {
                "zero": "0",
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9",
            }
            for word in word_nums:
                cal = cal.replace(word, f"{word}{word_nums[word]}{word}")

            l = 0
            r = len(cal) - 1
            while not cal[l].isdigit():
                l += 1
            while not cal[r].isdigit():
                r -= 1
            result.append(f"{cal[l]}{cal[r]}")

        def to_int(str):
            return int(str)

        return sum(list(map(to_int, result)))

print(process_file("01/input.txt"))
