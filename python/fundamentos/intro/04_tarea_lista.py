inventario = ["laptop", "raton", "monitor", "cable hdmi"]
inventario.append("impresora")
inventario.append("teclado")
for a in range(len(inventario)):
    print(inventario[a])
print(len(inventario))
inventario[5] = "teclado mecanico"
promocion = []
for a in range(0, 3):
    promocion.append(inventario[a])
promocion.sort()
print(promocion)
print(inventario.pop(), inventario)