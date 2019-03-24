def minmax(points):
    x = sorted(map(lambda p: p[0], points))
    y = sorted(map(lambda p: p[1], points))
    z = sorted(map(lambda p: p[2], points))
    return { 'xmin': x[0],
             'xmax': x[-1],
             'ymin': y[0],
             'ymax': y[-1],
             'zmin': z[0],
             'zmax': z[-1] }

def boundingbox(points):
    mm = minmax(points)
    return [ mm['xmax'] - mm['xmin'],
             mm['ymax'] - mm['ymin'],
             mm['zmax'] - mm['zmin'] ]

def center(points):
    mm = minmax(points)
    return [ (mm['xmin'] + mm['xmax']) / 2,
             (mm['ymin'] + mm['ymax']) / 2,
             (mm['zmin'] + mm['zmax']) / 2 ]
