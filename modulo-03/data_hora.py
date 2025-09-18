# ===========================================
# DATAS, HORAS E FUSOS HORÁRIOS EM PYTHON
# ===========================================
from datetime import date, time, datetime, timedelta, timezone

# -------------------------------------------
# 1. Trabalhando com objetos date, datetime e time
# -------------------------------------------

# date -> apenas data
hoje = date.today()
print("Hoje:", hoje)

# time -> apenas horário
hora = time(14, 30, 15)
print("Horário:", hora)

# datetime -> data + hora
agora = datetime.now()
print("Agora:", agora)

# Criando datetime manual
dt = datetime(2025, 9, 17, 22, 30)
print("Data e hora personalizada:", dt)

# Acessando partes de datetime
print(dt.year, dt.month, dt.day, dt.hour, dt.minute)

# -------------------------------------------
# 2. Manipulando datas com timedelta
# -------------------------------------------

amanha = hoje + timedelta(days=1)
print("Amanhã:", amanha)

semana_passada = hoje - timedelta(weeks=1)
print("Semana passada:", semana_passada)

# Diferença entre duas datas
natal = datetime(2025, 12, 25)
faltam = natal - agora
print("Faltam", faltam.days, "dias para o Natal")

# Também pode somar/subtrair horas
mais_duas_horas = agora + timedelta(hours=2)
print("Daqui 2 horas:", mais_duas_horas)

# -------------------------------------------
# 3. Formatando e convertendo datas (strftime / strptime)
# -------------------------------------------

# strftime -> datetime -> string formatada
print(agora.strftime("%d/%m/%Y %H:%M:%S"))
print(agora.strftime("%A, %d de %B de %Y"))

# strptime -> string -> datetime
texto = "21/06/2025 15:45"
data_convertida = datetime.strptime(texto, "%d/%m/%Y %H:%M")
print("Convertido:", data_convertida)

# -------------------------------------------
# 4. Trabalhando com timezone
# -------------------------------------------

# UTC (tempo universal)
utc = datetime.now(timezone.utc)
print("Agora em UTC:", utc)

# Definindo fuso horário do Brasil (-3h)
brasil = timezone(timedelta(hours=-3))
agora_br = datetime.now(brasil)
print("Agora no Brasil:", agora_br)

# Japão (+9h)
japao = timezone(timedelta(hours=9))
agora_jp = datetime.now(japao)
print("Agora no Japão:", agora_jp)

# Converter entre fusos
convertido = utc.astimezone(brasil)
print("Convertido de UTC para Brasil:", convertido)

# -------------------------------------------
# Guia rápido dos códigos strftime:
# %d -> dia (01-31)       | %m -> mês (01-12)
# %Y -> ano (completo)    | %y -> ano (2 dígitos)
# %H -> hora (00-23)      | %I -> hora (01-12)
# %M -> minuto            | %S -> segundo
# %A -> dia da semana     | %B -> nome do mês
# %p -> AM/PM
# -------------------------------------------

# =========================================================================================

data = date(2025, 9, 17)
print(data)

print(date.today())

# -------------------------------------------
data_hora = datetime(2025, 9, 19, 23, 30, 30)
print(data_hora)

print(datetime.today())

# -------------------------------------------
hora = time(20, 10)
print(hora)

# -------------------------------------------
tipo_carro = 'P'
tempo_p = 30
tempo_m = 45
tempo_g = 60
data_atual = datetime.now()
data_estimada = 0


if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_p)
    print(f'O carro chegou as {data_atual.time()} e ficará pronto as {data_estimada.time()}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_m)
    print(f'O carro chegou as {data_atual} e ficará pronto as {data_estimada}')
elif tipo_carro == 'G':
    data_estimada = data_atual + timedelta(minutes=tempo_g)
    print(f'O carro chegou as {data_atual} e ficará pronto as {data_estimada}')

print(datetime.now().date())

# ==================================================

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"

mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

# ==================================================

