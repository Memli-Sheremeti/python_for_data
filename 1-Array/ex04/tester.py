from load_image import ft_load
from rotate import ft_rotate
import matplotlib.pyplot as plt


print(ft_load("animal.jpeg"))
img = ft_rotate("animal.jpeg")
print(img)
# plt.figure(figsize=(6, 6))
plt.imshow(img, cmap="gray")
plt.show()
