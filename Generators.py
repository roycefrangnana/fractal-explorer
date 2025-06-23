import numpy as np
import cv2 as cv
import random
import math


def generate_fern_cv(points, scale, st_color, end_color, bg_color, thick=1):
    width, height = 600, 700
    img = np.full((height, width, 3), bg_color, dtype=np.uint8)
    x, y = 0, 0
    frames = []

    for i in range(points):
        r = np.random.random()
        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

        px = int(width / 2 + x * scale)
        py = int(height - y * scale)

        if 0 <= px < width and 0 <= py < height:
            t = i / points
            color = [
                int(st_color[j] * (1 - t) + end_color[j] * t)
                for j in range(3)
            ]
            cv.circle(img, (px, py), thick, color, -1)  # ← draw the point here

        if i % 100 == 0:
            frames.append(img.copy())

    frames.append(img)
    return frames

def generate_triangle(depth,st_color,end_color,bg_color,thick):
    width,height=600,600
    img = np.full((height, width, 3), bg_color, dtype=np.uint8)
    frames=[]
    Q=[]
    def funct(d, a, b, c):
        if d == 0:
            return

        # Keep points as floats for accurate math
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        Q.append([a, b, c, d])
        # Draw triangle (convert only for drawing)
        # Midpoints (stay in float)
        ab = (a + b) / 2
        bc = (b + c) / 2
        ca = (c + a) / 2

        # Recursive calls
        funct(d - 1, a, ab, ca)
        funct(d - 1, ab, b, bc)
        funct(d - 1, ca, bc, c)

    i = depth
    funct(depth, (300, 50), (50, 550), (550, 550))
    while i > 0:
        t = i / depth
        color = [
            int(end_color[j] * (1 - t) + st_color[j] * t)
            for j in range(3)
        ]
        for l in Q:
            if l[3] == i:
                a, b, c = l[0], l[1], l[2]
                cv.line(img, tuple(a.astype(int)), tuple(b.astype(int)), color, thick)
                cv.line(img, tuple(b.astype(int)), tuple(c.astype(int)), color, thick)
                cv.line(img, tuple(c.astype(int)), tuple(a.astype(int)), color, thick)
                r=random.randint(1,10)
                if depth >8 and i<5:
                    continue
                if i<depth-2 and r%80!=0:
                    continue
                frames.append(img.copy())

        i -= 1
    frames.append(img)
    return frames


def generate_carpet(depth,st_color,end_color,bg_color,thick):
    width, height = 600, 600
    img = np.full((height, width, 3), bg_color, dtype=np.uint8)
    frames = []
    Q = []

    def sierpinski_carpet(x, y, size, depth):
        if depth == 0:
            return

        new_size = size // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue  # skip center
                new_x = x + i * new_size
                new_y = y + j * new_size
                Q.append((new_x, new_y, new_size, depth))
                sierpinski_carpet(new_x, new_y, new_size, depth - 1)

    sierpinski_carpet(50, 50, 500, depth)
    i = depth
    while i > 0:
        t = i / depth
        color = [
            int(end_color[j] * (1 - t) + st_color[j] * t)
            for j in range(3)
        ]
        for x, y, s, d in Q:
            if d == i:
                cv.rectangle(img, (x, y), (x + s, y + s), color, thick)
                r=random.randint(1,20)
                if i<depth-2 and r%100!=0 :
                    continue
                frames.append(img.copy())

        i -= 1
    frames.append(img)
    return frames


def generate_tree(depth, st_color,end_color, bg_color,turn):
    width, height = 600, 600
    img = np.full((height, width, 3), bg_color, dtype=np.uint8)
    frames = []
    Q = []

    def get_points(x1, y1, size, ang, d):
        if d == 0:
            return
        x2 = int(x1 + size * np.cos(np.radians(ang)))
        y2 = int(y1 - size * np.sin(np.radians(ang)))
        Q.append([(x1, y1), (x2, y2), d])

        get_points(x2, y2, size * 0.7, ang - turn, d - 1)
        get_points(x2, y2, size * 0.7, ang + turn, d - 1)

    get_points(300, 550, 155, 90, depth)
    i = depth
    while i > 0:
        t = i / depth
        color = [
            int(end_color[j] * (1 - t) + st_color[j] * t)
            for j in range(3)
        ]
        for l in Q:
            if l[2] == i:
                cv.line(img, l[0], l[1], color, thickness=max(1, i // 2))
                r=random.randint(1,20)
                if depth>8 and i<3:
                    continue
                if i>depth-3 and r%50!=0:
                    continue
                frames.append(img.copy())

        i -= 1
    frames.append(img)
    return frames


def generate_flake(depth, st_color, bg_color, thick):
    width, height = 800, 800
    frames = []

    def draw_koch_curve(img, start_point, end_point, current_depth, target_depth):
        if current_depth == 0:
            color = st_color  # Use the provided flake color
            cv.line(img, (int(start_point[0]), int(start_point[1])),
                    (int(end_point[0]), int(end_point[1])), color, thick)
            return

        pA = start_point
        pD = end_point
        pB = pA + (pD - pA) / 3
        pC = pA + 2 * (pD - pA) / 3

        x_b, y_b = pB[0], pB[1]
        x_c, y_c = pC[0], pC[1]

        pM_x = 0.5 * (x_b + x_c) - (y_c - y_b) * np.sqrt(3) / 2
        pM_y = 0.5 * (y_b + y_c) + (x_c - x_b) * np.sqrt(3) / 2
        pM = np.array([pM_x, pM_y])

        draw_koch_curve(img, pA, pB, current_depth - 1, target_depth)
        draw_koch_curve(img, pB, pM, current_depth - 1, target_depth)
        draw_koch_curve(img, pM, pC, current_depth - 1, target_depth)
        draw_koch_curve(img, pC, pD, current_depth - 1, target_depth)

    # Canvas setup
    side_length = min(width, height) * 0.7
    center_x, center_y = width // 2, height // 2

    p_top = np.array([center_x, center_y - side_length * np.sqrt(3) / 3])
    p_bl = np.array([center_x - side_length / 2, center_y + side_length * np.sqrt(3) / 6])
    p_br = np.array([center_x + side_length / 2, center_y + side_length * np.sqrt(3) / 6])

    for d in range(depth + 1):
        img = np.full((height, width, 3), bg_color, dtype=np.uint8)

        draw_koch_curve(img, p_top, p_bl, d, d)
        draw_koch_curve(img, p_bl, p_br, d, d)
        draw_koch_curve(img, p_br, p_top, d, d)

        frames.append(img)

    return frames

#------------------------------------------------------------------------------------

def generate_dragon(max_depth, fg_color, bg_color, thickness, angle_deg):
    width, height = 600, 600
    frames = []
    angle_rad = math.radians(angle_deg)  # ✅ Convert angle to radians

    # Start from center with a horizontal line
    p0 = (width // 3, height // 2)
    p1 = (2 * width // 3, height // 2)

    def draw_dragon(img, p0, p1, depth):
        if depth == 0:
            cv.line(img, (int(p0[0]), int(p0[1])), (int(p1[0]), int(p1[1])), fg_color, thickness)
            return

        # Find midpoint
        mx = (p0[0] + p1[0]) / 2
        my = (p0[1] + p1[1]) / 2

        # Vector from p0 to p1
        dx = (p1[0] - p0[0]) / 2
        dy = (p1[1] - p0[1]) / 2

        # ✅ Rotate the vector by custom angle
        rx = dx * math.cos(angle_rad) - dy * math.sin(angle_rad)
        ry = dx * math.sin(angle_rad) + dy * math.cos(angle_rad)

        # Midpoint after rotation
        px = mx - rx
        py = my - ry
        mid = (px, py)

        draw_dragon(img, p0, mid, depth - 1)
        draw_dragon(img, p1, mid, depth - 1)

    for current_depth in range(1, max_depth + 1):
        frame = np.full((height, width, 3), bg_color, dtype=np.uint8)
        draw_dragon(frame, p0, p1, current_depth)
        frames.append(frame.copy())

    return frames


#-----------------------------------------------------------------------------------------
def generator_cantor(depth,st_color,end_color,bg_color):
    width, height = 1000, 600
    frames = []
    Q=[]
    img=np.full((height, width, 3), bg_color, dtype=np.uint8)

    def points_cantor(X, size, depth):
        if depth == 0:
            return
        Q.append([int(X), int(X + size), depth])
        points_cantor(X, size / 3, depth - 1)
        points_cantor(X + (2 * size / 3), size / 3, depth - 1)

    points_cantor(20,960,depth)
    i=depth
    while i > 0:
        t = i / depth
        color = [
            int(end_color[j] * (1 - t) + st_color[j] * t)
            for j in range(3)
        ]
        for l in Q:
            if l[2] == i:
                Y = int(550 * (1 - i / depth))
                cv.line(img, (l[0], Y + 25), (l[1], Y + 25), color, thickness=i)
                frames.append(img.copy())
        i -= 1
    return frames

def generate_mandelbrot(x0, y0, grid_option):
    if grid_option == 1:
        img = cv.imread("images/Mandelbrot_gridon.png")
    else:
        img = cv.imread("images/Mandelbrot_gridoff.png")

    height, width = img.shape[:2]
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5

    c = complex(x0, y0)
    z = 0
    max_iter = 100
    points = []

    for _ in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            break
        zx = int((z.real - x_min) / (x_max - x_min) * width)
        zy = int((z.imag - y_min) / (y_max - y_min) * height)
        if 0 <= zx < width and 0 <= zy < height:
            points.append((zx, zy))

    for i in range(1, len(points)):
        cv.line(img, points[i - 1], points[i], (0, 255, 255), 1, cv.LINE_AA)

    return img

def generate_julia(c_x,c_y):
    frames=[]
    w,h=800,800
    max_iter = 100
    xmin, xmax = -1.5, 1.5
    ymin, ymax = -1.5, 1.5

    x = np.linspace(xmin, xmax, w)
    y = np.linspace(ymin, ymax, h)
    re, im = np.meshgrid(x, y)

    z_real_full = re.copy()
    z_imag_full = im.copy()
    z_real = z_real_full.copy()
    z_imag = z_imag_full.copy()
    img = np.zeros((h, w), dtype=np.uint8)
    mask = np.ones((h, w), dtype=bool)
    for i in range(1, max_iter + 1):
        # Perform one iteration step only on active points
        z_real2 = z_real[mask] ** 2
        z_imag2 = z_imag[mask] ** 2

        z_temp = z_real2 - z_imag2 + c_x
        z_imag_new = 2 * z_real[mask] * z_imag[mask] + c_y

        z_real[mask] = z_temp
        z_imag[mask] = z_imag_new

        mag2 = z_real[mask] ** 2 + z_imag[mask] ** 2
        still_bounded = mag2 <= 4

        # Update mask
        new_mask = np.zeros_like(mask)
        new_mask[mask] = still_bounded
        mask = new_mask

        # Increase iteration count for bounded pixels
        img[mask] += 1

        # Normalize and color the frame
        img_norm = cv.normalize(img, None, 0, 255, cv.NORM_MINMAX)
        color_img = cv.applyColorMap(img_norm, cv.COLORMAP_MAGMA)
        frames.append(color_img)

    return frames
def generate_hilbert(level,line_color,bg_color,show_grid):
    frames=[]
    size = 512
    margin = 20
    grid_color = (100, 100, 100)

    img = np.full((size, size, 3), bg_color, dtype=np.uint8)
    points = []

    def hilbert(x, y, xi, xj, yi, yj, n):
        if n <= 0:
            x_mid = int(x + (xi + yi) / 2)
            y_mid = int(y + (xj + yj) / 2)
            points.append((x_mid, y_mid))
        else:
            hilbert(x, y, yi / 2, yj / 2, xi / 2, xj / 2, n - 1)
            hilbert(x + xi / 2, y + xj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)
            hilbert(x + xi / 2 + yi / 2, y + xj / 2 + yj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)
            hilbert(x + xi / 2 + yi, y + xj / 2 + yj, -yi / 2, -yj / 2, -xi / 2, -xj / 2, n - 1)

    N = 2 ** level
    step = (size - 2 * margin) / N

    # ==== Draw Grid (optional) ====
    if show_grid:
        for i in range(N + 1):
            x = int(margin + i * step)
            y = int(margin + i * step)
            cv.line(img, (x, margin), (x, size - margin), grid_color, 1)
            cv.line(img, (margin, y), (size - margin, y), grid_color, 1)

    # ==== Draw Hilbert Curve ====
    hilbert(margin, margin, step * N, 0, 0, step * N, level)
    if level>=4:
        j=10
    else:
        j=60
    for i in range(1, len(points)):
        pt1 = tuple(map(int, points[i - 1]))
        pt2 = tuple(map(int, points[i]))
        cv.line(img, pt1, pt2, line_color, 1, cv.LINE_AA)
        if i%j==0:
            frames.append(img.copy())
    frames.append(img)
    return frames

def gen_chaotriangle(iterations, st_color, end_color, bg_color,thickness):
    size=600
    frames = []
    img = np.full((size, size, 3), bg_color, dtype=np.uint8)
    pt = (300, 300)
    points = [(300, 50), (50, 550), (550, 550)]
    for i in range(iterations):
        ch = random.choice(points)
        x = (ch[0] + pt[0]) / 2
        y = (ch[1] + pt[1]) / 2
        c=(int(x), int(y))
        t = i / iterations
        color = [
            int(st_color[j] * (1 - t) + end_color[j] * t)
            for j in range(3)
        ]
        cv.circle(img,c,thickness,color,-1)
        if i<200 and i%15==0:
            frames.append(img.copy())
        elif i%180==0:
            frames.append(img.copy())
        pt = (x, y)
    frames.append(img)
    return frames

def gen_chaocarp(iterations, st_color, end_color, bg_color, thickness):
    size = 600
    frames = []
    img = np.full((size, size, 3), bg_color, dtype=np.uint8)
    pt = (300, 300)
    points = [
        (100, 100), (300, 100), (500, 100),
        (100, 300), (500, 300),
        (100, 500), (300, 500), (500, 500)
    ]

    for i in range(iterations):
        ch = random.choice(points)
        x = (pt[0] + 2 * ch[0]) / 3
        y = (pt[1] + 2 * ch[1]) / 3
        c = (int(x), int(y))
        t = i / iterations
        color = [
            int(st_color[j] * (1 - t) + end_color[j] * t)
            for j in range(3)
        ]
        cv.circle(img, c, thickness, color, -1)
        if i < 200 and i % 15 == 0:
            frames.append(img.copy())
        elif i % 150 == 0:
            frames.append(img.copy())
        pt = (x, y)
    frames.append(img)
    return frames


def gen_frost(iterations, st_color, end_color, bg_color, thickness):
    size = 600
    frames = []
    img = np.full((size, size, 3), bg_color, dtype=np.uint8)
    pt = (300, 300)
    points = [(550, 300), (425, 516), (175, 516), (50, 300), (175, 83), (425, 83)]

    for i in range(iterations):
        ch = random.choice(points)
        x = (pt[0] + 2 * ch[0]) / 3
        y = (pt[1] + 2 * ch[1]) / 3
        c = (int(x), int(y))
        t = i / iterations
        color = [
            int(st_color[j] * (1 - t) + end_color[j] * t)
            for j in range(3)
        ]
        cv.circle(img, c, thickness, color, -1)
        if i < 200 and i % 15 == 0:
            frames.append(img.copy())
        elif i % 150 == 0:
            frames.append(img.copy())
        pt = (x, y)
    frames.append(img)
    return frames

def gen_hexwing(iterations,st_color,end_color,bg_color,thickness):
    size = 600
    frames = []
    img = np.full((size, size, 3), bg_color, dtype=np.uint8)
    pt = [300, 300]
    val=range(0,6)
    vertices = [(550, 300), (425, 516), (175, 516), (50, 300), (175, 83), (425, 83)]

    for i in range(iterations):
        r = random.choice(val)
        k = vertices[r]
        if r == 0 or r == 3:
            pt[0] = (k[0] + 2 * pt[0]) / 3
            pt[1] = (k[1] + 2 * pt[1]) / 3
        else:
            pt[0] = (5 * k[0] + pt[0]) / 6
            pt[1] = (5 * k[1] + pt[1]) / 6
        cen = (int(pt[0]), int(pt[1]))
        t = i / iterations
        color = [
            int(st_color[j] * (1 - t) + end_color[j] * t)
            for j in range(3)
        ]
        cv.circle(img, cen, thickness, color, -1)
        if i < 200 and i % 15 == 0:
            frames.append(img.copy())
        elif i % 150 == 0:
            frames.append(img.copy())
    frames.append(img)
    return frames

def gen_hexflake(iterations, st_color, end_color, bg_color, thickness):
    size = 600
    frames = []
    img = np.full((size, size, 3), bg_color, dtype=np.uint8)
    cx, cy, r = 300, 300, 400

    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = int(cx + r * math.cos(angle))
        y = int(cy + r * math.sin(angle))
        points.append((x, y))

    x, y = random.randint(200, 400), random.randint(200, 400)
    last_idx = -1

    def non_adjacent_index(last):
        return random.choice([i for i in range(6) if abs(i - last) not in [0, 1, 5]])

    for i in range(iterations):
        idx = non_adjacent_index(last_idx)
        tx, ty = points[idx]
        x = (x + tx) / 2
        y = (y + ty) / 2
        t = i / iterations
        color = [
            int(st_color[j] * (1 - t) + end_color[j] * t)
            for j in range(3)
        ]
        cen=(int(x),int(y))
        cv.circle(img,cen,thickness,color,-1)
        last_idx = idx
        if i < 200 and i % 15 == 0:
            frames.append(img.copy())
        elif i % 150 == 0:
            frames.append(img.copy())
    frames.append(img)
    return frames


def gen_petal(iterations, st_color, end_color, bg_color, thickness,n_pet):
    size = 600
    frames = []
    img = np.full((size, size, 3), bg_color, dtype=np.uint8)
    cx, cy, r = 300, 300, 400

    points = []
    for i in range(n_pet):
        angle = math.radians(360 * i/n_pet)
        x = int(cx + r * math.cos(angle))
        y = int(cy + r * math.sin(angle))
        points.append((x, y))
    for _ in range(1200):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, 35)
        x = int(cx + radius * math.cos(angle))
        y = int(cy + radius * math.sin(angle))
        color = random.choice([
            (0, 230, 255),  # yellow center
            (0, 180, 255),  # golden-orange
        ])
        if 0 <= x < 600 and 0 <= y < 600:
            img[y, x] = color

    x, y = random.randint(200, 400), random.randint(200, 400)
    last_idx = -1

    def non_adjacent_index(last):
        return random.choice([i for i in range(n_pet) if abs(i - last) not in [0, 1, n_pet-1]])

    for i in range(iterations):
        if last_idx == -1:
            idx = random.randint(0, n_pet - 1)
        else:
            idx = non_adjacent_index(last_idx)

        tx, ty = points[idx]
        x = (x + tx) / 2
        y = (y + ty) / 2
        t = i / iterations
        color = [
            int(st_color[j] * (1 - t) + end_color[j] * t)
            for j in range(3)
        ]
        cen=(int(x),int(y))
        cv.circle(img,cen,thickness,color,-1)
        last_idx = idx
        if i < 200 and i % 15 == 0:
            frames.append(img.copy())
        elif i % 150 == 0:
            frames.append(img.copy())
    frames.append(img)
    return frames
