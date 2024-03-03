# 주어진 이미지에 대하여 색상을 흑백으로 변환하고, 
# 대비를 증가시킨 다음 저장하세요.

from PIL import Image, ImageEnhance

image = Image.open('Real_Madrid_CF.png')

image = image.convert('RGB') # 에러로 인해 RGB 형식으로 변경

bw_image = image.convert("L") # 이미지 흑백으로 변환

enhancer = ImageEnhance.Contrast(bw_image)

enhanced_image = enhancer.enhance(2)

enhanced_image.save("black_and_white.jpg") 