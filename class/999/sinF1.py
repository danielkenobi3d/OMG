import pymel.core as pm
import math

locators = []
boxes = []
amplitud = 5
phase = 0  # math.pi
offset = 0
samples_number = 80  # 增加采样数以获得更平滑的曲线
resolution_a = math.pi / samples_number  # 这个值是弧度
resolution_x = 80 / samples_number  # 这个值是Maya单位

for each in range(samples_number):
    locators.append(pm.spaceLocator())
    boxes.append(pm.polyCube(w=0.3, h=1, d=0.3)[0])

for index, (sample_loc, sample_box) in enumerate(zip(locators, boxes)):
    x_position = resolution_x * index
    y_position = amplitud * math.sin(resolution_a * index + phase) + offset

    # 设置定位器位置
    sample_loc.translateX.set(x_position)
    sample_loc.translateY.set(y_position)
    sample_loc.translateZ.set(0)
    sample_loc.scale.set(0.1, 0.1, 0.1)  # 缩小定位器大小

    # 设置盒子位置和大小
    sample_box.translateX.set(x_position)
    sample_box.translateY.set(y_position / 2)  # 将盒子的中心点放在y_position
    sample_box.translateZ.set(0)

    # 计算盒子高度（将y_position从-amplitud到+amplitud映射到0.5到5）
    normalized_height = (y_position + amplitud) / (2 * amplitud)
    box_height = 0.5 + normalized_height * 4.5
    sample_box.scaleY.set(box_height)

# 创建曲线连接所有定位器
curve_points = [(loc.translateX.get(), loc.translateY.get(), loc.translateZ.get()) for loc in locators]
pm.curve(degree=3, point=curve_points)

# 创建一个组来包含所有的定位器和盒子
pm.group(locators + boxes, name="sineWave_group")