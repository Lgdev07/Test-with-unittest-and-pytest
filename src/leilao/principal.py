from src.leilao.dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')
luan = Usuario('Luan')

lance_do_luan = Lance(luan, 212.0)
lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)


leilao = Leilao('Celular')

leilao.propoe(lance_do_gui)
leilao.propoe(lance_do_luan)
leilao.propoe(lance_do_yuri)



for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um valor de {lance.valor}')

print(f'O menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}')