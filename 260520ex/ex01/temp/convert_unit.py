def convertUnit(length_mm):
    units = {
        "cm": length_mm * 0.1,
        "m": length_mm * 0.001,
        "inch": length_mm * 0.03937,
        "feet": length_mm * 0.003281,
    }

    return units


def printLength(unit_lengths):
    for unit in unit_lengths:
        print(f"{unit}: {unit_lengths[unit]:.2f}{unit}")
