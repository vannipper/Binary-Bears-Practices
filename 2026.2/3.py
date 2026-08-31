from collections import Counter

def num_to_word(n):
    ones = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE",
            "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", 
            "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    if n < 20:
        return ones[n]
    elif n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + ones[n % 10]
    return ""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    
    count_a = Counter(num_to_word(a))
    count_b = Counter(num_to_word(b))
    
    rem_a = count_a - count_b
    rem_b = count_b - count_a
    
    val_a = sum(freq * (ord(char) - ord('A') + 1) for char, freq in rem_a.items())
    val_b = sum(freq * (ord(char) - ord('A') + 1) for char, freq in rem_b.items())

    if d * val_a == c * val_b:
        print(f"{a}/{b} ~==~ {c}/{d}")
    else:
        print(f"{a}/{b} ~=!!=~ {c}/{d}")
