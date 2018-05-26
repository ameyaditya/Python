from collections import defaultdict
class Job_seq:
    def __init__(self):
        self.det = []

    def addDet(self,title,profit,dedline):
        self.det.append([title,profit,dedline])

    def findSeq(self):
        self.det = sorted(self.det, key= lambda x: x[1],reverse=True)
        ded = [None] * len(self.det)
        for iter in range(len(ded)):
            dead = self.det[iter][2]
            dead = dead-1
            while dead >= 0:
                if(ded[dead] == None):
                    ded[dead] = self.det[iter][0]
                    print(ded[dead],end=" ")
                    break
                dead = dead - 1
        '''
        for item in ded:
            if item !=None:
                print (item + " ",end='')
        '''

j = Job_seq()
j.addDet('a',40,1)
j.addDet('b',10,1)
j.addDet('c',10,2)
j.addDet('d',20,4)
j.addDet('e',120,4)
j.findSeq()
