def calculate_cuboid(L,B,H):
    surface_area = 2 * (L * B + B * H + H * L)
    volume = L * B * H
    return surface_area, volume
l=int(input())
b=int(input())
h=int(input())
print(calculate_cuboid(l,b,h))