import base64
from io import BytesIO
import matplotlib.pyplot as plt

def generate_image(MINIMUM= 1, MAXIMUM= 1000000):
    x_values = range(MINIMUM,MAXIMUM+1)
    y_values = []

    for x in x_values:
        count = 0
        while x != 1:
            if x % 2 == 0:
                x /= 2
            else:
                x = 3*x + 1
            count += 1
        
        y_values.append(count)


    # Englisch (für Wikipedia)
    plt.title("Collatz Conjecture")
    plt.ylabel("Iterations to reach 1")

    # Für beide Sprachen
    plt.xlabel("input")

    plt.plot(
        x_values, # Die Werte für x als "iterable" (listenartig)
        y_values, # Die Werte für y als "iterable" (listenartig)
        'ro',  # ro steht für red (r) und circles (o) => rote punkte
        markersize=1, # Punktgröße
        # damit die einzelnen Punkte bei einem Raum (1, 100) nicht genauso klein sind, wie bei einem anderen Raum (1, 100000) wird diese automatisch angepasst
        # beim ersten Raum wäre der Wert 100/100 = 1 => dickerer Rand und damit bessere Sichtbarkeit bei wenigeren Punkten
        # beim zweitenräum wäre der Wert 100/100000 = 0.001 => dünnerer Rand und damit bessere Sichtbarkeit bei vielen Punkten
        markeredgewidth=100/(MAXIMUM-MINIMUM) # Randbreite
    )
    # Damit der Graph nicht zuviel zeigt (und nicht zu wenig) werden die Mininmums und Maximums manuell gesetzt
    plt.xlim(xmin=MINIMUM-1, xmax=MAXIMUM)
    plt.ylim(ymin=0)

    image = BytesIO()

    # optional kann die Abbildung auch als Bild gespeichert werden
    plt.savefig(image, format="png")
    return base64.encodebytes(image.getvalue())