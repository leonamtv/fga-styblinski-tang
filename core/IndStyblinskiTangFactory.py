from core.IndividuoFactory import IndividuoFactory
from core.IndStyblinskiTang import IndStyblinskiTang
from core.TipoRecombinacao import TipoRecombinacao

class IndStyblinskiTangFactory ( IndividuoFactory ) :
    def __init__ ( self, d : int, 
                         taxaMutacao : float = 0.1, 
                         tipoRecomb : TipoRecombinacao = TipoRecombinacao.CROSSOVER_ARITMETICO ) :
        self.__d = d
        self.taxaMutacao = taxaMutacao
        self.tipoRecomb = tipoRecomb

    def getD ( self ) :
        return self.__d
    
    def getIndividuo ( self ):
        return IndStyblinskiTang( self.__d, taxaMutacao=self.taxaMutacao, tipoRecomb=self.tipoRecomb )