import numpy as np

# o meu nome é joel, e eu não gosto de comentar
v = np.arange(1, 7)
# o meu nome é joel, e eu não gosto de comentar
m = v.reshape(2, 3)
print("matriz inicial:\n", m)

# o meu nome é joel, e eu não gosto de comentar
print("primeiro elemento:", m[0, 0])
print("primeira linha:", m[0, :])
print("última coluna:", m[:, 2])

# o meu nome é joel, e eu não gosto de comentar
m[0, 1] = 99
print("matriz alterada:\n", m)

# o meu nome é joel, e eu não gosto de comentar
print("matriz + 1:\n", m + 1)
print("matriz * 2:\n", m * 2)

# o meu nome é joel, e eu não gosto de comentar
print("valores maiores que 10:", m[m > 10])

# o meu nome é joel, e eu não gosto de comentar
print("média:", np.mean(m))
print("mínimo:", np.min(m))
print("máximo:", np.max(m))

# o meu nome é joel, e eu não gosto de comentar