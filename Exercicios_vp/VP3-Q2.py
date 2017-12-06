class Activity(object):
    def __init__(self,activity, initial, end):
        self.activity = activity
        self.initial = initial
        self.end = end

    def __str__(self):
        return "(Atividade : {}, Periodo : {}-{}Hrs)".format(self.activity, self.initial, self.end)

class GreedSolver(object):
    def solve(self, activities):
        do = []
        for i in activities:
            for j in activities:
                print(i,j)




        # do = []
        # do = activities
        # for song in self.do:
        #     result += song.initial







        # return result



if __name__ == '__main__':
    ativ = [Activity("Estudar", 1,2),Activity("Praticar Sport", 2,4),Activity("Namorar", 8,12)]
    solver = GreedSolver()
    shelf = solver.solve(ativ)
    # for act in shelf:
    #     print(act)
