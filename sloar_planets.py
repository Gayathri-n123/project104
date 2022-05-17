import cv2

img=cv2.imread("solar-system.jpg")



cv2.putText(img,"Sun",(120,90),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.5,color=(0,0,255))
cv2.putText(img,"Mercury",(110,190),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(0,0,255))
cv2.putText(img,"Venus",(190,260),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(0,0,255))
cv2.putText(img,"Earth",(290,260),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(0,0,255))
cv2.putText(img,"Mars",(390,260),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(0,0,255))
cv2.putText(img,"Jupiter",(490,90),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,255))
cv2.putText(img,"Saturn",(750,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(0,0,255))
cv2.putText(img,"Uranus",(950,145),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(0,0,255))
cv2.putText(img,"Neptune",(1080,145),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(0,0,255))
cv2.imshow("output",img)
cv2.imwrite("solar-system-output.jpg",img)
cv2.waitKey(0)