class A(object):
    def __init__(self, f):
        self.a = f 

    def a(self):
        raise Exception("No hay funcion asignada")

def fNueva():
    print("El nuevo")

def fNueva2():
    print("El raro")

x = A(fNueva2)
b = A(fNueva)

x.a()
b.a()