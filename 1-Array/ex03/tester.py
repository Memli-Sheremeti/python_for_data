from load_image import ft_load
from zoom import ft_zoom
import matplotlib.pyplot as plt


print(ft_load("animal.jpeg"))
img = ft_zoom("animal.jpeg")
print(img)
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap="gray")
plt.show()
