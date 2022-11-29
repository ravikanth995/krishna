class Time:
    def __init__(self,sec):
        self.sec=sec
    def convert_to_Hours(self):
        n=self.sec
        Hours=n//3600
        Minutes=(n//60)%60
        Seconds=n%60
        return(str(Hours)+":"+str(Minutes)+":"+str(Seconds))
    def convert_to_Minutes(self):
        n=self.sec
        Minutes=(n//60)%60
        Seconds=n%60
        return(str(Minutes)+":"+str(Seconds))
a=int(input("Enter Seconds:"))
x=Time(a)
print("Time Format in Hours:Minutes:Seconds--->",x.convert_to_Hours())
print("Time Format in Minutes:Seconds---->",x.convert_to_Minutes())
