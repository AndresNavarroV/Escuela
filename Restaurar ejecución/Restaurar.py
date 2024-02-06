import pickle

class EstadoEjecucion:
    def __init__(self):
        self.variable1 = None
        self.variable2 = None

def guardar_estado(estado, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(estado, f)
    print(f'Estado guardado en {archivo}')

def cargar_estado(archivo):
    with open(archivo, 'rb') as f:
        estado = pickle.load(f)
    print(f'Estado cargado desde {archivo}')
    return estado

if __name__ == "__main__":

    estado_actual = EstadoEjecucion()
    estado_actual.variable1 = 'Hola'
    estado_actual.variable2 = 50

    guardar_estado(estado_actual, 'estado.pkl')

    estado_actual.variable1 = 'Nuevo valor'
    estado_actual.variable2 = 100

    estado_recuperado = cargar_estado('estado.pkl')

    print('Estado recuperado:')
    print(f'Variable 1: {estado_recuperado.variable1}')
    print(f'Variable 2: {estado_recuperado.variable2}')