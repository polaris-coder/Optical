from matplotlib.ticker import MultipleLocator
import math
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Geometric_optics2 import opticalSystem

class DrawTool(FigureCanvas):

    def __init__(self,OriginalLens, pupilRadius, pupiltheta, wavelength):
        # 初始化
        self.OriginalLens = OriginalLens  # 透镜参数
        self.pupilRadius = pupilRadius  # 入瞳半径
        self.pupiltheta = pupiltheta  # 最大视场角
        self.wavelength = wavelength # 光线波长
        self.pupilPosition = 4  # 入瞳位置
        # 4) 绘制时的颜色信息
        self.colors = ['b', 'lime', 'r', 'y']
        self.thetasRange = np.array(range(self.pupiltheta + 1))  # 角度范围为0-20
        num_thetas = 4  # 视场角的个数
        self.thetasDiagram = np.linspace(0, self.pupiltheta, num_thetas)  # 定义视场角
        # 2. 实例化光学系统
        # 根据波长的不同，对光学系统实例化多次
        self.lensSys = opticalSystem.LensSys(self.OriginalLens, self.pupilRadius, self.pupiltheta, self.pupilPosition, self.wavelength)
        self.lensSys.calBfl()  # 确定光学系统理想成像面的位置
        self.L_OEP = 0
        self.Lens = self.lensSys.Lens[math.ceil(len(self.lensSys.Lens) / 2)]
        for i in range(self.lensSys.pupilPosition):
            self.L_OEP = self.L_OEP + self.Lens[i]['t']

    # 绘制横向像差点列图
    def Ppint_diagram(self):

        # 设置采样规则
        num_phi = 16  # pi内采样数
        num_h = 21  # 孔径直径采样数

        Lateral_apertureRays = self.pupilRadius  # 光束孔径设置为18.5
        XY, AXY = self.lensSys.lateralAberration(self.thetasDiagram, Lateral_apertureRays, num_phi, num_h)  # 返回的是三个波长的X,Y值
        # 确定坐标轴刻度范围
        XYmax = []
        for nw in range(len(self.wavelength)):
            XYmax.append(np.abs(XY[nw]['X']).max())
            XYmax.append(np.abs(XY[nw]['Y']).max())
        XYmax.append(AXY['X'].max())
        XYmax.append(AXY['Y'].max())
        xymax = math.ceil(max(XYmax) / 0.5) * 0.5

        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(5, 5), dpi=100)
        # 第二步：在父类中激活Figure窗口
        super(DrawTool, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)

        self.axes1 = self.fig.add_subplot(221)
        self.axes1.set_xlim(-xymax, xymax)
        self.axes1.set_ylim(-xymax, xymax)
        self.axes1.plot(AXY['X'], AXY['Y'], c='k')
        for nw in range(len(self.wavelength)):
            X = XY[nw]['X'][:,:,0].flatten()
            Y = XY[nw]['Y'][:,:,0].flatten()
            self.axes1.scatter(X, Y, c = self.colors[nw], marker='+')
        self.axes1.xaxis.set_major_locator(MultipleLocator(xymax / 5))
        self.axes1.yaxis.set_major_locator(MultipleLocator(xymax / 5))
        for label in self.axes1.xaxis.get_ticklabels():
            # label is a Text instance
            label.set_rotation(45)
        self.axes1.grid(color='gainsboro')
        # plt.xticks([])  # 去x坐标刻度
        # plt.yticks([])  # 去y坐标刻度
        self.axes1.set_xlabel("z/mm")
        self.axes1.set_ylabel("y/mm")

        self.axes2 = self.fig.add_subplot(222)
        self.axes2.set_xlim(-xymax, xymax)
        self.axes2.set_ylim(-xymax, xymax)
        self.axes2.plot(AXY['X'], AXY['Y'], c='k')
        for nw in range(len(self.wavelength)):
            X = XY[nw]['X'][:,:,1].flatten()
            Y = XY[nw]['Y'][:,:,1].flatten()
            self.axes2.scatter(X, Y, c = self.colors[nw], marker='+')
        self.axes2.xaxis.set_major_locator(MultipleLocator(xymax / 5))
        self.axes2.yaxis.set_major_locator(MultipleLocator(xymax / 5))
        for label in self.axes2.xaxis.get_ticklabels() :
            # label is a Text instance
            label.set_rotation(45)
        self.axes2.grid(color='gainsboro')
        # plt.xticks([])  # 去x坐标刻度
        # plt.yticks([])  # 去y坐标刻度
        self.axes2.set_xlabel("z/mm")
        self.axes2.set_ylabel("y/mm")

        self.axes3 = self.fig.add_subplot(223)
        self.axes3.set_xlim(-xymax, xymax)
        self.axes3.set_ylim(-xymax, xymax)
        self.axes3.plot(AXY['X'], AXY['Y'], c='k')
        for nw in range(len(self.wavelength)):
            X = XY[nw]['X'][:,:,2].flatten()
            Y = XY[nw]['Y'][:,:,2].flatten()
            self.axes3.scatter(X, Y, c = self.colors[nw], marker='+')
        self.axes3.xaxis.set_major_locator(MultipleLocator(xymax / 5))
        self.axes3.yaxis.set_major_locator(MultipleLocator(xymax / 5))
        for label in self.axes3.xaxis.get_ticklabels() :
            # label is a Text instance
            label.set_rotation(45)
        self.axes3.grid(color='gainsboro')
        # plt.xticks([])  # 去x坐标刻度
        # plt.yticks([])  # 去y坐标刻度
        self.axes3.set_xlabel("z/mm")
        self.axes3.set_ylabel("y/mm")

        self.axes4 = self.fig.add_subplot(224)
        self.axes4.set_xlim(-xymax, xymax)
        self.axes4.set_ylim(-xymax, xymax)
        self.axes4.plot(AXY['X'], AXY['Y'], c='k')
        for nw in range(len(self.wavelength)):
            X = XY[nw]['X'][:,:,3].flatten()
            Y = XY[nw]['Y'][:,:,3].flatten()
            self.axes4.scatter(X, Y, c = self.colors[nw], marker='+')
        self.axes4.xaxis.set_major_locator(MultipleLocator(xymax / 5))
        self.axes4.yaxis.set_major_locator(MultipleLocator(xymax / 5))
        for label in self.axes4.xaxis.get_ticklabels() :
            # label is a Text instance
            label.set_rotation(45)
        self.axes4.grid(color='gainsboro')
        # plt.xticks([])  # 去x坐标刻度
        # plt.yticks([])  # 去y坐标刻度
        self.axes4.set_xlabel("z/mm")
        self.axes4.set_ylabel("y/mm")

        self.fig.tight_layout(pad=0.1, w_pad=0.2, h_pad=0.2)

    # 绘制径向像差曲线
    def radial_aberration_curve(self):
        Longitude_apertureRays = 2  # 光束孔径设置为2，1/10
        Error = self.lensSys.longitudalAberration(self.thetasRange, Longitude_apertureRays)
        # 确定坐标轴刻度范围
        Emax = []
        Emin = []
        for nw in range(len(self.wavelength)):
            Emax.append(Error[nw]['xc_error'].max())
            Emax.append(Error[nw]['yc_error'].max())
            Emin.append(Error[nw]['xc_error'].min())
            Emin.append(Error[nw]['yc_error'].min())
        emax = math.ceil((min(Emax) - min(Emin)) / 0.5) * 0.5
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(5, 5), dpi=100)
        # 第二步：在父类中激活Figure窗口
        super(DrawTool, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlim(-emax, emax)  # 范围有问题
        self.axes.set_ylim(0, self.pupiltheta)
        for nw in range(len(self.wavelength)):
            self.axes.plot(Error[nw]['yc_error'], self.thetasRange, c=self.colors[nw])  # + abs(min(Emax))
            self.axes.plot(Error[nw]['xc_error'], self.thetasRange, c=self.colors[nw], linestyle='--')
        self.axes.xaxis.set_major_locator(MultipleLocator(emax / 5))  # 0.4自动化
        self.axes.yaxis.set_major_locator(MultipleLocator(self.pupiltheta / 10))  # 2自动化
        self.axes.grid()
        self.axes.set_title('Longitudal Aberration')
        self.axes.set_xlabel('range/mm')
        self.axes.set_ylabel('angle/degree')

    # 绘制畸变曲线
    def distortion_curve(self):
        Distortion = self.lensSys.distortion(self.thetasRange)
        # 确定坐标轴刻度范围
        Dmax = []
        Dmin = []
        for nw in range(len(self.wavelength)):
            Dmax.append(Distortion[nw].max())
            Dmax.append(Distortion[nw].max())
            Dmin.append(Distortion[nw].min())
            Dmin.append(Distortion[nw].min())
        dmax = math.ceil((max(Dmax) - min(Dmin)) / 0.1) * 0.1
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(5, 5), dpi=100)
        # 第二步：在父类中激活Figure窗口
        super(DrawTool, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlim(-dmax, dmax)
        self.axes.set_ylim(0, self.pupiltheta)
        for nw in range(len(self.wavelength)):
            Distortion[nw][0] = Distortion[nw][0] + Distortion[nw][1]
            self.axes.plot(Distortion[nw], self.thetasRange, color=self.colors[nw])
        self.axes.xaxis.set_major_locator(MultipleLocator(dmax / 5))
        self.axes.yaxis.set_major_locator(MultipleLocator(self.pupiltheta / 10))
        self.axes.grid()
        self.axes.set_title('Distortion')
        self.axes.set_xlabel('percent/%')
        self.axes.set_ylabel('angle/degree')

    # 绘制光线追迹示意图
    def ray_tracing(self):

        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(5, 5), dpi=100)
        # 第二步：在父类中激活Figure窗口
        super(DrawTool, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

        num_rays = 3

        for k in range(len(self.thetasDiagram)):
            num_lens = self.lensSys.num_lens  # 透镜面的个数
            self.thetasDiagram[k] = np.array(self.thetasDiagram[k]) * np.pi / 180  # 角度转弧度
            # 光线采样
            ray_x = np.zeros(shape=num_rays)
            ray_y = np.linspace(-self.lensSys.pupilRadius / 2 - self.L_OEP * np.tan(self.thetasDiagram[k]),
                                self.lensSys.pupilRadius / 2 - self.L_OEP * np.tan(self.thetasDiagram[k]), num_rays)
            ray_z = np.zeros(shape=num_rays)
            ray_X = np.zeros(shape=num_rays)
            ray_Y = np.ones(shape=num_rays) * np.sin(self.thetasDiagram[k])
            ray_Z = np.ones(shape=num_rays) * np.cos(self.thetasDiagram[k])
            ray = {'x': ray_x, 'y': ray_y, 'z': ray_z, 'X': ray_X, 'Y': ray_Y, 'Z': ray_Z}
            rays = self.lensSys.SkewRayTrace(ray, self.Lens)
            # 1. 生成坐标数组
            # 1) 将光线在每个透镜面上的坐标提取出来
            y = np.zeros(shape=(num_lens, num_rays))
            z = np.zeros(shape=(num_lens, num_rays))
            for i in range(len(self.Lens)):
                for j in range(num_rays):
                    y[i, j] = rays[i]['y'][j]
                    z[i, j] = rays[i]['z'][j]
            # 2) 将其修改为在光轴坐标系中的坐标
            t = np.array([self.Lens[i]['t'] for i in range(num_lens)])
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
            for i in range(num_rays):
                self.axes.plot(z[1:num_lens, i], y[1:num_lens, i], self.colors[k])
            # 3. 绘制透镜
            yLast = y.max()

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
            rays = self.lensSys.SkewRayTrace(ray, self.Lens)  # rays保存了光线在每一个透镜面上的坐标，以及方向矢量

            # 2. 计算每一个透镜的高度
            num_lens = int((len(self.Lens) - 2) / 2)
            H_lens = []  # H_lens保存了每一个透镜的孔径
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
                C = self.Lens[nl]['C']  # 曲率
                # 计算第nl个面顶点在z轴上的坐标
                if nl > 0:
                    z0 = z0 + self.Lens[nl - 1]['t']  # 计算第nl个面顶点的z轴坐标
                # 计算透镜圆心
                if C == 0:
                    surf_y = np.array([-H_lens[nl - 1], H_lens[nl - 1]])
                    surf_z = np.array([1, 1]) * z0
                else:
                    r = 1 / C  # 计算半径
                    (a, b) = (z0 + r, 0)  # 透镜中心
                    c = np.arcsin(abs((H_lens[nl - 1] - b) / r))  # 计算透镜最大的角度
                    theta = np.arange(-c, c, 0.01)  # 计算角度范围
                    thetas = np.append(theta, c)
                    surf_z = a - r * np.cos(thetas)  # 计算透镜面z范围
                    surf_y = b + abs(r) * np.sin(thetas)  # 计算透镜面y范围
                # 存储透镜面的坐标
                zRange.append(surf_z)
                yRange.append(surf_y)
                if nl > 0:
                    if nl == self.lensSys.num_lens - 1:
                        self.axes.plot(np.array(surf_z) / self.lensSys.pupilRadius, np.array([-yLast, yLast]), 'k')
                    else:
                        self.axes.plot(np.array(surf_z) / self.lensSys.pupilRadius,
                                       np.array(surf_y) / self.lensSys.pupilRadius,
                                       'k')
                # 绘制透镜上下表面
                if nl > 0 and nl % 2 == 0:
                    self.axes.plot(
                        [zRange[nl - 2][-1] / self.lensSys.pupilRadius, surf_z[-1] / self.lensSys.pupilRadius],
                        [H_lens[nl - 1] / self.lensSys.pupilRadius, H_lens[nl - 1] / self.lensSys.pupilRadius], 'k')
                    self.axes.plot(
                        [zRange[nl - 2][-1] / self.lensSys.pupilRadius, surf_z[-1] / self.lensSys.pupilRadius],
                        [-H_lens[nl - 1] / self.lensSys.pupilRadius, -H_lens[nl - 1] / self.lensSys.pupilRadius], 'k')