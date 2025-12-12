"""Basic unit converter (length, weight, temperature)."""
from .utils import safe_input

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    units = {'m': 1.0, 'cm': 0.01, 'mm': 0.001, 'km': 1000.0, 'ft': 0.3048, 'in': 0.0254}
    if from_unit not in units or to_unit not in units:
        raise ValueError('Unsupported length unit')
    return value * units[from_unit] / units[to_unit]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    if from_unit == 'c':
        if to_unit == 'f':
            return value * 9/5 + 32
        if to_unit == 'k':
            return value + 273.15
    if from_unit == 'f':
        if to_unit == 'c':
            return (value - 32) * 5/9
        if to_unit == 'k':
            return (value - 32) * 5/9 + 273.15
    if from_unit == 'k':
        if to_unit == 'c':
            return value - 273.15
        if to_unit == 'f':
            return (value - 273.15) * 9/5 + 32
    raise ValueError('Unsupported temperature units')

def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    units = {'kg': 1.0, 'g': 0.001, 'mg': 1e-6, 'lb': 0.45359237}
    if from_unit not in units or to_unit not in units:
        raise ValueError('Unsupported weight unit')
    return value * units[from_unit] / units[to_unit]

def run():
    MENU = '''\nUNIT CONVERTER:\n1. Length\n2. Temperature\n3. Weight\n4. Back to Main Menu\n'''
    while True:
        print(MENU)
        c = safe_input('Choice: ').strip()
        if c == '1':
            try:
                v = float(safe_input('Value: '))
                f = safe_input('From (m, cm, mm, km, ft, in): ').strip()
                t = safe_input('To (m, cm, mm, km, ft, in): ').strip()
                print('Result:', convert_length(v, f, t))
            except Exception as e:
                print('Error:', e)
        elif c == '2':
            try:
                v = float(safe_input('Value: '))
                f = safe_input('From (c, f, k): ').strip().lower()
                t = safe_input('To (c, f, k): ').strip().lower()
                print('Result:', convert_temperature(v, f, t))
            except Exception as e:
                print('Error:', e)
        elif c == '3':
            try:
                v = float(safe_input('Value: '))
                f = safe_input('From (kg, g, mg, lb): ').strip()
                t = safe_input('To (kg, g, mg, lb): ').strip()
                print('Result:', convert_weight(v, f, t))
            except Exception as e:
                print('Error:', e)
        elif c == '4' or c == '':
            break
        else:
            print('Invalid choice')