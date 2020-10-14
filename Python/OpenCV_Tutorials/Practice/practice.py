import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

a = 100000000000001100011
b = 1100011

k = cv2.waitKey(1)

y = a & b

#key = cv2.waitKey(1) & 0xff
#print(key)
#print(ord('e'))

print(int(a))
print(int(b))

print(bin(y))
print(y)
print(bin(k))
