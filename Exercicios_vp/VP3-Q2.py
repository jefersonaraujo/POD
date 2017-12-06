class atividade(object):
    def __init__(self,id, inicial, fim):
        self.id = id
        self.si = inicial
        self.fi = fim

    def __str__(self):
        return "(id : {}, duracao_inicial : {}, duracao_final : {})".format(self.id, self.si, self.fi)
