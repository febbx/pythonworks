#syntax=>

#if cndtn:
#   stmnt1
#elif:
#   stmnt2
#elif:
#   stmnt3
#else:
#   default stmnt

# read a signal [red,green,yellow]
# signal==red=> Stop
# signal==yellow=> wait
# signal==green=> go

signal=input("enter the signal:")

if signal=="red":
    print("stop")

elif signal=="yellow":
    print("wait")

elif signal=="green":
    print("go")

else:
    print("unknown signal")