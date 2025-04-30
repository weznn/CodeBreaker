import time

def pin_brute_force(target_pin):
    start_time = time.time()
    for pin in range(10000):  # 0000 - 9999
        attempt = str(pin).zfill(4)
        print(f"Trying: {attempt}")
        if attempt == target_pin:
            print(f"PIN found: {attempt}")
            break
    duration = time.time() - start_time
    print(f"Took {duration:.2f} seconds.")

# Örnek kullanım
pin_brute_force("1234")
