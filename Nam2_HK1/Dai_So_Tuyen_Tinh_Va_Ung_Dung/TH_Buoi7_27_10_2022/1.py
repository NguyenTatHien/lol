import numpy as np
signals = np.array([[1,2],[3,4],[10,0]])
sample = np.array([3,-1])
d= np.inner(signals,sample)
print(d)
#Nguyen ly not nhac trong chuoi am thanh
import numpy as np
A= np.array([0,0,-1,2,3,-1,0,1,-1,-1])
search_vector = np.array([0,1,-1])
b= len(A), len(search_vector)
print(b)
B= np.array([1])
B = np.resize(B,(len(A)-len(search_vector)+1, len(search_vector)))
B = np.asmatrix(B)
for i in range(len(A) - len(search_vector)+1):
    for j in range(len(search_vector)):
        C=B[i,j] = A[i+j]
print(C)

C= np.inner(B,search_vector)
for i in range(len(A) - len(search_vector)+1):
    if (C[0,i] == np.inner(search_vector, search_vector)):
        print(i,B[i])
#Tao anh mau  from PIL imporImage
from PIL import Image
img = Image.open('C:/Hiển microsoft/lo.jpg')
img.height # xem chiều cao của ảnh
img.width # chiều rộng của ảnh
img.mode # xem kiểu ảnh. Thường là 'RGBA', với kiểu ảnh có chữ ‘P’ chúng ta phải
# print(img)
# print(c)
# print(d)
# print(e)
img = img.convert("RGB") # convert it to RGB (để chuyển về dạng RGB)
new_width = int(img.width / 2) # giảm ½ chiều rộng
new_height = int(img.height / 2) # giảm ½ chiều cao
new_img = img.resize((new_width, new_height),Image.Resampling.LANCZOS)
a=new_img.save('C:/Hiển microsoft/lo_small.jpg')
print(img)
print(new_width)
print(new_img)
print(a)

from PIL import Image, ImageDraw
input_image = Image.open('C://Hiển microsoft//lo.jpg')
input_pixels = input_image.load() # đọc các pixel(điểm ảnh). GV giải thích khái niệm pixel
box_kernel = [[1 / 9, 1 / 9, 1 / 9],
             [1 / 9, 1 / 9, 1 / 9],
            [1 / 9, 1 / 9, 1 / 9]]
kernel = box_kernel
offset = len(kernel) // 2
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)
print(draw)
for x in range(offset, input_image.width - offset):
    for y in range(offset, input_image.height - offset):
        acc = [0, 0, 0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b - offset
                pixel = input_pixels[xn, yn]
                acc[0] += pixel[0] * kernel[a][b]
                acc[1] += pixel[1] * kernel[a][b]
                acc[2] += pixel[2] * kernel[a][b]
        draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
output_image.save("C://Hiển microsoft//lo_mo.jpg")

import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

image = color.rgb2gray(data.astronaut())

image_rescaled = rescale(image, 1.0 / 4.0)
image_resized = resize(image, (image.shape[0] / 4, image.shape[1] / 4))
image_downscaled = downscale_local_mean(image, (4, 3))

fig, axes = plt.subplots(nrows=2, ncols=2)

ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Ảnh gốc')

ax[1].imshow(image_rescaled, cmap='gray')
ax[1].set_title('Ảnh đã scale')

ax[2].imshow(image_resized, cmap='gray')
ax[2].set_title('Ảnh có resize kích thước(no aliasing)')

ax[3].imshow(image_downscaled, cmap='gray')
ax[3].set_title('Ảnh giảm tỷ lệ (no aliasing)')

ax[0].set_xlim(0, 512)
ax[0].set_ylim(512, 0)
plt.tight_layout()
plt.show()

import numpy as np
A = np.array([[0,0,1.0/2, 1.0/2],
            [1.0/3,0,0,0],
            [1.0/3,0,0,1.0/2],
            [1.0/3,1.0,1.0/2,0]])
x = np.array([1,1,1,1])
print(x)
x = np.dot(A, x)
print (x)
x = np.array([1.0, 1.0, 1.0, 1.0])
for i in range(10):
    x = np.dot(A, x)
    print (i+1, x)
A = np.array([[0,0,1.0/2, 0.0],
            [1.0/3,0,0,0],
            [1.0/3,0,0,0.0],
            [1.0/3,1.0,1.0/2,0]])
for i in range(5):
    x = np.dot(A, x)
    print (i+1, x)
x = np.array([1.0, 1.0, 1.0, 1.0])
A = np.array([[0,0,1.0/2, 1/4.0],
            [1.0/3,0,0,1/4.0],
            [1.0/3,0,0,1/4.0],
            [1.0/3,1.0,1.0/2,1/4.0]])
for i in range(7):
    x = np.dot(A, x)
    print (i+1, x)
c=np.max(x)
print(c)
A = np.array([[0.0, 0.0, 1/2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [1.0/3, 0.0, 1/2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [1/3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [1.0/3,1/2.0,1/2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0 ,1/2.0, 0.0, 0.0, 0.0,1/2.0, 0.0,0.0],
            [0.0, 0.0, 0.0,0.0, 0.0, 0.0, 1.0,1/2.0],
            [0.0, 0.0, 0.0,1/2.0, 1.0, 0.0, 0.0, 1/2.0],
            [0.0, 0.0, 0.0,0.0, 0.0,1/2.0, 0.0, 0.0]])
N = 8
x = np.array([1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N])
for i in range(7):
    x = np.dot(A, x)
    print (i+1, x)
d = 0.85
N = 8
x = np.array([1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N])

M = d*A + ((1-d)/N)* np.ones([N,N])
print(M)
for i in range(7):
    x = np.dot(A, x)
    print (i+1, x)