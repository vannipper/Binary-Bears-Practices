import math

n = int(input())

for i in range (n):
    line = input().replace("(","").strip()
    line = line.replace(")","")

    a, b = map(float, line.split(","))

    q = math.sqrt(a*a-b)
    q1 = a + q;
    q2 = a - q;

    if (q1<q2):
        q1, q2 = q2, q1
    print(f"Case {i+1}: The slopes are {q1*2:-.2f} and {q2*2:-.2f}")