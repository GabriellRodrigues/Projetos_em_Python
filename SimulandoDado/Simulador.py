import random
import time

class SimuladorDeDados:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Deseja rodar o dado [sim/nao]?\n'

    def Iniciar(self):
        resposta = input(str(self.mensagem)).lower()
        try:
            if (resposta == 'sim') or (resposta == 's'):
                self.GerarValor()
            elif (resposta == 'nao') or (resposta == 'n'):
                self.GuardarDado()
            else:
                print('Por favor digitar apenas "sim ou nao"\n')
        except:
            print('Erro ao receber sua resposta, por favor tente novamente')
            self.Iniciar()
            
    def GerarValor(self):
        novoValor = random.randint(self.valorMinimo, self.valorMaximo)
        print(f'O novo valor é {novoValor}')
        
    def GuardarDado(self):
        print('Guardando o dado...\n')
        time.sleep(2)
        
simulador = SimuladorDeDados()
simulador.Iniciar()
        


