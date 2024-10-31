import maya.cmds as cmds
import math


def create_multi_period_helix(
        amplitude=2,  # 横向振幅
        cycles=8,  # 周期数
        height_per_cycle=8,  # 每个周期的高度
        segments_per_cycle=50,  # 每个周期的分段数
        frequency_factor=0.25  # 频率调节因子 - 降低这个值会让螺旋更舒展
):
    """
    创建低频多周期的无限符号螺旋曲线

    参数:
    amplitude: 横向振幅
    cycles: 重复的周期数
    height_per_cycle: 每个周期的高度
    segments_per_cycle: 每个周期的分段数
    frequency_factor: 频率调节因子，控制螺旋的旋转频率
    """

    # 清理已存在的曲线
    for i in range(3):
        if cmds.objExists(f'helix_{i + 1}'):
            cmds.delete(f'helix_{i + 1}')

    # 计算总段数
    total_segments = segments_per_cycle * cycles
    total_height = height_per_cycle * cycles

    # 三条曲线的相位差（120度）
    strand_phases = [0, 2 * math.pi / 3, 4 * math.pi / 3]

    for i, phase in enumerate(strand_phases):
        points = []

        for t in range(total_segments + 1):
            # 参数方程 - 使用frequency_factor来降低频率
            param = 2 * math.pi * t / segments_per_cycle * frequency_factor + phase

            # 使用"8"字形参数方程
            denominator = 1 + math.sin(param) ** 2
            x = amplitude * math.cos(param) / denominator
            z = amplitude * math.sin(param) * math.cos(param) / denominator
            y = (total_height * t) / total_segments

            points.append((x, y, z))

        # 创建NURBS曲线
        curve = cmds.curve(p=points, d=3, name=f'helix_{i + 1}')


# 执行函数，生成更舒展的螺旋
create_multi_period_helix(
    amplitude=2,  # 控制"∞"形状的宽度
    cycles=8,  # 周期数
    height_per_cycle=8,  # 每个周期的高度
    segments_per_cycle=50,  # 每个周期的分段数
    frequency_factor=0.25  # 降低频率，使螺旋更加舒展