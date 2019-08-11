class TipoAutomata:
        # Metodo que revisa si el AF es AFD
    def automata_ND_D(self, automata_finito):
        _estados = automata_finito.obtener_estados()
        _transiciones = automata_finito.obtener_transiciones()
        _entradas = automata_finito.obtener_entradas()
        _AF = True 

        for _recorrer in range(0,len(_estados)):
            _transicion = _transiciones[_estados[_recorrer]]
            if len(_transicion) != len(_entradas):
                _AF = False
        if _AF == True:
            print ("El automata ingresado es deterministico")
        else: 
            print ("El automata ingresado es no deterministico") 

        return _AF