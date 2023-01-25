import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_skin():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    skin = f.generate()
    # Add noise to the fractal shape to make it look more like skin
    noise = np.random.normal(0, 0.05, skin.shape)
    skin = skin + noise
    skin = np.clip(skin, 0, 1)
    # Apply a skin-like color map to the fractal shape
    skin = plt.cm.YlOrBr(skin)
    # Return the fractal skin
    return skin

# Generate 10 fractal skin images
for i in range(10):
    skin = generate_fractal_skin()
    plt.imsave("fractal_skin_{}.png".format(i), skin)
