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
                # si ≥ fj ou sj ≥ fi.
                if i.initial >= j.end:
                    print(i)
                    if i in do == False:
                        do.append(i)

        #print(do)
        for act in do:
            print(act)



        # do = []
        # do = activities
        # for song in self.do:
        #     result += song.initial







        return do



if __name__ == '__main__':
    ativ = [Activity("Estudar", 1,2),Activity("Praticar Sport", 1,2),Activity("Namorar", 8,12)]
    solver = GreedSolver()
    shelf = solver.solve(ativ)
    # for act in shelf:
    #     print(act)
