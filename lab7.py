import numpy as np

def centroid(p1x, p1y, p2x, p2y, p3x, p3y ,m1 ,m2 ,m3):
    positions = np.array([[p1x, p2x, p3x],
                          [p1y, p2y, p3y]]) #in 2-D
    
    masses = np.array([m1 ,m2, m3]) #in 1-D
    
    tot_mass = np.sum(masses)
    
    cx = np.sum(positions[0,:]*masses) / tot_mass
    cy = np.sum(positions[1,:]*masses) / tot_mass
    

    
    
    return tot_mass, cx, cy

