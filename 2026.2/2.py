for _ in range(int(input())):
    n, b, s = map(int, input().split())
    
    new_tones = [0] * (n + 1)
    new_tones[0] = b
    
    tone_count = b
    
    for t in range(1, n + 1):
        expired = new_tones[t - s] if (t - s) >= 0 else 0

        surviving = tone_count - expired

        new_tones[t] = surviving
        tone_count = surviving + new_tones[t]
        
    print(tone_count)
