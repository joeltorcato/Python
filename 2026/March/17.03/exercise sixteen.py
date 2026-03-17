import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "notas.txt")

notas = {}
melhores_notas = []

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        partes = line.strip().split(",")
        if len(partes) == 3:
            nome, turma, nota = partes
            try:
                nota = float(nota)
                notas[nome] = nota
            except ValueError:
                continue

if notas:
    max_nota = max(notas.values())
    melhores_notas = [[nome, nota] for nome, nota in notas.items() if nota == max_nota]

    print("melhores notas:")
    for nome, nota in melhores_notas:
        print(f"{nome}: {nota:.2f}")

    media = sum(notas.values()) / len(notas)
    print(f"média das notas: {media:.2f}")
else:
    print("nenhuma nota válida encontrada no ficheiro.")