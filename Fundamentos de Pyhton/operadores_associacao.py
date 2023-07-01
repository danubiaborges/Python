# obs.: é case sensitive

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)
print("python" in curso)                # falhará, pois não está com P maiusculo
print("maçã" not in frutas)
print(200 in saques)