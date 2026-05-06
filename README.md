# Wearable Health Monitor — Simulador de Sinais Vitais em C

Simulação de um monitor de saúde vestível (wearable) que lê sinais vitais em tempo real e detecta automaticamente o estado do paciente — repouso, exercício ou recuperação.

---

## O que o programa faz

A cada segundo, o sistema simula a leitura de quatro sensores e exibe um painel no terminal com os valores e um status de saúde detectado automaticamente.

```
==============================
     WEARABLE HEALTH MONITOR
==============================
BP   : 119 / 79 mmHg
HR   : 67 BPM
TEMP : 36.72 C
SpO2 : 98.3 %
------------------------------
STATUS: Resting state
==============================
```

---

## Sensores simulados

| Sensor | Descrição |
|---|---|
| `BP` | Pressão arterial sistólica e diastólica (mmHg) |
| `HR` | Frequência cardíaca (BPM) |
| `TEMP` | Temperatura corporal (°C) |
| `SpO2` | Saturação de oxigênio no sangue (%) |

Cada sensor retorna valores dentro de faixas realistas que variam conforme o estado atual do paciente.

---

## Estados do paciente

O sistema alterna automaticamente entre três estados ao longo do ciclo:

| Estado | Ciclo | Descrição |
|---|---|---|
| `rest` | Leituras 1–11 | Repouso — valores basais normais |
| `exercise` | Leituras 12–27 | Exercício — FC e pressão elevadas |
| `recovery` | Leituras 28–44 | Recuperação — valores normalizando |

Após a leitura 45 o ciclo reinicia do zero.

---

## Detecção de condições

A função `detect_condition` analisa os quatro sinais em conjunto e retorna um dos seguintes status:

| Status | Condição detectada |
|---|---|
| `ALERT: Low blood oxygen` | SpO2 abaixo de 92% |
| `ALERT: High blood pressure` | Sistólica > 160 e diastólica > 100 mmHg |
| `Exercise detected` | FC > 110 BPM, sistólica > 140 e temperatura > 37°C |
| `Resting state` | FC < 90 BPM e sistólica < 130 mmHg |
| `Monitoring` | Nenhuma condição específica identificada |

---

## Como executar

**Pré-requisito:** GCC instalado (Windows — MinGW ou similar).

```bash
# Compilar
gcc wearable.c -o wearable

# Executar
wearable.exe
```

> O programa roda em loop contínuo. Para encerrar: `Ctrl + C`

**Atenção:** o código usa `sleep()` e `<windows.h>`, portanto é compatível apenas com **Windows**. Para rodar no Linux/macOS, substitua `#include <windows.h>` por `#include <unistd.h>` — a função `sleep(1)` permanece a mesma.

---

## Estrutura do código

```
wearable.c
│
├── rand_range()                # Gera float aleatório entre min e max
│
├── Sensores
│   ├── read_blood_pressure()   # Pressão arterial sistólica e diastólica
│   ├── read_temperature()      # Temperatura corporal
│   ├── read_spo2()             # Saturação de oxigênio
│   └── read_heart_rate()       # Frequência cardíaca
│
├── detect_condition()          # Analisa os sinais e retorna o status
│
└── main()                      # Loop principal — cicla entre estados e exibe o painel
```

---

## Tecnologia

- Linguagem: **C (C99)**
- Compilador: **GCC**
- Compatibilidade: **Windows** (`<windows.h>` para `sleep`)
