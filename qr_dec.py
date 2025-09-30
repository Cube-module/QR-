import pyzbar
import qrcode 
import matplotlib as ml
import pyzbar
import cv2
import numpy as np

def file_add(name_f, qr_cd):
    """
    Принимает название файла для загрузки изображения и что кодируем в qr (name_f, qr_cd)
    
    Создает файл с qr кодом
    """
    # пример данных
    data = qr_cd

    # имя выходного файла
    filename = name_f

    # генерировать qr-код
    img = qrcode.make(data)

    # сохранить img в файл
    img.save(filename)

def Dec(name_f):
    """
    Принимает название файла с qr кодом (name_f)
    
    Возвращает декодированные данные и файл с изображением (data, bbox, img)
    """
    
    # читать изображение QRCODE
    img = cv2.imread(name_f)

    # инициализируем детектор QRCode cv2
    detector = cv2.QRCodeDetector()

    # обнаружить и декодировать
    data, bbox, a = detector.detectAndDecode(img) # bbox получается 3 мерным 
    
    return data, bbox, img

def write_p(data, bbox, img):
    """
    Принимает расшифрованное значение, координаты углов и изображение
    
    Выводит расшифровку и qr с линиями 
    """
    # отобразить результат
    if bbox is not None:
        
        print(data)
        points = []
        for point in bbox[0]:
            x, y = int(point[0]), int(point[1])  # преобразуем в целые числа
            points.append((x, y))
        
        print(f"Точки: {points}")
        
        # Рисуем 4 линии
        cv2.line(img, points[0], points[1], (255, 255,0), 10)
        cv2.line(img, points[1], points[2], (255, 255,0), 10) 
        cv2.line(img, points[2], points[3], (255, 255,0), 10)
        cv2.line(img, points[3], points[0], (255, 255,0), 10)
        
    cv2.imwrite("img.png", img)
    
def main():
    # создаем qr
    file = "Cube-module.png"
    qr_codding = "https://github.com/Cube-module"
    
    file_add(file, qr_codding)
    
    # декодируем qr
    data, bbox ,img = Dec(file)
    
    # выводим результат
    write_p(data, bbox, img)
    
    
if __name__ == "__main__":
    main()  
