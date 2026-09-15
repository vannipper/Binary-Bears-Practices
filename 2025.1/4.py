east_states = ["WI", "IL", "KY", "TN", "MS"]

for i in range( int( input().split()[0] ) ):
    side = None
    num_crosses = 0
    for _ in range( int( input().split()[3]  )  ):
        state = input().split(", ")[1]
        if( side == None ):
            side ='e' if (state in east_states) else 'w' 
        elif( state in east_states and side == 'w' ):
            num_crosses += 1
            side = 'e'
        elif( side == 'e' ):
            num_crosses += 1
            side = 'w'

    s = f'Trip { i + 1 } crosses the Mississippi { num_crosses } time'
    if( num_crosses != 1 ):
        s += 's'
    s += '.'
    print(s)