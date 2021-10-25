def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError('The LEngth of cuboid can onlt be int or a float')
    return (l*l*l)
