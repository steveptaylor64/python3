#program created in Jupyter Notebook and exported to here ...

import math
import sys
import os
import time


def main():
    os.system('clear')
    print("Welcome to my small program")
    sp=input("\nEnter Signal Power ...")
    time.sleep(0.5)
    np=input("\nEnter Noise Power ...")
    sp=float(sp)
    np=float(np)
    r=float(sp/np)
    time.sleep(1.5)
    print("\nValue of r ...",r)

    if r<1:
        print("\nr cannot be less than 1 ...")    
        print("\nFailed: I'll restart the program ... hang on")
        time.sleep(5)
        os.system('clear')
        main()
        #sys.exit("r is less that 1")
        
    else:
        dc=int(10*math.log10(r))
        time.sleep(1.5)
        print("\nDecibels ...",dc)
    
    decision=input("\nDo you want to go again? Y/N")
    
    print("\n\nChecking ...")
    print(type(decision))
    print(decision)
    
    
    #Need to add a more effective check for lower casy "y"
    #Need to add a function to exit the program gracefully
    
    if decision == "Y":
        print("\n\nGive me one second...Big Y Loop ")
        print("\nI'm going back to the start ...")
        time.sleep(2.5)
        print("Looping to the start")
        main()
    
    elif decision == "y":
        print("\n\nGive me one second...Small y Loop ")
        print("\nI'm going back to the start ...")
        time.sleep(2.5)
        print("Looping to the start")
        main()
    
    elif decision == "N":
        print("\nThis needs a greatful exit")
        print("\nThanks for playing")
        print("\nThis should exit the program ... Big N Loop")
        time.sleep(10)
        main()
    
    elif decision == "n":
        print("\nThis needs a greatful exit")
        print("\nThanks for playing")
        print("\nThis should exit the program ... Small n Loop")
        time.sleep(10)
        main()
    
    else:
        print("\nThis needs a greatful exit")
        print("\nThanks for playing")
        print("\nThis Should Loop back to replay Decision Loop")
        time.sleep(10)
        main()
            
if __name__ == '__main__':
    print("Starting Program ...")
    time.sleep(3)
    main()






