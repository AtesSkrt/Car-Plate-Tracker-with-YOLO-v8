import torch #pytorch GPU kullanabilmemizi sağlar, görüntü işlerken gpu cpu'dan çok daha hızlı. yolo ve easyocr için gerekli.
from ultralytics import YOLO #yolo makine öğrenmesi ile eğittiğimiz AI
import cv2 #kameradan frame çekme, frame'leri editleme için kullanıldı
import easyocr #plakayı okuyan AI
import string

model = YOLO("best.pt")

results = model.predict(source="0", show=True)

print(results)