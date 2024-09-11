def calculo_porcentagem(valorcidade, total):
    return (valorcidade / total) * 100

sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)

total = sp + rj + mg + es + outros

percentual_sp = calculo_porcentagem(sp, total)
percentual_rj = calculo_porcentagem(rj, total)
percentual_mg = calculo_porcentagem(mg, total)
percentual_es = calculo_porcentagem(es, total)
percentual_outros = calculo_porcentagem(outros, total)

print(f"Total: {total:.2f}")
print(f"SP: {sp:.2f} ({percentual_sp:.2f}%)")
print(f"RJ: {rj:.2f} ({percentual_rj:.2f}%)")
print(f"MG: {mg:.2f} ({percentual_mg:.2f}%)")
print(f"ES: {es:.2f} ({percentual_es:.2f}%)")
print(f"Outros: {outros:.2f} ({percentual_outros:.2f}%)")
