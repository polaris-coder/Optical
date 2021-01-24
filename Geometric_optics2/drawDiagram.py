import math
import numpy as np
import matplotlib.pyplot as plt

class drawDiagram():
    def __init__(self, lensSys):
        self.lensSys = lensSys
        self.L_OEP = 0
        self.Lens = lensSys.Lens[math.ceil(len(lensSys.Lens) / 2)]
        for i in range(self.lensSys.pupilPosition):
            self.L_OEP = self.L_OEP + self.Lens[i]['t']

    # 功能：绘制二维透镜面(私有函数)
    def __drawSurf(self, yLast):
        # 1. 对最大视场角光线进行追迹，记录光线与每一个透镜面的交点坐标(即确定每一个透镜的孔径大小)
        theta = math.pi * self.lensSys.pupiltheta / 180
        thetas = [theta, theta]
        x = 0
        y = np.array([self.lensSys.pupilRadius - self.L_OEP * np.tan(theta),
                      -self.lensSys.pupilRadius - self.L_OEP * np.tan(theta)])
        z = 0
        X = 0
        Y = np.sin(thetas)
        Z = np.cos(thetas)
        ray = {'x': x, 'y': y, 'z': z, 'X': X, 'Y': Y, 'Z': Z}
        rays = self.lensSys.SkewRayTrace(ray, self.Lens)    # rays保存了光线在每一个透镜面上的坐标，以及方向矢量

        # 2. 计算每一个透镜的高度
        num_lens = int((len(self.Lens) - 2) / 2)
        H_lens = []    # H_lens保存了每一个透镜的孔径
        for nl in range(num_lens):
            H = max([np.abs(rays[nl * 2 + 1]['y']).max(), np.abs(rays[nl * 2 + 2]['y']).max()])
            H_lens.append(H)
            H_lens.append(H)
        H_lens.append(yLast * self.lensSys.pupilRadius)

        # 3. 计算每一个面上的点坐标
        zRange = []
        yRange = []
        z0 = 0
        for nl in range(1, len(self.Lens)):
            C = self.Lens[nl]['C']    # 曲率
            # 计算第nl个面顶点在z轴上的坐标
            if nl > 0:
                z0 = z0 + self.Lens[nl - 1]['t']    # 计算第nl个面顶点的z轴坐标
            # 计算透镜圆心
            if C == 0:
                surf_y = np.array([-H_lens[nl - 1], H_lens[nl - 1]])
                surf_z = np.array([1, 1]) * z0
            else:
                r = 1 / C    # 计算半径
                (a, b) = (z0 + r, 0)    # 透镜中心
                c = np.arcsin(abs((H_lens[nl - 1] - b) / r))  # 计算透镜最大的角度
                theta = np.arange(-c, c, 0.01)    # 计算角度范围
                thetas = np.append(theta, c)
                surf_z = a - r * np.cos(thetas)    # 计算透镜面z范围
                surf_y = b + abs(r) * np.sin(thetas)    # 计算透镜面y范围
            # 存储透镜面的坐标
            zRange.append(surf_z)
            yRange.append(surf_y)
            if nl > 0:
                if nl == self.lensSys.num_lens - 1:
                    self.axes.plot(np.array(surf_z) / self.lensSys.pupilRadius, np.array([-yLast, yLast]), 'k')
                else:
                    self.axes.plot(np.array(surf_z) / self.lensSys.pupilRadius, np.array(surf_y) / self.lensSys.pupilRadius,
                             'k')
            # 绘制透镜上下表面
            if nl > 0 and nl % 2 == 0:
                self.axes.plot([zRange[nl-2][-1] / self.lensSys.pupilRadius, surf_z[-1] / self.lensSys.pupilRadius],
                             [H_lens[nl-1] / self.lensSys.pupilRadius, H_lens[nl-1] / self.lensSys.pupilRadius], 'k')
                self.axes.plot([zRange[nl-2][-1] / self.lensSys.pupilRadius, surf_z[-1] / self.lensSys.pupilRadius],
                             [-H_lens[nl-1] / self.lensSys.pupilRadius, -H_lens[nl-1] / self.lensSys.pupilRadius], 'k')

    # 绘制光线示意图
    # 输入：theta:    光束角度
    #      num_rays:    光线个数
    # 输出：光线追迹示意图
    def drawRayTrace(self, theta, num_rays, color):
        num_lens = self.lensSys.num_lens    # 透镜面的个数
        theta = np.array(theta) * np.pi / 180       # 角度转弧度
        # 光线采样
        ray_x = np.zeros(shape = num_rays)
        ray_y = np.linspace(-self.lensSys.pupilRadius / 2 - self.L_OEP * np.tan(theta),
                            self.lensSys.pupilRadius / 2 - self.L_OEP * np.tan(theta), num_rays)
        ray_z = np.zeros(shape = num_rays)
        ray_X = np.zeros(shape = num_rays)
        ray_Y = np.ones(shape = num_rays) * np.sin(theta)
        ray_Z = np.ones(shape = num_rays) * np.cos(theta)
        ray = {'x': ray_x, 'y': ray_y, 'z': ray_z, 'X': ray_X, 'Y': ray_Y, 'Z': ray_Z}
        rays = self.lensSys.SkewRayTrace(ray, self.Lens)
        # 1. 生成坐标数组
        # 1) 将光线在每个透镜面上的坐标提取出来
        y = np.zeros(shape = (num_lens, num_rays))
        z = np.zeros(shape = (num_lens, num_rays))
        for i in range(len(self.Lens)):
            for j in range(num_rays):
                y[i,j] = rays[i]['y'][j]
                z[i,j] = rays[i]['z'][j]
        # 2) 将其修改为在光轴坐标系中的坐标
        t = np.array([self.Lens[i]['t'] for i in range(num_lens)])
        for i in range(num_lens):
            if i > 0:
                t[i] = t[i] + t[i-1]
        S = np.zeros(shape = num_lens)
        S[1:num_lens] = t[:num_lens-1]
        z = z + np.array([S] * num_rays).T
        # 归一化
        y = y / self.lensSys.pupilRadius
        z = z / self.lensSys.pupilRadius
        # 2. 绘制光线
        for i in range(num_rays):
            self.axes.plot(z[1:num_lens, i], y[1:num_lens, i], color)
        # 3. 绘制透镜
        yLast = y.max()
        self.__drawSurf(yLast)