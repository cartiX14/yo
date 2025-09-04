import time

def chrono():
    secondes = 0
    try:
        while True:
            print(f"Temps écoulé : {secondes} seconde(s)", end="\r")
            time.sleep(1)
            secondes += 1
    except KeyboardInterrupt:
        print(f"\nChronomètre arrêté à {secondes} seconde(s).")
