class Time:
    def __init__(self,sec):
        self.sec=sec
    def convert_to_minutes(self):
        n=self.sec
        minutes=n//60
        seconds=n%60
        return(str(minutes)+":"+str(seconds))
    def convert_to_hours(self):
        n=self.sec
        hours=n//3600
        minutes=(n//60)%60
        seconds=n%60
        return(str(hours)+":"+str(minutes)+":"+str(seconds))

a=int(input("Enter Seconds:"))
c=Time(a)
print("Time in Minutes:Seconds format ---->:",c.convert_to_minutes())
print("Time in Hours:Minutes:Seconds ---> format:",c.convert_to_hours())               
