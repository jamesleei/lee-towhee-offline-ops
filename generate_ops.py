from towhee import pipe, ops

p = (
    pipe.input('path')
        .map('path', 'img', ops.image_decode.cv2_rgb())
        .map('img', 'embedding', ops.image_embedding.timm(model_name='resnet50'))
        .output('embedding')
)

# 使用假数据触发 Operator 下载
p('./fake.jpg')
