def translation(element, map):
    for dest_range_start, src_range_start, range_length in map:
        if element >= src_range_start and element < src_range_start + range_length:
            offset = element - src_range_start
            return dest_range_start + offset
    return element


seeds = []
locations = []
maps = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": []
}

with open("input.txt", "r") as file:
    lines = file.readlines()

current_section = None

for line in lines:
    if line.startswith("seeds:"):
        current_section = "seeds"
        seeds = [int(word) for word in line.split()[1:] if word.isdigit()]

    elif line.startswith("seed-to-soil map:"):
        current_section = "seed-to-soil"
        maps[current_section] = []

    elif line.startswith("soil-to-fertilizer map:"):
        current_section = "soil-to-fertilizer"
        maps[current_section] = []

    elif line.startswith("fertilizer-to-water map:"):
        current_section = "fertilizer-to-water"
        maps[current_section] = []

    elif line.startswith("water-to-light map:"):
        current_section = "water-to-light"
        maps[current_section] = []

    elif line.startswith("light-to-temperature map:"):
        current_section = "light-to-temperature"
        maps[current_section] = []

    elif line.startswith("temperature-to-humidity map:"):
        current_section = "temperature-to-humidity"
        maps[current_section] = []

    elif line.startswith("humidity-to-location map:"):
        current_section = "humidity-to-location"
        maps[current_section] = []

    elif current_section is not None and line.strip():
        numbers_list = [int(word) for word in line.split() if word.isdigit()]
        maps[current_section].append(numbers_list)


for seed in seeds:
    soil = translation(seed, maps["seed-to-soil"])
    fertilizer = translation(soil, maps["soil-to-fertilizer"])
    water = translation(fertilizer, maps["fertilizer-to-water"])
    light = translation(water, maps["water-to-light"])
    temperature = translation(light, maps["light-to-temperature"])
    humidity = translation(temperature, maps["temperature-to-humidity"])
    location = translation(humidity, maps["humidity-to-location"])
    locations.append(location)


print(min(locations))