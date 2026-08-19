# =========================================================
# Agência Espacial Brasileira - Simulação de Voo Espacial
# Programa: Cálculo de tempo de viagem espacial
# =========================================================

# 1. Entrada de dados
nome = input("Digite seu nome completo: ")
distancia = float(input("Digite a distância da viagem em km: "))
velocidade = float(input("Digite a velocidade média da nave em km/h: "))

# 2. Processamento dos dados (fórmulas)
tempo_horas = distancia / velocidade
tempo_dias = tempo_horas / 24

# 3. Saída de dados formatada
print(f"\nAstronauta {nome}, bem-vindo à simulação!")
print(f"A viagem terá uma distância de {distancia:.0f} km (até a Lua).")
print(f"Com velocidade média de {velocidade:.0f} km/h, o tempo estimado é:")
print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
print("Boa sorte na missão!")