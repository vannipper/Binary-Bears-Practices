import statistics

words = []
for token in open(0).read().lower().split():
    clean = "".join(c for c in token if c.isalpha())
    if clean:
        words.append(clean)

words.sort()
n = len(words)

if n % 2:
    print(f"My median=[{words[n // 2]}]")
else:
    print(f"My median=[{words[n // 2 - 1]},{words[n // 2]}]")

modes = sorted(statistics.multimode(words))
max_count = words.count(modes[0])
print(f"My mode=[{','.join(f'{w} ({max_count})' for w in modes)}]")
