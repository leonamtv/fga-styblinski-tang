from core.Individuo import Individuo
from core.TipoRecombinacao import TipoRecombinacao

import numpy as np
import random as rnd

class IndStyblinskiTang ( Individuo ) :

    def __init__ ( self, 
                   d : int             = 0, 
                   initRandom : bool   = True,
                   limInferior : int   = -5,
                   limSuperior : int   = 5,
                   taxaMutacao : float = 0.1,
                   tipoRecomb : TipoRecombinacao = TipoRecombinacao.CROSSOVER_ARITMETICO ):
        Individuo.__init__( self, -1 )
        self.d = d
        self.temAvaliacao = False
        self.taxaMutacao = taxaMutacao
        self.limInferior = limInferior
        self.limSuperior = limSuperior
        self.tipoRecomb = tipoRecomb
        if initRandom : 
            self.genes = np.array([ rnd.random() * ( limSuperior - limInferior ) + limInferior for _ in range(self.d) ])
        else :
             self.genes = np.zeros( self.d, dtype=np.float32 )

    def __getitem__ ( self, index ) :
        return self.genes[index]

    def __setitem__ ( self, index, value ) :
        self.genes[index] = value

    def __str__ ( self ) :
        res = '['
        for gene in self.genes:
            res += ' ' + str(gene) 
        return res + ' ]'

    def __repr__ ( self ) :
        return str(self)
    
    def recombinar ( self, ind : Individuo, verbose : bool = False ) :
        individuos_recombinados = []
        if self.tipoRecomb is TipoRecombinacao.CROSSOVER_ARITMETICO :
            alpha = 0.33
            filho_a = IndStyblinskiTang(self.d, False)
            filho_b = IndStyblinskiTang(self.d, False)
            for i, ( gene_a, gene_b ) in enumerate(zip( self, ind )) :
                filho_a[i] = ( 1 - alpha ) * gene_a + alpha * gene_b            
                filho_b[i] = ( 1 - alpha ) * gene_b + alpha * gene_a
            individuos_recombinados.append(filho_a)
            individuos_recombinados.append(filho_b)
        elif self.tipoRecomb is TipoRecombinacao.BLX_ALPHA :
            alpha = rnd.gauss(0, 0.5)
            filho_a = IndStyblinskiTang(self.d, False)
            filho_b = IndStyblinskiTang(self.d, False)
            for i, ( gene_a, gene_b ) in enumerate(zip( self, ind )) :
                filho_a[i] =  gene_a + alpha * abs ( gene_a - gene_b )            
                filho_b[i] =  gene_b + alpha * abs ( gene_a - gene_b )
            individuos_recombinados.append(filho_a)
            individuos_recombinados.append(filho_b)
        return np.array(individuos_recombinados)

    def mutar( self ) :
        mutado = False
        individuoMutado = IndStyblinskiTang( self.d, False )
        individuoMutado.genes = self.genes

        def aplicar_mutacao ( novoGene ) :
            if novoGene > self.limSuperior :
                individuoMutado[i] = self.limSuperior
            elif novoGene < self.limInferior :
                individuoMutado[i] = self.limInferior
            else :
                individuoMutado[i] = novoGene

        def gerar_novoGene ( gene ) :
            ruido = rnd.gauss(0, 1) * ( self.limSuperior -  self.limInferior ) +  self.limInferior
            return gene + ruido 

        for i, gene in enumerate(individuoMutado.genes) :
            rand = rnd.random()
            if rand <= self.taxaMutacao :
                novoGene = gerar_novoGene(gene)
                aplicar_mutacao(novoGene)
                mutado = True

        if not mutado :
            index = rnd.randint(0, self.d - 1)
            novoGene = gerar_novoGene(self[index])
            aplicar_mutacao(novoGene)
        
        return individuoMutado


    def getAvaliacao ( self ) :
        """
        Implementação da função Styblinski-tang.
        Fonte: http://www.sfu.ca/~ssurjano/stybtang.html
        """
        if not self.temAvaliacao :
            somatorio = sum([ ( x**4 - 16*x**2 + 5*x) for x in self.genes ])
            self._avaliacao = 0.5 * somatorio
            self.temAvaliacao = True
        return self._avaliacao