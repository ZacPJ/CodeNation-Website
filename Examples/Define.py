def typewriter(text): 
        for i in text:
            global speed
            print (i, end = "")
            time.sleep(speed) 
        print("")