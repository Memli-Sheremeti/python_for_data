from load_image import ft_load
from pimp_imgage import ft_invert
from pimp_imgage import ft_grey
from pimp_imgage import ft_red
from pimp_imgage import ft_green
from pimp_imgage import ft_blue


img = ft_load("landscape.jpg")
print(img)
ft_invert(img)
ft_red(img)
ft_green(img)
ft_blue(img)
ft_grey(img)
