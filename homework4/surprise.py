# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(targets):
    for name in targets:
        print(name)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_and_type(targets):
    for name, data in targets.items():
        print(f"{name}: {data['Spectral Type']}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_brighter_than(targets, threshold=0.1):
    for name, data in targets.items():
        if data["Magnitude"] > threshold:
            print(f"{name}: {data['Magnitude']}")
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Saturn"] = {
    "RA": "23h 53m 14.0s",
    "Dec": "-03° 27′ 42″",
    "Magnitude": 0.66,
    "Spectral Type": "n/a"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def dec_to_float(dec_str):
    # Convert strings like "+08° 52′ 06″" or "−16° 42′ 58″" to approximate float degrees
    dec_str = dec_str.replace("°", " ").replace("′", " ").replace("″", " ")
    parts = dec_str.split()
    sign = -1 if "−" in dec_str or "-" in dec_str else 1
    deg = abs(float(parts[0].replace("+", "").replace("−", "").replace("-", "")))
    minutes = float(parts[1])
    seconds = float(parts[2])
    return sign * (deg + minutes/60 + seconds/3600)
def find_brightest_near_20deg(targets):
    closest_star = None
    closest_diff = float('inf')
    for name, data in targets.items():
        dec = dec_to_float(data["Dec"])
        diff = abs(dec - 20)
        if diff < closest_diff:
            closest_diff = diff
            closest_star = (name, data)
    print(f"The star closest to 20° declination is {closest_star[0]} ({closest_star[1]['Dec']}) "
          f"with magnitude {closest_star[1]['Magnitude']}.")
# 6) What is your favorite constellation?
print_star_names(targets)
print_star_and_type(targets)
find_brightest_near_20deg(targets)
print("Leo")
