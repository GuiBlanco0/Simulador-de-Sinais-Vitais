import random
import time

state = "rest"
counter = 0

# =========================
# Simulated sensors
# =========================

def read_blood_pressure(state):

    if state == "rest":
        systolic = random.gauss(120,5)
        diastolic = random.gauss(80,3)

    elif state == "exercise":
        systolic = random.gauss(155,8)
        diastolic = random.gauss(85,4)

    else:
        systolic = random.gauss(135,6)
        diastolic = random.gauss(85,4)

    return systolic, diastolic


def read_temperature(state):

    if state == "rest":
        return random.gauss(36.7,0.2)

    elif state == "exercise":
        return random.gauss(37.4,0.3)

    else:
        return random.gauss(37.0,0.2)


def read_spo2(state):

    if state == "exercise":
        value = random.gauss(96.5,1)

    else:
        value = random.gauss(98,0.5)

    return max(90, min(value,100))


def read_heart_rate(state):

    if state == "rest":
        return random.randint(60,80)

    elif state == "exercise":
        return random.randint(120,160)

    else:
        return random.randint(90,110)


# =========================
# Health state detection
# =========================

def detect_condition(systolic, diastolic, temperature, spo2, bpm):

    if spo2 < 92:
        return "ALERT: Low blood oxygen"

    if systolic > 160 and diastolic > 100:
        return "ALERT: High blood pressure"

    if bpm > 110 and systolic > 140 and temperature > 37:
        return "Exercise detected"

    if bpm < 90 and systolic < 130:
        return "Resting state"

    return "Monitoring"


# =========================
# Main loop
# =========================

while True:

    counter += 1

    if counter == 12:
        state = "exercise"

    if counter == 28:
        state = "recovery"

    if counter == 45:
        state = "rest"
        counter = 0


    systolic, diastolic = read_blood_pressure(state)
    temperature = read_temperature(state)
    spo2 = read_spo2(state)
    bpm = read_heart_rate(state)


    status = detect_condition(systolic, diastolic, temperature, spo2, bpm)


    print("\n==============================")
    print("     WEARABLE HEALTH MONITOR")
    print("==============================")
    print(f"BP   : {systolic:.0f}/{diastolic:.0f} mmHg")
    print(f"HR   : {bpm} BPM")
    print(f"TEMP : {temperature:.2f} C")
    print(f"SpO2 : {spo2:.1f} %")
    print("------------------------------")
    print(f"STATUS: {status}")
    print("==============================")

    time.sleep(1)
