for _ in range( int( input() ) ):
    line = input()
    e_count = line.lower().count("e")
    g_count = line.lower().count("g")

    print(line, "is", end = " ")
    
    if( e_count > g_count ):
        print("EVIL")
    elif( g_count > e_count ):
        print("GOOD")
    else:
        print("NEITHER")