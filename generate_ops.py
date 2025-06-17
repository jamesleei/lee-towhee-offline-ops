# generate_ops.py
from towhee import ops

# 触发 Towhee Operators 下载
ops.image_decode.cv2_rgb()
ops.image_embedding.timm(model_name='resnet50')
print("Operators pulled successfully!")
