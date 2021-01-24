import math
import numpy as np
from Geometric_optics2 import opticalSystem
from Geometric_optics2 import drawDiagram
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 1. 输入
    # 1) 光学系统透镜信息(曲率半径，厚度，材料)
    num_Lens = 3
    OriginalLens = [] # 参数一
    # 目前是给定的，所以直接写出来，该部分'm'如果为空格，表示透镜的第二个面
    OriginalLens.append({'C': 0.0, 't': 100.0, 'm': 'vacuum'})
    OriginalLens.append({'C': 1.0 / 40.94, 't': 8.74, 'm': 'SSK4A'})    # 将第一个透镜面添加进去
    OriginalLens.append({'C': 0.0, 't': 11.05, 'm': ' '})
    OriginalLens.append({'C': -1.0 / 55.65, 't': 2.78, 'm': 'SF12'})
    OriginalLens.append({'C': 1.0 / 39.75, 't': 7.63, 'm': ' '})
    OriginalLens.append({'C': 1.0 / 107.56, 't': 9.54, 'm': 'SSK4A'})
    OriginalLens.append({'C': -1.0 / 43.33, 't': 0.0, 'm': ' ', 'n': 35})
    OriginalLens.append({'C': 0, 't': 0, 'm': 'vacuum'})
    
    # 实际中，我们需要根据透镜的个数添加透镜面的信息
    '''
    for nL in range(num_Lens):
        surf1 = {'C': 1.0 / 40.94, 't': 8.74, 'm': 'SSK4A'}    # 根据需求添加
        surf2 = {'C': 0.0, 't': 11.05, 'm': ' '}
    '''
    # 2) 光学系统的基本参数
    pupilRadius = 18.5    # 入瞳孔径大小 参数二
    pupiltheta = 20       # 最大视场角 参数三
    pupilPosition = 4     # 入瞳位置
    # 3) 光线波长
    wavelength = []              # 建立wavelength列表用来存储波长 参数四
    wavelength.append(0.4861)    # 将所需第一个波长的光添加进去
    wavelength.append(0.5876)
    wavelength.append(0.6563)

    # 4) 绘制时的颜色信息
    colors = ['b', 'lime', 'r', 'y']

    # 2. 实例化光学系统
    # 根据波长的不同，对光学系统实例化多次
    lensSys = opticalSystem.LensSys(OriginalLens, pupilRadius, pupiltheta, pupilPosition, wavelength)
    lensSys.calBfl()    # 确定光学系统理想成像面的位置

    # 2. 绘制横向像差点列图
    num_thetas = 4    # 视场角的个数
    # 设置采样规则
    num_phi = 16  # pi内采样数
    num_h = 21  # 孔径直径采样数

    thetasDiagram = np.linspace(0, pupiltheta, num_thetas)    # 定义视场角
    Lateral_apertureRays = pupilRadius    # 光束孔径设置为18.5
    XY, AXY = lensSys.lateralAberration(thetasDiagram, Lateral_apertureRays, num_phi, num_h)    # 返回的是三个波长的X,Y值
    # 确定坐标轴刻度范围
    XYmax = []
    for nw in range(len(wavelength)):
        XYmax.append(np.abs(XY[nw]['X']).max())
        XYmax.append(np.abs(XY[nw]['Y']).max())
    XYmax.append(AXY['X'].max())
    XYmax.append(AXY['Y'].max())
    xymax = math.ceil(max(XYmax) / 0.5) * 0.5
    # 绘制横向像差点列图（刻度需要再稀疏一点、网格画淡一点、视场角个数可选）
    fig = plt.figure()
    for nt in range(len(thetasDiagram)):
        plt.subplot(2, 2, nt + 1)
        plt.xlim(-xymax, xymax)
        plt.ylim(-xymax, xymax)
        plt.plot(AXY['X'], AXY['Y'], c = 'k')
        for nw in range(len(wavelength)):
            X = XY[nw]['X'][:,:,nt].flatten()
            Y = XY[nw]['Y'][:,:,nt].flatten()
            plt.scatter(X, Y, c = colors[nw], marker='+')
        ax = plt.gca()
        ax.xaxis.set_major_locator(plt.MultipleLocator(xymax/5))
        ax.yaxis.set_major_locator(plt.MultipleLocator(xymax/5))
        plt.grid(color = 'gainsboro')
        # plt.xticks([])  # 去x坐标刻度
        # plt.yticks([])  # 去y坐标刻度
        plt.xlabel("z/mm")
        plt.ylabel("y/mm")
    plt.suptitle('Spot diagram')
    plt.show()

    # 3. 绘制径向像差曲线
    Longitude_apertureRays = 2    # 光束孔径设置为2，1/10
    thetasRange = np.array(range(pupiltheta+1))    # 角度范围为0-20
    Error = lensSys.longitudalAberration(thetasRange, Longitude_apertureRays)
    # 确定坐标轴刻度范围
    Emax = []
    Emin = []
    for nw in range(len(wavelength)):
        Emax.append(Error[nw]['xc_error'].max())
        Emax.append(Error[nw]['yc_error'].max())
        Emin.append(Error[nw]['xc_error'].min())
        Emin.append(Error[nw]['yc_error'].min())
    emax = math.ceil((min(Emax) - min(Emin)) / 0.5) * 0.5
    # 绘制径向像差曲线
    plt.figure()
    plt.xlim(-emax, emax)    # 范围有问题
    plt.ylim(0, pupiltheta)
    for nw in range(len(wavelength)):
        plt.plot(Error[nw]['yc_error'], thetasRange, c = colors[nw])    # + abs(min(Emax))
        plt.plot(Error[nw]['xc_error'], thetasRange, c = colors[nw], linestyle='--')
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator(emax / 5))    # 0.4自动化
    ax.yaxis.set_major_locator(plt.MultipleLocator(pupiltheta / 10))    # 2自动化
    plt.grid()
    plt.title('Longitudal Aberration')
    plt.xlabel('range/mm')
    plt.ylabel('angle/degree')
    plt.show()

    # 4. 绘制畸变曲线
    Distortion = lensSys.distortion(thetasRange)
    # 确定坐标轴刻度范围
    Dmax = []
    Dmin = []
    for nw in range(len(wavelength)):
        Dmax.append(Distortion[nw].max())
        Dmax.append(Distortion[nw].max())
        Dmin.append(Distortion[nw].min())
        Dmin.append(Distortion[nw].min())
    dmax = math.ceil((max(Dmax) - min(Dmin)) / 0.1) * 0.1
    # 绘制畸变曲线
    plt.figure()
    plt.xlim(-dmax, dmax)
    plt.ylim(0, pupiltheta)
    for nw in range(len(wavelength)):
        Distortion[nw][0] = Distortion[nw][0] + Distortion[nw][1]
        plt.plot(Distortion[nw], thetasRange, color = colors[nw])
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator(dmax / 5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(pupiltheta / 10))
    plt.grid()
    plt.title('Distortion')
    plt.xlabel('percent/%')
    plt.ylabel('angle/degree')
    plt.show()

    # 5. 绘制光线追迹示意图
    num_rays = 3
    for i in range(len(thetasDiagram)):
        drawRays = drawDiagram.drawDiagram(lensSys)
        drawRays.drawRayTrace(thetasDiagram[i], num_rays, colors[i])
    plt.show()