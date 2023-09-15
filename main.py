from functools import reduce

# Der Algorithmus von Euklid ist etwas zu lange um ihn nur als Lambda-Funktion zu schreiben.
# Deshalb schreiben wir eine Funktion, die den Algorithmus implementiert.
def gcd(a, b):
    """
    Berechnet den größten gemeinsamen Teiler von a und b.
    Args:
    - a (int): Eine Zahl.
    - b (int): Eine Zahl.
    Returns:
    - int: Der größte gemeinsame Teiler von a und b.
    """
    pass


def gcd(numbers):
    """
    Berechnet den größten gemeinsamen Teiler einer Liste von Zahlen.
    Benutzt dazu die Funktion gcd(a, b) mit reduce().
    Args:
    - numbers (list): Eine Liste von Zahlen.
    Returns:
    - int: Der größte gemeinsame Teiler der Liste.
    """
    return 0


if __name__ == '__main__':
    numbers = [12, 15, 21]
    result = gcd(numbers)
    print(result)  # Sollte 3 ausgeben