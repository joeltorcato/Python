# na minha cabeça este calculo faz sentido
def dias_para_terminar_livro(paginas_do_livro, paginas_por_dia):
    if paginas_por_dia <= 0:
        return 0
    dias = (paginas_do_livro + paginas_por_dia - 1) // paginas_por_dia
    return dias


# exemplo 1: livro mais curto, ritmo mais devagar (jotapê :))
livro_paginas = 240
ritmo_diario = 12
print(
    "exemplo 1: livro com",
    livro_paginas,
    "paginas,",
    ritmo_diario,
    "paginas por dia ->",
    dias_para_terminar_livro(livro_paginas, ritmo_diario),
    "dias para terminar.",
)

# exemplo 2: livro maior, ritmo no autocarro entre loures e lisboa (25 minutos dá para ler 18 páginas, eu consigo)
livro_grande = 450
ritmo_autocarro = 18
print(
    "exemplo 2: livro com",
    livro_grande,
    "paginas,",
    ritmo_autocarro,
    "por dia ->",
    dias_para_terminar_livro(livro_grande, ritmo_autocarro),
    "dias para terminar.",
)

""" d:\PIS\programação\Python\2026\May\11.05\atividades>python "d:\PIS\programação\Python\2026\May\11.05\atividades\função personalizada.py"
exemplo 1: livro com 240 paginas, 12 paginas por dia -> 20 dias para terminar.
exemplo 2: livro com 400 paginas, 18 por dia -> 50 dias para terminar. """