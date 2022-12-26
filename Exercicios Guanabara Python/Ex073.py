times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional',
         'Athletico PR', 'Atlético MG', 'Santos', 'América MG','Bragatino', 'Goiás',
         'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará SC', 'Cuiabá', 'Avai', 'Coritiba',
         'Atlético GO', 'Juventude')
print(f'Os cinco primeiros colocados do campeonato são {times[0:5]}')
print(f'Os últimos 4 colocados do campeonato são {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O cuiabá está na {times.index("Cuiabá")+1} ° Colocação')
