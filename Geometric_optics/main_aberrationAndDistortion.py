from matplotlib.ticker import MultipleLocator
from Geometric_optics import opticalSystem, drawDiagram
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math

class Tool(FigureCanvas):
    
    def __init__(self,Lens,pupilRadius,pupiltheta,pupilPosition,thetas,apertureRays,apertureRays2):
        self.Lens=Lens
        self.pupilRadius=pupilRadius
        self.pupiltheta=pupiltheta
        self.pupilPosition=pupilPosition
        self.thetas=thetas
        self.apertureRays=apertureRays
        self.apertureRays2=apertureRays2

        # 实例化光学系统
        self.lensSys = opticalSystem.LensSys(self.Lens, self.pupilRadius, self.pupiltheta, self.pupilPosition)
        self.lensSys.calEfl()      # 确定光学系统理想成像面的位置

        self.L_OEP = 0
        for i in range(self.lensSys.pupilPosition):
            self.L_OEP = self.L_OEP + self.lensSys.Lens[i]['t']

    # 横向像差点列图
    def Ppint_diagram(self):
        # 2. 绘制横向像差点列图
        x0, y0 = self.lensSys.centralLocationInImage(self.thetas)
        X, Y = self.lensSys.lateralAberration(self.thetas, self.apertureRays)

        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(6, 5), dpi=100)
        # 第二步：在父类中激活Figure窗口
        super(Tool, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes1 = self.fig.add_subplot(221)

        self.axes1.set_xlim(-1,1)
        self.axes1.set_ylim(-1,1)
        Xb = X[:, :, 0].flatten()
        Yb = Y[:, :, 0].flatten()
        self.axes1.scatter(Xb - x0[0], Yb - y0[0], marker='+')
        self.axes1.xaxis.set_major_locator(MultipleLocator(0.2))# 将x轴主刻度标签设置为0.2的倍数
        self.axes1.yaxis.set_major_locator(MultipleLocator(0.2))# 将y轴主刻度标签设置为0.2的倍数
        for label in self.axes1.xaxis.get_ticklabels():
            # label is a Text instance
            label.set_rotation(45)
        self.axes1.grid()
        self.axes1.set_xlabel("z/mm")
        self.axes1.set_ylabel("y/mm")

        self.axes2 = self.fig.add_subplot(222)
        self.axes2.set_xlim(-1, 1)
        self.axes2.set_ylim(-1, 1)
        Xb = X[:, :, 1].flatten()
        Yb = Y[:, :, 1].flatten()
        self.axes2.scatter(Xb - x0[1], Yb - y0[1], marker='+')
        self.axes2.xaxis.set_major_locator(MultipleLocator(0.2))
        self.axes2.yaxis.set_major_locator(MultipleLocator(0.2))
        for label in self.axes2.xaxis.get_ticklabels() :
            # label is a Text instance
            label.set_rotation(45)
        self.axes2.grid()
        self.axes2.set_xlabel("z/mm")
        self.axes2.set_ylabel("y/mm")

        self.axes3 = self.fig.add_subplot(223)
        self.axes3.set_xlim(-1, 1)
        self.axes3.set_ylim(-1, 1)
        Xb = X[:, :, 2].flatten()
        Yb = Y[:, :, 2].flatten()
        self.axes3.scatter(Xb - x0[2], Yb - y0[2], marker='+')
        self.axes3.xaxis.set_major_locator(MultipleLocator(0.2))
        self.axes3.yaxis.set_major_locator(MultipleLocator(0.2))
        for label in self.axes3.xaxis.get_ticklabels() :
            # label is a Text instance
            label.set_rotation(45)
        self.axes3.grid()
        self.axes3.set_xlabel("z/mm")
        self.axes3.set_ylabel("y/mm")

        self.axes4 = self.fig.add_subplot(224)
        self.axes4.set_xlim(-1, 1)
        self.axes4.set_ylim(-1, 1)
        Xb = X[:, :, 3].flatten()
        Yb = Y[:, :, 3].flatten()
        self.axes4.scatter(Xb - x0[3], Yb - y0[3], marker='+')
        self.axes4.xaxis.set_major_locator(MultipleLocator(0.2))
        self.axes4.yaxis.set_major_locator(MultipleLocator(0.2))
        for label in self.axes4.xaxis.get_ticklabels() :
            # label is a Text instance
            label.set_rotation(45)
        self.axes4.grid()
        self.axes4.set_xlabel("z/mm")
        self.axes4.set_ylabel("y/mm")

        self.fig.tight_layout(pad=0.1, w_pad=0.1, h_pad=0.1)

    # 径向像差曲线
    def radial_aberration_curve(self):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(6,5), dpi=100)
        #第二步：在父类中激活Figure窗口
        super(Tool,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

        # 3. 绘制径向像差曲线
        thetas = np.array(range(self.pupiltheta + 1))  # 角度范围为0-20
        z_yc, z_xc = self.lensSys.longitudalAberration(thetas, self.apertureRays2)
        # 绘制径向像差曲线
        self.axes.set_xlim(-self.apertureRays2, self.apertureRays2)
        self.axes.set_ylim(0, 20)
        self.axes.plot(z_yc, thetas)
        self.axes.plot(z_xc, thetas, linestyle='--')
        xmajorLocator = MultipleLocator(0.4)  # 将x轴主刻度标签设置为0.2的倍数
        ymajorLocator = MultipleLocator(2)  # 将y轴主刻度标签设置为0.2的倍数
        self.axes.xaxis.set_major_locator(xmajorLocator)
        self.axes.yaxis.set_major_locator(ymajorLocator)
        self.axes.grid()
        self.axes.set_title('Longitudal Aberration')
        self.axes.set_xlabel('range/mm')
        self.axes.set_ylabel('angle/degree')

    # 畸变曲线
    def distortion_curve(self):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(6,5), dpi=100)
        #第二步：在父类中激活Figure窗口
        super(Tool,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

        # 4. 绘制畸变曲线
        thetas = np.array(range(self.pupiltheta + 1))  # 角度范围为0-20
        error = self.lensSys.distortion(thetas)
        # 绘制畸变曲线
        self.axes.set_xlim(-0.5, 0.5)
        self.axes.set_ylim(0, 20)
        self.axes.plot(error, thetas)
        xmajorLocator = MultipleLocator(0.1)  # 将x轴主刻度标签设置为0.2的倍数
        ymajorLocator = MultipleLocator(2)  # 将y轴主刻度标签设置为0.2的倍数
        self.axes.xaxis.set_major_locator(xmajorLocator)
        self.axes.yaxis.set_major_locator(ymajorLocator)
        self.axes.grid()
        self.axes.set_title('Distortion')
        self.axes.set_xlabel('percent/%')
        self.axes.set_ylabel('angle/degree')

    # 光线追迹示意图
    def ray_tracing(self):
        # 5. 绘制光线追迹示意图
        theta = 10  # 光线的角度
        num_rays = 3  # 需要的光线个数

        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(6, 5), dpi=100)
        # 第二步：在父类中激活Figure窗口
        super(Tool, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

        num_lens = self.lensSys.num_lens  # 透镜面的个数
        theta = theta * math.pi / 180  # 角度转弧度
        # 光线采样
        ray_x = np.zeros(shape=num_rays)
        ray_y = np.linspace(-self.lensSys.pupilRadius / 2 - self.L_OEP * math.tan(theta),
                            self.lensSys.pupilRadius / 2 - self.L_OEP * math.tan(theta), num_rays)
        ray_z = np.zeros(shape=num_rays)
        ray_X = np.zeros(shape=num_rays)
        ray_Y = np.ones(shape=num_rays) * math.sin(theta)
        ray_Z = np.ones(shape=num_rays) * math.cos(theta)
        ray = {'x': ray_x, 'y': ray_y, 'z': ray_z, 'X': ray_X, 'Y': ray_Y, 'Z': ray_Z}
        rays = self.lensSys.SkewRayTrace(ray)
        # 1. 生成坐标数组
        # 1) 将光线在每个透镜面上的坐标提取出来
        y = np.zeros(shape=(num_lens, num_rays))
        z = np.zeros(shape=(num_lens, num_rays))
        for i in range(len(self.lensSys.Lens)):
            for j in range(num_rays):
                y[i, j] = rays[i]['y'][j]
                z[i, j] = rays[i]['z'][j]
        # 2) 将其修正为在光轴坐标系中的坐标
        t = np.array([self.lensSys.Lens[i]['t'] for i in range(num_lens)])
        for i in range(num_lens):
            if i > 0:
                t[i] = t[i] + t[i - 1]
        S = np.zeros(shape=num_lens)
        S[1:num_lens] = t[:num_lens - 1]
        z = z + np.array([S] * num_rays).T
        # 归一化
        y = y / self.lensSys.pupilRadius
        z = z / self.lensSys.pupilRadius
        # 2. 绘制光线
        # fig = plt.figure()
        # ax = fig.add_subplot(111)

        for i in range(num_rays):
            self.axes.plot(z[:, i], y[:, i], 'b')
            # plt.plot(z[1:num_lens, i], y[1:num_lens, i], 'b')
        # 3. 绘制透镜
        yLast = y.max()
        # self.__drawSurf(yLast)
        lenH = self.lensSys.pupilRadius
        num_lens = len(self.lensSys.Lens)
        zRange = []
        yRange = []
        z0 = 0
        for nl in range(num_lens):
            C = self.lensSys.Lens[nl]['C']  # 曲率
            # 计算镜面中心在光轴上的位置
            if nl > 0:
                z0 = z0 + self.lensSys.Lens[nl - 1]['t']
            # 计算透镜圆心
            if C == 0:
                surf_y = np.array([-lenH, lenH])
                surf_z = np.array([1, 1]) * z0
            else:
                r = 1 / C  # 计算半径
                (a, b) = (z0 + r, 0)  # 透镜中心
                c = np.arcsin(abs((lenH - b) / r))  # 计算透镜最大的角度
                theta = np.arange(-c, c, 0.01)  # 计算角度范围
                thetas = np.append(theta, c)
                surf_z = a - r * np.cos(thetas)  # 计算透镜面z范围
                surf_y = b + abs(r) * np.sin(thetas)  # 计算透镜面y范围
            # 存储透镜面的坐标
            zRange.append(surf_z)
            yRange.append(surf_y)

            if nl > 0:
                if nl == num_lens - 1 and yLast > lenH:
                    self.axes.plot(np.array(surf_z) / self.lensSys.pupilRadius, np.array([-yLast, yLast]), 'k')
                else:
                    self.axes.plot(np.array(surf_z) / self.lensSys.pupilRadius, np.array(surf_y) / self.lensSys.pupilRadius,
                            'k')
            # 绘制透镜上下表面
            if nl > 0 and nl % 2 == 0:
                self.axes.plot([zRange[nl - 1][-1] / self.lensSys.pupilRadius, surf_z[-1] / self.lensSys.pupilRadius],
                        [lenH / self.lensSys.pupilRadius, lenH / self.lensSys.pupilRadius], 'k')
                self.axes.plot([zRange[nl - 1][-1] / self.lensSys.pupilRadius, surf_z[-1] / self.lensSys.pupilRadius],
                        [-lenH / self.lensSys.pupilRadius, -lenH / self.lensSys.pupilRadius], 'k')

        # drawRays = drawDiagram.drawDiagram(self.lensSys)
        # drawRays.drawRayTrace(theta, num_rays)