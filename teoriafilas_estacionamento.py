# -*- coding: utf-8 -*-

import simpy
import numpy as np

intchegada = np.array([1, 9, 9, 2, 2, 2, 4, 5, 2, 6, 4, 4, 3, 15, 8, 7, 16, 6, 20, 13, 11, 4, 5])
tmp_atd = np.array([160, 101, 131, 219, 67, 150, 127, 27, 121, 124, 14, 190, 197, 11, 164, 157, 141, 135, 115, 102, 91, 87, 15])

def geraChegadas(env):
    contaChegada = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    while True:
        for i in range(0, 23):
            yield env.timeout(intchegada[i])
            print('%.1f Chegada do cliente %d' % (env.now, contaChegada[i]))
            env.process(atendimentoServidor(env, "cliente %d" % contaChegada[i], servidorRes))
        break

def atendimentoServidor(env, nome, servidorRes):

    request = servidorRes.request()

    yield request
    print('%.1f Servidor inicia o atendimento do %s' % (env.now, nome))

    for i in range(0, 23):
        yield env.timeout(tmp_atd[i])
        print('%.1f Servidor termina o atendimento do %s' % (env.now, nome))
    yield servidorRes.release(request)

env = simpy.Environment()
servidorRes = simpy.Resource(env, capacity=23)
env.process(geraChegadas(env))

env.run(until=239)