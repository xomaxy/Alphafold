import numpy as np

def generar_secuencia(n):
    amino_set = ['A', 'M', 'B', 'N', 'C', 'P', 'D', 'Q', 'E', 'R', 'F', 'S', 'G', 'T', 'H', 'V', 'I', 'W', 'K', 'Y', 'L', 'Z']
    return ''.join(np.random.choice(amino_set, n))

def cambiar_letras_aleatoriamente(secuencia, n_cambios):
    # Convert the sequence into a list to allow modifications
    secuencia_lista = list(secuencia)
    longitud_secuencia = len(secuencia_lista)
    
    # Perform n_cambios random changes in the sequence
    for _ in range(n_cambios):
        # Select a random position to change
        pos = np.random.randint(longitud_secuencia)
        # Randomly select a new letter from the array
        nueva_letra = np.random.choice(letras_mayusculas)
        # Replace the letter at the chosen position
        secuencia_lista[pos] = nueva_letra
    
    # Convert the list back to a string
    return ''.join(secuencia_lista)
