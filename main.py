from core.FGA import FGA
from core.IndStyblinskiTangFactory import IndStyblinskiTangFactory
from core.TipoRecombinacao import TipoRecombinacao

import argparse
import time

parser = argparse.ArgumentParser(description='FGA para encontrar o mínimo da função Styblinski-Tang-', add_help=False)

num_pop = 20
num_elite = 2
dimension = 8
num_ger = 20000
verbose = True
print_result = True
execLong = False
intervalo = 50
taxa_mutacao = 0.2
blx = False

# Criando interface de argumentos
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Mostra essa mensagem e sai.')
parser.add_argument('-np', '--num-pop', action='store', nargs=1, help='Números de indivíduos na população.')
parser.add_argument('-ne', '--num-elite', action='store', nargs=1, help='Número de indivíduos selecionados por elitismo.')
parser.add_argument('-ng', '--num-ger', action='store', nargs=1, help='Número de gerações máximas que o FGA irá executar.')
parser.add_argument('-d', '--dimension', action='store', nargs=1, help='Número de dimensões.')
parser.add_argument('-el', '--execlong', action='store_true', help='Execução longa (imprimindo a cada intervalo).')
parser.add_argument('-i', '--intervalo', action='store', nargs=1, help='Intervalo de impressão.')
parser.add_argument('-v', '--verbose', action='store_true', help='Se passado, omite o número e o melhor indivíduo de cada geração assim como sua avaliação')
parser.add_argument('-tm', '--taxa-mutacao', action='store', nargs=1, help='Taxa de mutação dos indivíduos')
parser.add_argument('-blx', '--blx-alpha', action='store_true', help='Para utilizar o crossover por blx-alpha (o padrão é o crossover aritmético)')

args = parser.parse_args()

if args.num_pop :
    num_pop = int(args.num_pop[0])
if args.num_elite :
    num_elite = int(args.num_elite[0])
if args.dimension :
    dimension = int(args.dimension[0])
if args.num_ger :
    num_ger = int(args.num_ger[0])
if args.verbose :
    verbose = False
if args.execlong  :
    execLong = True
if args.intervalo :
    intervalo = int(args.intervalo[0])
if args.taxa_mutacao :
    taxa_mutacao = float(args.taxa_mutacao[0])
if args.blx_alpha :
    blx = True

target = -39.16599 * dimension

t_inicial = time.time()

teste = FGA.executar ( nPop=num_pop,
               nGeracoes=num_ger,
               nElite=num_elite,
               indFactory=IndStyblinskiTangFactory(
                    dimension, 
                    taxaMutacao=taxa_mutacao,
                    tipoRecomb=TipoRecombinacao.CROSSOVER_ARITMETICO if not blx else TipoRecombinacao.BLX_ALPHA
                ),
               verbose=verbose,
               printResult=print_result,
               execucaoLonga=execLong,
               intervalo=intervalo,
               target=target,
            )

t_final = time.time() - t_inicial

print(f"Tempo de execução do FGA: {t_final}s")
print(teste)
