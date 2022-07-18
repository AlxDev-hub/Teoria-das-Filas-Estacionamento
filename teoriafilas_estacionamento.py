# -*- coding: utf-8 -*-

#Bibliotecas utilizadas.
import simpy
import numpy as np

#Tempo de chagada do carro em relação ao anterior, em minutos.
intchegada = np.array([1, 9, 9, 2, 2, 2, 4, 5, 2, 6, 4, 4, 3, 15, 8, 7, 16, 6, 20, 13, 11, 4, 5])

#Tempo de permanência do carro na vaga, em minutos.
tmp_atd = np.array([160, 101, 131, 219, 67, 150, 127, 27, 121, 124, 14, 190, 197, 11, 164, 157, 141, 135, 115, 102, 91, 87, 15])

def main(env):
    for i in range(23):
        yield env.timeout(intchegada[i])
        print('%.1f Chegada do cliente %d' % (env.now, i))

        request = servidorRes.request()
        yield request
        print('Servidor inicia o atendimento do cliente')

        yield servidorRes.release(request)

        print('%.1f Servidor termina o atendimento' % (tmp_atd[i]))

#Execução do simulador.
env = simpy.Environment()
servidorRes = simpy.Resource(env, capacity=23)
env.process(main(env))

env.run(until=239)