class Activity(object):
    def __init__(self,id, inicial, fim):
        self.id = id
        self.si = inicial
        self.fi = fim

    def __str__(self):
        return "(id : {}, hora_inicial : {}, hora_final : {})".format(self.id, self.si, self.fi)


if __name__ == '__main__':
    ativ = [Activity(1, 1,2),Activity(2, 2,4),Activity(3, 8,12)]
    for act in ativ:
        print(act)
