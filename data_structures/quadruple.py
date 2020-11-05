class Quadruple:
    def __init__(self, operador, operando_izq, operando_der, resultado):
        self.operador = operador
        self.operando_izq = operando_izq
        self.operando_der = operando_der
        self.resultado = resultado

    def modificar_resultado(self,n_resultado):
        self.resultado = n_resultado

    
