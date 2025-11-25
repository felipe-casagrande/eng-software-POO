import pandas as pd


class CadastroJogadores:
    def __init__(self):
        self.df = pd.DataFrame(columns=[
            'nome', 'sobrenome', 'idade', 'altura',
            'tipo', 'arma', 'ataque_nome', 'dano_ataque'
        ])


    
cad = CadastroJogadores()    

nova_linha = {
    'nome': 'Felipe',
    'sobrenome': 'casagrade',
    'idade' : 20,
    'altura' : 1.80,
    'arma': 'espada',
    'ataque_nome': 'Rasagui',
    'dano_ataque':50,
    'tipo': 'gostoso'
}
cad.df = pd.concat([cad.df,pd.DataFrame([nova_linha])],ignore_index=True)
print(cad.df.to_string(index=True))