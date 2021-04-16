#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín

import cv2
import scipy
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("./test/00401.jpg") # No se ve un pimiento, es super oscura ¿aclararla?
#img=cv2.imread("./test/00423.jpg")
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()

im=img/64.0
m_power_law_transformation = cv2.pow (im, 0.6)
cv2.imshow ('Original Image', im)
cv2.imshow ('Power Transformación de ley ', im)
cv2.waitKey (0)
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.show()
