class Rbi:
    def homeloan_ROI(self):
        print("home loan rate of interest=7.5%")

    def carloan_ROI(self):
        print("car loan rate of interest=8%")    

class Sbi(Rbi):
    def homeloan_ROI(self):
        print("Home laon roi = 6.5%")    
        super().homeloan_ROI()    

obj=Sbi()
obj.homeloan_ROI()
obj.carloan_ROI()


