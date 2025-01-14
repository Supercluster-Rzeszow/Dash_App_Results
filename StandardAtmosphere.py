import math
import numpy as np
import pandas as pd

e   =   2.71828182846
def Height():
    H   =   list(range(0, 84000))
    return  H
#-----------------------------------------------    
def Temperature(H):

    if H <= 11000:
        Tb      =   288.15
        Beta    =   -0.0065
        Hb      =   0
    elif H > 11000 and H <= 20000:
        Tb      =   216.65
        Beta    =   0      
        Hb      =   11000
    elif H > 20000 and H <= 32000:
        Tb      =   216.65
        Beta    =   0.001      
        Hb      =   20000
    elif H > 32000 and H <= 47000:
        Tb      =   228.65
        Beta    =   0.0028    
        Hb      =   32000
    elif H > 47000 and H <= 51000:
        Tb      =   270.65
        Beta    =   0   
        Hb      =   47000
    elif H > 51000 and H <= 71000:
        Tb      =   270.65
        Beta    =   -0.0028   
        Hb      =   51000
    elif H > 71000 and H <= 84000:
        Tb      =   214.65
        Beta    =   -0.002   
        Hb      =   71000
    Th   =   Tb + Beta * (H-Hb)
    
    return  Th    
#-----------------------------------------------        
def Pressure(H, Th):  

    R = 287.052
    g = 9.80665
    
    if H <= 11000:
        Tb      =   288.15
        Beta    =   -0.0065
        Hb      =   0
        pb      =   101325
    elif H > 11000 and H <= 20000:
        Tb      =   216.65
        Beta    =   0      
        Hb      =   11000
        pb      =   22632.1
    elif H > 20000 and H <= 32000:
        Tb      =   216.65
        Beta    =   0.001      
        Hb      =   20000
        pb      =   5474.9
    elif H > 32000 and H <= 47000:
        Tb      =   228.65
        Beta    =   0.0028    
        Hb      =   32000
        pb      =   868.02
    elif H > 47000 and H <= 51000:
        Tb      =   270.65
        Beta    =   0   
        Hb      =   47000
        pb      =   110.91
    elif H > 51000 and H <= 71000:
        Tb      =   270.65
        Beta    =   -0.0028   
        Hb      =   51000
        pb      =   66.939
    elif H > 71000 and H <= 84000:
        Tb      =   214.65
        Beta    =   -0.002   
        Hb      =   71000
        pb      =   3.9564
        
    if Beta != 0:
        ph = pb * (1 + Beta/Tb * (H - Hb))**(-g/(Beta * R))
        
    elif Beta == 0:
        ph = pb * e**(-g/(R*Th) * (H - Hb))   
        
    return ph
 #-----------------------------------------------  
def Density(Th, ph):  
    R   =   287.052

    rho_h = ph / (R * Th)
        
    return rho_h
 #-----------------------------------------------  
def SpeedOfSound(Th):  

    R   =   287.052
    k   =   1.41
       
    a_h = (k * R * Th)**(1/2)
        
    return a_h    
#-----------------------------------------------
def MainLoop():
    height  =   Height()
    GM      =   3.986004e+14
    ER      =   6.3781e+06
    SimBase =   0.1
    SimTime =   72000
    TimeVector = np.arange(0,SimTime, SimBase)
    T           =   [0] * len(TimeVector)
    p           =   [0] * len(TimeVector)
    rho         =   [0] * len(TimeVector)
    g           =   [0] * len(TimeVector)
    F_G         =   [0] * len(TimeVector)
    F_B         =   [0] * len(TimeVector)
    F_D         =   [0] * len(TimeVector)
    a           =   [0] * len(TimeVector)
    v           =   [0] * len(TimeVector)
    h           =   [0] * len(TimeVector)
    r           =   [0] * len(TimeVector)
    A_b         =   [0] * len(TimeVector)  
    V_b         =   [0] * len(TimeVector)
    ascent_rate =   [0] * len(TimeVector)

    h_offset = 100            # height above the mean sea level 
    burst_altitude = 0
    time_to_burst = 0
    neck_lift = 0
    launch_radius = 0
    V_b[0] = 1.1         # initial baloon volume 
    t_0 = 0
    rho_He = 0.1786
    C_d = 0.3
    BaloonMass = 0.45
    PayloadMass = 0.25
    TotalMass = BaloonMass + PayloadMass
    r_pop = 2.36
    pop_time = 0
    pop_height = 0


    #pierwsza pętla
    h[0]            = 0 + h_offset
    T[0]            = Temperature(h[0])
    p[0]            = Pressure(h[0], T[0])
    rho[0]          = Density(T[0], p[0])
    k_constant      = (p[0]*V_b[0])/T[0]
    g[0]            = GM / (ER + h[0])**2
    F_G[0]          = TotalMass * g[0]
    F_D[0]          = 0
    V_b[0]          = (k_constant * T[0])/p[0]
    A_b[0]          = math.pi * ((3*V_b[0])/(4*math.pi))**(2/3)
    r[0]            = math.sqrt(A_b[0]/math.pi)
    F_B[0]          = -1 * V_b[0] * (rho_He - rho[0]) * g[0]
    a[0]            = 0
    v[0]            = 0
    calka_v         = 0
    calka_h         = 0 + h[0]

    for i in range(1,len(TimeVector)):
        T[i]            = Temperature(h[i-1])
        p[i]            = Pressure(h[i-1], T[i])
        rho[i]          = Density(T[i], p[i])
        V_b[i]          = (k_constant * T[i])/p[i]
        g[i]            = GM / (ER + h[i])**2
        F_B[i]          = V_b[i] * rho[i] * g[i]
        F_G[i]          = TotalMass * g[i]
        A_b[i]          = math.pi * ((3*V_b[i])/(4*math.pi))**(2/3)
        r[i]            = math.sqrt(A_b[i]/math.pi) 
        F_D[i]          = 0.5*C_d*A_b[i]*((v[i-1])**2)
        
        a[i]            = (F_B[i] - F_G[i] - F_D[i])/TotalMass
           
        calka_v         = calka_v + (a[i] + a[i-1]) * 0.5 * SimBase
        v[i]            = calka_v
       
        calka_h         = calka_h + (v[i] + v[i-1]) * 0.5 * SimBase
        h[i]            = calka_h

        if r[i] >= r_pop:
            pop_time    = i*SimBase
            pop_height  = h[i]
            break


    output_data = pd.DataFrame(np.transpose(np.array([TimeVector, h, v, a, T, p, rho, g, F_G, F_B, F_D, V_b, A_b, r])),
                    columns=['Time [s]', 'Height [m]', 'Vertical speed [m/s]',
                             'Acceleration [m/s^2]', 'Temperature [K]', 'Pressure [Pa]',
                             'Density [kg/m^3]', 'Gravitational acceleration [m/s^2]',
                             'Gravity [N]', 'Buoyancy [N]', 'Drag [N]',
                             'Baloon volume [m^3]', 'Baloon cross-section area [m^2]', 'Baloon radius [m]'])
                                
    return output_data, pop_time, pop_height
#-----------------------------------------------

#-----------------------------------------------

output_data, pop_time, pop_height = MainLoop()
print(pop_height)
