import streamlit as st
import time
import cv2
import imageio
from io import BytesIO
from Generators import generate_fern_cv, generate_triangle, generate_carpet, generate_tree, generate_flake, \
    generate_dragon, generator_cantor, generate_mandelbrot,generate_julia,generate_hilbert,gen_chaotriangle, \
    gen_chaocarp, gen_frost, gen_hexwing, gen_hexflake, gen_petal
from Home_mind_pages import Minds_Page, Home, Nature_Page, gallery

def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))  # BB, GG, RR → BGR

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Session state for navigation
if 'clicked' not in st.session_state:
    st.session_state.clicked = 'A'

# Sidebar buttons
with st.sidebar:
    st.markdown('<div class="custom-button home">', unsafe_allow_html=True)
    if st.button("Home 🏠", key="home"):
        st.session_state.clicked = 'A'
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="custom-button minds">', unsafe_allow_html=True)
    if st.button("Minds Behind Fractals", key="minds"):
        st.session_state.clicked = 'B'
    if st.button("Nature and Fractals"):
        st.session_state.clicked='NaF'
    if st.button("Fractal Gallery"):
        st.session_state.clicked='gal'
    st.markdown('</div>', unsafe_allow_html=True)

    st.title("Fractal Explorers")

    st.markdown('<div class="custom-button fractals">', unsafe_allow_html=True)
    st.subheader("Chaos Game")
    if st.button("Barnsley Fern"):
        st.session_state.clicked = 'C'
    if st.button("Sierpiński Triangle",key='1'):
        st.session_state.clicked = 'CD'
    if st.button("Sierpiński Carpet",key='2'):
        st.session_state.clicked = 'DE'
    if st.button("Frost Bloom"):
        st.session_state.clicked= 'EF'
    if st.button("HexaWing"):
        st.session_state.clicked= 'FG'
    if st.button("HexaFlake"):
        st.session_state.clicked= 'GH'
    if st.button("PetalBurst"):
        st.session_state.clicked= 'HI'
    st.subheader("Geometric Fractals")
    if st.button("Sierpiński Triangle",key='3'):
        st.session_state.clicked = 'D'
    if st.button("Sierpiński Carpet",key='4'):
        st.session_state.clicked = 'E'
    if st.button("Binary Tree"):
        st.session_state.clicked= 'F'
    if st.button("Koch Snowflake"):
        st.session_state.clicked= 'G'
    if st.button("Dragon Curve"):
        st.session_state.clicked= 'H'
    if st.button("Cantor Set"):
        st.session_state.clicked='I'
    if st.button("Mandelbrot Set"):
        st.session_state.clicked='J'
    if st.button("Julia set"):
        st.session_state.clicked='K'
    if st.button("Hilbert Curve"):
        st.session_state.clicked='L'
    st.markdown('</div>', unsafe_allow_html=True)

# Page content based on click
if st.session_state.clicked == 'A':
    Home()
elif st.session_state.clicked == 'B':
    st.title("Unveiling The Brains Behind The Fractals  ")
    st.write("✨ Honoring the Thinkers Who Turned Math Into Art")
    Minds_Page()
elif st.session_state.clicked == 'NaF':
    Nature_Page()
elif st.session_state.clicked == 'gal':
    gallery()
elif st.session_state.clicked == 'C':

    #--------------------------------
    st.title("🌿Barnsley Fern Fractal Explorer")
    st.write("A beautiful fractal that looks like a real fern!")
    st.subheader("🎛️ Controls Section")
    col1,col2=st.columns(2)
    with col1:
        points=st.slider("No of points", 5000, 20000,6000,step=500)
        s_col1,s_col2,s_col3=st.columns(3)
        with s_col1:
            st_color=st.color_picker("Starting color","#00FF00")
        with s_col2:
            end_color=st.color_picker("Ending color","#A3FF00")
        with s_col3:
            bg_color=st.color_picker("background color","#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        thickness = st.slider("Dot size ",1,5,1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    #generator_fern
    scale = 65
    if st.button("Generate"):
        frames = generate_fern_cv(points, scale, st_bgr, end_bgr, bg_bgr,thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        final_image = frames[-1]

        _, buffer = cv2.imencode('.png', final_image)
        img_bytes = BytesIO(buffer)

        gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
        gif_bytes = BytesIO()

        imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
        gif_bytes.seek(0)
        img_bytes.seek(0)
        c1,c2=st.columns(2)
        with c1:
            st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="barnsley_fern.png",
                           mime="image/png")
        with c2:
            st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="barnsley_fern.gif",
                           mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🌿 The math behind the Barnsley Fern uses affine transformations of the form:\n\n"
            "    Y = A·X + B\n"
            "Where:  \n"
            "📌 X = [x, y]ᵗ   (current point)  \n"
            "📌 A = 2×2 matrix (rotation + scaling)  \n"
            "📌 B = 2×1 vector (translation)\n\n"
            "Each rule uses a different A and B:\n\n"
            
            "🔹 Rule 1 (Stem) — used 1%:\n"
            "    A = [[ 0.00,  0.00],\n"
            "         [ 0.00,  0.16]],\n"
            "    B = [0, 0]\n\n"
        
            "🔹 Rule 2 (Leafy part) — used 85%:\n"
            "    A = [[ 0.85,  0.04],\n"
            "         [-0.04,  0.85]],\n"
            "    B = [0, 1.6]\n\n"
        
            "🔹 Rule 3 (Left leaflets) — used 7%:\n"
            "    A = [[ 0.20, -0.26],\n"
            "         [ 0.23,  0.22]],\n"
            "    B = [0, 1.6]\n\n"
        
            "🔹 Rule 4 (Right leaflets) — used 7%:\n"
            "    A = [[-0.15,  0.28],\n"
            "         [ 0.26,  0.24]],\n"
            "    B = [0, 0.44]\n\n"
            "🌿 Barnsley Fern is made by repeating simple math steps many times. Here's the full story:\n\n"
            "We start with a dot at (0, 0). Then, again and again, we choose one of four rules (formulas) to move the dot to a new place.\n\n"
            "Each rule has a different job, and is chosen randomly with specific probabilities:\n\n"
            "🔹 Rule 1 (Stem) — used 1% of the time:  \n"
            "    x_new = 0  \n                y_new = 0.16 * y  \n"
            "    → Shrinks the dot straight down. This forms the thin stem at the bottom.\n\n"
            "🔹 Rule 2 (Successive leaflets) — used 85% of the time:  \n"
            "    x_new = 0.85 * x + 0.04 * y  \n"
            "    y_new = -0.04 * x + 0.85 * y + 1.6  \n"
            "    → Gently turns and moves the dot upward — draws the main leafy part.\n\n"
            "🔹 Rule 3 (Left leaflets) — used 7% of the time:  \n"
            "    x_new = 0.2 * x - 0.26 * y  \n"
            "    y_new = 0.23 * x + 0.22 * y + 1.6  \n"
            "    → Adds left-side smaller leaves.\n\n"
            "🔹 Rule 4 (Right leaflets) — used 7% of the time:  \n"
            "    x_new = -0.15 * x + 0.28 * y \n"
            "    y_new = 0.26 * x + 0.24 * y + 0.44  \n"
            "    → Adds right-side smaller leaves.\n\n"
            "🎯 Because these rules are picked with different chances, most points form the leafy top,\n"
            "while fewer build the stem or side branches.\n\n"
            "📌 This method is called an Iterated Function System (IFS) — where we apply transformations repeatedly.\n"
            "Even with randomness, math creates a realistic fern!"
        )

    #-------------------------------------
elif st.session_state.clicked == 'CD':
    st.title("🔺Sierpiński Triangle Fractal Explorer")
    st.write("A classic fractal generated by randomly jumping halfway toward triangle vertices.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        points = st.slider("No of points", 5000, 10000, 6000, step=500)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#FFB200")
        with s_col2:
            end_color = st.color_picker("Ending color", "#FF4200")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        thickness = st.slider("Dot size ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames=gen_chaotriangle(points, st_bgr, end_bgr, bg_bgr,thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        final_image = frames[-1]

        _, buffer = cv2.imencode('.png', final_image)
        img_bytes = BytesIO(buffer)

        gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
        gif_bytes = BytesIO()

        imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
        gif_bytes.seek(0)
        img_bytes.seek(0)
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="sierpinski_triangle.png",
                               mime="image/png")
        with c2:
            st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="sierpinski_triangle.gif",
                               mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🎲 The **Chaos Sierpiński Triangle** is built not by cutting — but by randomness!\n\n"
            "Here’s how it works:\n\n"
            "1️⃣ Start with 3 points forming a triangle — call them the *attractors*.\n\n"
            "2️⃣ Choose a random starting point anywhere on the canvas.\n\n"
            "3️⃣ Pick one of the triangle’s corners randomly.\n\n"
            "4️⃣ Move **halfway** from the current point toward that corner.\n\n"
            "5️⃣ Plot the new point, and repeat the process millions of times!\n\n"
            "🌟 Surprisingly, this simple random game reveals the exact same fractal pattern as the deterministic method!\n\n"
            "📌 This is called a **stochastic fractal** — where **randomness creates order**.\n\n"
            "🧠 No cutting, no shrinking — just bouncing around the triangle in a chaotic dance that leaves behind a beautiful structure."
        )


#-----------------------------------------------------------------------------------
elif st.session_state.clicked == 'DE' :
    st.title("🔳Sierpiński Carpet Fractal Explorer")
    st.write("A square-based fractal formed by chaotic jumps toward an 8-point grid, avoiding the center.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        points = st.slider("No of points", 5000, 10000, 6000, step=500)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#653DAA")
        with s_col2:
            end_color = st.color_picker("Ending color", "#EA81E3")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        thickness = st.slider("Dot size ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames = gen_chaocarp(points, st_bgr, end_bgr, bg_bgr, thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        final_image = frames[-1]

        _, buffer = cv2.imencode('.png', final_image)
        img_bytes = BytesIO(buffer)

        gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
        gif_bytes = BytesIO()

        imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
        gif_bytes.seek(0)
        img_bytes.seek(0)
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="sierpinski_carpet.png",
                               mime="image/png")
        with c2:
            st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="sierpinski_carpet.gif",
                               mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🧩 The **Chaos Sierpiński Carpet** looks like a woven grid of holes — but it’s made by *jumping randomly*, not cutting out squares!\n\n"
            "Here’s how it works:\n\n"
            "1️⃣ Start with 8 points around a square grid (like corners and centers of edges).\n\n"
            "2️⃣ Pick any point to start with — say, the center of the canvas.\n\n"
            "3️⃣ Randomly pick one of the 8 attractor points (avoiding the center).\n\n"
            "4️⃣ Move **halfway** toward that point.\n\n"
            "5️⃣ Plot it, then repeat this process many times.\n\n"
            "🌀 Over time, points *avoid the center* and fill the space with a self-similar carpet pattern.\n\n"
            "📌 This is again a **chaotic fractal** — the pattern emerges purely from position-based rules with no drawing of squares.\n\n"
            "✨ The result? A mesmerizing digital doormat made by randomness!"
        )

#--------------------------------------------------------------------
elif st.session_state.clicked == 'EF':
    st.title("🌸 Frost Bloom Fractal Explorer")
    st.write("A chaos fractal born from a hexagon, blooming like frozen petals through random symmetry.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        points = st.slider("No of points", 5000, 10000, 6000, step=500)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#94DDDE")
        with s_col2:
            end_color = st.color_picker("Ending color", "#179BE2")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        thickness = st.slider("Dot size ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames = gen_frost(points, st_bgr, end_bgr, bg_bgr, thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        final_image = frames[-1]

        _, buffer = cv2.imencode('.png', final_image)
        img_bytes = BytesIO(buffer)

        gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
        gif_bytes = BytesIO()

        imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
        gif_bytes.seek(0)
        img_bytes.seek(0)
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Hexabloom.png",
                               mime="image/png")
        with c2:
            st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Hexabloom.gif",
                               mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🌸 The **Hexaflake** fractal is a snowflake-like beauty born from a hexagon and pure randomness!\n\n"
            "Here’s how it works:\n\n"
            "1️⃣ Take 6 attractor points — the **corners of a regular hexagon**.\n\n"
            "2️⃣ Start from the center of the canvas.\n\n"
            "3️⃣ Randomly choose one of the 6 corners.\n\n"
            "4️⃣ Move **2/3 of the way** toward that corner.\n\n"
            "5️⃣ Plot the point, and repeat this process thousands of times.\n\n"
            "❄️ Over time, a **hexagonal snowflake-like pattern** appears — no cutting, no recursion, just geometric jumping!\n\n"
            "📌 This is a **chaotic fractal**, meaning it's created by simple random rules — not by removing shapes like in classic fractals.\n\n"
            "🧠 The Hexaflake blends perfect symmetry with random movement to form a stunning, frozen explosion of self-similarity."
        )


#----------------------------------------------------
elif st.session_state.clicked=='FG':
    st.title("🦋 Hexawing Fractal Explorer")
    st.write("A hexagon-based chaos fractal with mirrored, wing-like symmetry emerging from controlled randomness.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        points = st.slider("No of points", 5000, 10000, 6000, step=500)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#E89C06")
        with s_col2:
            end_color = st.color_picker("Ending color", "#1906E8")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        thickness = st.slider("Dot size ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames = gen_hexwing(points, st_bgr, end_bgr, bg_bgr, thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        final_image = frames[-1]

        _, buffer = cv2.imencode('.png', final_image)
        img_bytes = BytesIO(buffer)

        gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
        gif_bytes = BytesIO()

        imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
        gif_bytes.seek(0)
        img_bytes.seek(0)
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Hexawing.png",
                               mime="image/png")
        with c2:
            st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Hexawing.gif",
                               mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🦋 The **HexaWing Fractal** is a stunning pattern born from a *hexagon and a bit of chaos* — a butterfly made of math!\n\n"
            "Here’s how it works:\n\n"
            "1️⃣ Start with 6 attractor points — the **vertices of a hexagon**.\n\n"
            "2️⃣ Begin from the center of the canvas.\n\n"
            "3️⃣ Randomly pick one of the 6 points.\n\n"
            "4️⃣ Move toward it using a custom rule:\n\n"
            "• If it's a **side vertex**, move 2/3 of the way.  \n"
            "• If it's a **corner or tip**, move 5/6 of the way.\n\n"
            "5️⃣ Plot the point, then repeat this process thousands of times.\n\n"
            "🌟 The result? A symmetrical, wing-like fractal structure — *as if a butterfly emerged from controlled randomness*.\n\n"
            "📌 This is a **chaos fractal**, meaning there’s no cutting or recursion — just points dancing toward symmetry.\n\n"
            "🧠 HexaWing beautifully blends **hexagonal geometry** with a *custom movement rule*, creating a fractal with both order and flow."
        )


#-------------------------------------------------------------------------
elif st.session_state.clicked == 'GH':
    st.title("❄️ Hexaflake Fractal Explorer")
    st.write("A frozen fractal forged in randomness, shaped by hexagonal harmony.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        points = st.slider("No of points", 5000, 10000, 6000, step=500)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#E8D606")
        with s_col2:
            end_color = st.color_picker("Ending color", "#E80606")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        thickness = st.slider("Dot size ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames = gen_hexflake(points, st_bgr, end_bgr, bg_bgr, thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        final_image = frames[-1]

        _, buffer = cv2.imencode('.png', final_image)
        img_bytes = BytesIO(buffer)

        gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
        gif_bytes = BytesIO()

        imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
        gif_bytes.seek(0)
        img_bytes.seek(0)
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Hexaflake.png",
                               mime="image/png")
        with c2:
            st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Hexaflake.gif",
                               mime="image/gif")

    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "⬡ **Hexaflake Chaos Game (Skip Rule)**\n\n"
            "This version of the Hexaflake is generated using a randomized rule where each point hops **halfway toward a non-adjacent vertex** of a hexagon.\n\n"
            "🎲 Unlike traditional deterministic fractals that cut out parts recursively, this one is built entirely by **controlled chaos** — simple rules repeated thousands of times.\n\n"
            "🔁 At every step:  \n\n"
            "• A point is chosen randomly among the six corners of a large hexagon.   \n"
            "• The point moves halfway toward that vertex — but it must **skip adjacent ones** to avoid clumping.   \n"
            "• Over time, this generates a beautifully symmetrical, snowflake-like pattern.\n\n"
            "✨ The result is a **fractal bloom of order from randomness**, resembling a frozen, star-like structure — a balance of geometry and unpredictability.\n\n"
            "🧠 This fractal is an elegant example of how **emergent patterns** arise from very simple iterative rules."
        )

#----------------------------------------------------------------------------
elif st.session_state.clicked=='HI':
    st.title("💮 Petal Burst Fractal Explorer")
    st.write("🌸 A radiant fractal where petals bloom and burst from chaos with perfect symmetry.")
    col1, col2 = st.columns(2)
    with col1:
        points = st.slider("No of points", 5000, 10000, 6000, step=500)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#E806BD")
        with s_col2:
            end_color = st.color_picker("Ending color", "#DCA9E2")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        scol1,scol2=st.columns(2)
        with scol1:
            frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        with scol2:
            petal=st.slider("No of Petals ",7,9,8,step=1)
        thickness = st.slider("Dot size ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames = gen_petal(points, st_bgr, end_bgr, bg_bgr, thickness,petal)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        final_image = frames[-1]

        _, buffer = cv2.imencode('.png', final_image)
        img_bytes = BytesIO(buffer)

        gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
        gif_bytes = BytesIO()

        imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
        gif_bytes.seek(0)
        img_bytes.seek(0)
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Bloom.png",
                               mime="image/png")
        with c2:
            st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Bloom.gif",
                               mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🌸 The **PetalBurst** fractal is a floral explosion formed from chaos and symmetry —\n"
            "a dance of points leaping across a polygon, blooming into beautiful radial petals.\n\n"

            "Here’s how it works:\n\n"
            "1️⃣ Begin with a regular polygon (5, 6, 7… sides — your flower’s skeleton).\n\n"
            "2️⃣ Choose a random starting point inside the canvas.\n\n"
            "3️⃣ At each step, jump halfway (or some fraction) toward a **random non-adjacent vertex**.\n"
            "This skipping avoids near neighbors, causing petals to separate and spiral outward.\n\n"
            "4️⃣ Plot the new point. Repeat this thousands of times!\n\n"

            "🌼 With enough iterations, the dots settle into a soft, structured burst —\n"
            "like petals radiating from a floral core. This is the magic of the **chaos game**: \n"
            "simple rules, stunning patterns.\n\n"

            "✨ Unlike classic deterministic fractals, **PetalBurst** uses randomness\n"
            "to carve out symmetry — each render can be slightly different, yet always beautiful.\n\n"

            "🔢 You can control:\n"
            "→ Number of petals (polygon sides)  \n"
            "→ Point skipping logic  \n"
            "→ Color gradient from center to edge  \n"
            "→ Dot size, animation speed, and bloom intensity\n\n"

            "🧠 Though it feels organic, PetalBurst is a deep example of **emergent geometry** —\n"
            "where order grows out of randomness through iteration.\n\n"
            "🌷 Whether you see a daisy, mandala, or starburst, this fractal reminds us:\n"
            "**even chaos can create beauty.**"
        )



#-----------------------------------------------------------------------------
elif st.session_state.clicked == 'D':
    st.title("🔺Sierpiński Triangle Fractal Explorer")
    st.write("A classic fractal made by recursively removing triangles.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        depth = st.slider("depth",1, 10,5)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#FF4200")
        with s_col2:
            end_color = st.color_picker("Ending color", "#FFB200")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        thickness = st.slider("Line Thickness ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames=generate_triangle(depth,st_bgr,end_bgr,bg_bgr,thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        placeholder=st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Sierpiński_Triangle.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Sierpiński_Triangle.gif",
                                   mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🔺 The **Sierpiński Triangle** is made by cutting out smaller triangles from a big one — again and again!\n\n"
            "Here’s how it works:\n\n"
            "1️⃣ Start with a big equilateral triangle.\n\n"
            "2️⃣ Divide it into 4 smaller triangles by connecting the midpoints.\n\n"
            "3️⃣ Remove the middle triangle (the upside-down one).\n\n"
            "4️⃣ Repeat this process on the remaining 3 triangles, then 9, then 27... forever!\n\n"
            "📐 With each step, we remove part of the triangle, leaving behind a **pattern of holes** that forms a beautiful, self-repeating design.\n\n"
            "✨ This is an example of a **deterministic fractal** — no randomness involved, just repeated shrinking and cutting!\n\n"
            "📐 Mathematically:\n\n"
            "→ After 1 step: 3 triangles remain (each half the size)  \n"
            "→ After 2 steps: 3² = 9 triangles  \n"
            "→ After n steps: 3ⁿ triangles remain, each scaled down\n\n"
            "📉 The area at step n is (3/4)ⁿ times the original area, so as n → ∞, the total area → 0.\n"
            "But the number of edges grows endlessly, creating **infinite perimeter**.\n\n"
            "🧠 This fractal has a **Hausdorff Dimension** ≈ 1.585 — between a line (1D) and a surface (2D)."
        )

#-----------------------------------------------------
elif st.session_state.clicked == 'E':
    st.title("🔳Sierpiński Carpet Fractal Explorer")
    st.write("A 2D fractal formed by removing squares from a grid.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        depth = st.slider("depth", 1, 5, 4)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#1F00FF")
        with s_col2:
            end_color = st.color_picker("Ending color", "#00FFFA")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 5)
        thickness = st.slider("Line Thickness ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames=generate_carpet(depth,st_bgr,end_bgr,bg_bgr,thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)

        placeholder=st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Sierpiński_Carpet.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Sierpiński_Carpet.gif",
                                   mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🟩 The **Sierpiński Carpet** is like the triangle, but made from a square instead.\n\n"
            "Here’s how it works:\n\n"
            "1️⃣ Start with a large square.\n\n"
            "2️⃣ Divide it into 9 equal smaller squares (like a tic-tac-toe board).\n\n"
            "3️⃣ Remove the **center square**.\n\n"
            "4️⃣ Repeat this process for the remaining 8 squares.\n\n"
            "🌀 Every time, more tiny squares are removed. As this continues, the shape becomes more complex —\n"
            "but still keeps the same basic pattern!\n\n"
            "✏️ This shows **self-similarity** — every part looks like the whole, just smaller.\n"
            "It’s also a **fractal with zero area but infinite perimeter** when repeated forever!\n\n"
            "📐 After each step, the total area becomes smaller. Mathematically:\n\n"
            "→ After 1st step: 8/9 of the area remains  \n"
            "→ After 2nd step: (8/9)^2 = 64/81  \n"
            "→ After n steps: (8/9)^n area remains\n\n"
            "📉 As n → ∞, the area approaches 0 — even though it looks like something is still there!\n\n"
            "✏️ That’s why it's said to have **zero area**, but the **perimeter becomes infinite**, because the edges get more and more detailed at every step.\n\n"
            "🔁 This is a classic example of a **recursive geometric fractal** with infinite complexity!"
        )


#----------------------------------------------------------------------
elif st.session_state.clicked == 'F':
    st.title("🌳 Tree Fractal Explorer")
    st.write("A recursive fractal where each branch splits into two smaller branches.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        depth = st.slider("Iterations", 1, 12, 9)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#751F0A")
        with s_col2:
            end_color = st.color_picker("Ending color", "#5AF908")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 100, 10)
        turn_angle = st.slider("Turn angle ", 10, 60, 30,step=5)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames=generate_tree(depth,st_bgr,end_bgr,bg_bgr,turn_angle)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)

        placeholder=st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Fractal_tree.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Fractal_tree.gif",
                                   mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🌳 A **Fractal Tree** is made by splitting lines into branches again and again.\n\n"
            "Here's how it grows:\n\n"
            "1️⃣ Start with a vertical line (the trunk).\n\n"
            "2️⃣ From the top, draw two new lines (branches) at angles — usually left and right.\n\n"
            "3️⃣ Make these branches shorter than the trunk.\n\n"
            "4️⃣ Repeat this process from each new branch!\n\n"
            "🔁 This keeps going until the branches get tiny. The result looks like a real tree with endless twigs.\n\n"
            "🌿 This is a type of **recursive fractal** — it mimics how real trees split in nature!\n\n"
            "📐 Geometrically:\n\n"
            "→ Each branch has a length: L × rⁿ (where r < 1)  \n"
            "→ Number of branches grows exponentially: 2ⁿ branches at level n\n\n"
            "🔁 If total branch length is finite, the tree converges.  \n"
            "But visually, it appears infinitely detailed — like a real tree!\n\n"
            "🧠 This is a **recursive structure** using **rotation matrices** and **scaling transformations** — ideal for modeling nature."
        )



#---------------------------------------------------------------------
elif st.session_state.clicked == 'G':
    st.title("❄️Koch-Snowflake Fractal Explorer")
    st.write("A fractal created by adding triangles to each side, forming a snowflake shape.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        depth = st.slider("Iterations", 1, 6, 4)
        s_col1, s_col2 = st.columns(2)
        with s_col1:
            st_color = st.color_picker("Flake color", "#1F00FF")
        with s_col2:
            bg_color = st.color_picker("Background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 100, 200, 110)
        thickness = st.slider("Line Thickness ", 1, 5, 1)
    st_bgr = hex_to_bgr(st_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames=generate_flake(depth,st_bgr,bg_bgr,thickness)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        placeholder=st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Snowflake.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Snowflake.gif",
                                   mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "❄️ The **Koch Snowflake** starts with a simple triangle and builds spikes to form a snowflake shape.\n\n"
            "Steps:\n\n"
            "1️⃣ Start with an equilateral triangle.\n\n"
            "2️⃣ Divide each side into 3 equal parts.\n\n"
            "3️⃣ Replace the middle part with a triangle bump pointing outward (making a star-like shape).\n\n"
            "4️⃣ Repeat this on every side — again and again!\n\n"
            "📐 With each step, the shape becomes spikier and more detailed.\n"
            "🌟 Even though the area stays limited, the perimeter becomes **infinitely long**!\n\n"
            "🧠 This is a classic example of a **recursive fractal** — built by repeating a shape transformation.\n\n"
            "📐 After each step:\n\n"
            "→ Number of sides: 3 × 4ⁿ  \n"
            "→ Length of each side: (1/3)ⁿ of original  \n"
            "→ Total perimeter = initial × (4/3)ⁿ → becomes infinite!\n\n"
            "📏 But area converges! Total area approaches:  \n"
            "Area = (8/5) × (area of original triangle)\n\n"
            "🧠 It's a **mathematical paradox** — **infinite edge length** inside a **bounded shape**!"
        )

#--------------------------------------------
elif st.session_state.clicked == 'H':
    st.title("🐉 Dragon Curve Fractal Explorer")
    st.write(
        "Explore the recursive dragon curve fractal with custom depth and rotation angles. Adjust parameters and download your creation!")

    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        depth = st.slider("Iterations", 10, 20, 15)
        s_col1, s_col2= st.columns(2)
        with s_col1:
            st_color = st.color_picker("Starting color", "#751F0A")
        with s_col2:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 100, 1000, 200)
        turn_angle = st.slider("Turn angle ", 60, 130, 110, step=5)
    st_bgr = hex_to_bgr(st_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames=generate_dragon(depth, st_bgr, bg_bgr,1, turn_angle)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        placeholder = st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Dragon_curve.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Dragon_curve.gif",
                                   mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "🐉 The **Dragon Curve** is a line that keeps folding in a clever way to make a sharp, twisty pattern.\n\n"
            "Here’s the idea:  \n\n"
            "1️⃣ Start with a straight line.\n\n"
            "2️⃣ Fold it in the middle — like folding a paper.\n\n"
            "3️⃣ Unfold it so there’s a right angle.\n\n"
            "4️⃣ Repeat folding and unfolding, always keeping the previous folds, adding new ones at a right angle.    \n\n"
            "📐 Each fold adds more corners and twists.    \n"
            "🌀 After many steps, the line forms a **dragon-like curve** with a complex, beautiful structure.   \n\n"
            "This fractal shows how **repeated turns and reflections** can make patterns without drawing — just folding!\n\n"
            "📐 The total length stays constant, but the path becomes more twisted.\n\n"
            "→ The curve never crosses itself.  \n"
            "→ After n steps, it has 2ⁿ segments and 2ⁿ⁻¹ right-angle turns.\n\n"
            "🌀 The curve folds into tighter and tighter spaces, and eventually **fills part of the 2D plane**.\n\n"
            "🧠 It’s defined by a sequence of left/right turns generated using **binary rules**, and it’s an example of a **self-similar, non-overlapping fractal**."
        )

#---------------------------------------------------------------------------
elif st.session_state.clicked=='I':
    st.title("〰️Cantor Set Fractal Set")
    st.write("A 1D fractal formed by repeatedly removing the middle third of a segment.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        depth = st.slider("Iterations", 1, 6, 4)
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            st_color = st.color_picker("Starting color", "#420A75")
        with s_col2:
            end_color = st.color_picker("Ending color", "#F908B9")
        with s_col3:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 100, 1000, 500)
    st_bgr = hex_to_bgr(st_color)
    end_bgr = hex_to_bgr(end_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames=generator_cantor(depth,st_bgr,end_bgr,bg_bgr)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        placeholder=st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Cantor.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Cantor.gif",
                                   mime="image/gif")

    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "➖ The **Cantor Set** starts as a simple line — but hides infinite complexity through removal.\n\n"
            "Here’s the idea:  \n\n"
            "1️⃣ Start with a straight line segment (like from 0 to 1).\n\n"
            "2️⃣ Divide it into 3 equal parts.\n\n"
            "3️⃣ Remove the middle third — poof! it’s gone.\n\n"
            "4️⃣ Now repeat the same for each remaining segment.\n\n"
            "➗ At every step, each line becomes 2 shorter pieces — the middle is always removed.\n\n"
            "📉 After **n steps**, you have `2ⁿ` segments.\n"
            "📏 Each segment has length `(1/3)ⁿ`.\n"
            "➕ Total remaining length = `(2/3)ⁿ`, which shrinks fast.\n\n"
            "🔁 Even though the total length → 0, the number of points → ∞!\n"
            "🧠 That’s right: it’s an **uncountably infinite set** with no actual length.\n\n"
            "📐 The fractal dimension is:  \n"
            "`D = log(2) / log(3) ≈ 0.6309`\n"
            "— meaning it’s more than a bunch of points, but not quite a line.\n\n"
            "💡 The Cantor Set is a perfect example of how **simple rules + recursion = infinite depth**."
        )

#------------------------------------------------------------------------------
elif st.session_state.clicked == 'J':
    st.title("🐞 Mandelbrot Set Fractal Explorer")
    st.write("🧠 Feed me a complex number — I’ll show you how it runs or spirals into chaos.")
    st.subheader("🎛️ Controls Section")

    col1, col2 = st.columns(2)
    with col1:
        option = st.radio("Grid", ('On', 'Off'))
        st.write("This fractal is working in Complex plane")
    with col2:
        x = st.slider("Real part (X)", -2.0, 1.0, -0.75, step=0.01)
        y = st.slider("Imaginary part (Y)", -1.5, 1.5, 0.1, step=0.01)

    o = 1 if option == "On" else 0

    frame = generate_mandelbrot(x, y, o)

    img_placeholder = st.empty()
    img_placeholder.image(frame, channels="BGR")

    final_image = frame
    _, buffer = cv2.imencode('.png', final_image)
    img_bytes = BytesIO(buffer.tobytes())
    img_bytes.seek(0)

    c1, c2 = st.columns(2)
    with c1:
        st.download_button("📥 Download Final Image (PNG)", data=img_bytes,
                           file_name="Mandelbrot.png", mime="image/png")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "➕ The **Mandelbrot Set** is built from a simple rule — yet it creates infinite, chaotic beauty.\n\n"
            " 🔁 The Rule:\n\n"
            "`zₙ₊₁ = zₙ² + c`\n\n"
            "Start with `z₀ = 0`, and apply this rule over and over for a complex number `c = x + i·y`.\n\n"
            "📌 Each pixel you see corresponds to a different `c` value.\n\n"
            "🔍 If `z` stays bounded (doesn’t shoot off to infinity), we say that point belongs to the Mandelbrot Set.\n\n"
            " 💣 Escape Condition:\n\n"
            "`|z| > 2` → The point has escaped (it’s outside the set).\n\n"
            " 🎨 What You See:\n\n"
            "- **Black or dark points** → likely inside the set (orbit stays bounded)\n\n"
            "- **Colorful regions** → points where `z` escapes after several steps\n\n"
            "- The number of steps before escape decides the pixel’s color\n\n"
            "🌀 You’re looking at an **orbit** — how `z` evolves as we keep applying `z = z² + c`.\n\n"
            "🧠 The edge of the Mandelbrot Set is incredibly complex — full of spirals, bulbs, and self-similar patterns.\n\n"
            "🔗 It’s a true fractal: infinite detail, no matter how far you zoom in."
        )

#---------------------------------------------------------------------
elif st.session_state.clicked=='K':
    st.title("🔮Julia Set Fractal Explorer")
    st.subheader("🎛️ Controls Section")
    col1,col2=st.columns(2)
    with col1:
        comp=st.selectbox("Select complex number:",["-0.7 + 0.27015j","-0.8 + 0.156j","0.285 + 0.01j","0.355 + 0.355j","-0.4 + 0.6j","-0.7269 + 0.1889j","-0.70176 - 0.3842j"])
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 1, 10, 1)
    if comp=="-0.7 + 0.27015j":
        r,i=-0.7,0.27015
    elif comp=="-0.8 + 0.156j":
        r,i=-0.8,0.156
    elif comp=="0.285 + 0.01j":
        r,i=0.285,0.01
    elif comp=="0.355 + 0.355j":
        r,i=0.355,0.355
    elif comp=="-0.4 + 0.6j":
        r,i=-0.4,0.6
    elif comp=="-0.7269 + 0.1889j":
        r,i=-0.7269,0.1889
    else :
        r,i=-0.70176,-0.3842



    if st.button("Generate"):
        frames = generate_julia(r,i)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        placeholder = st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Julia.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Julia.gif",
                                   mime="image/gif")

    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "➕ The **Julia Set** is built using the same rule as Mandelbrot — but with a twist.\n\n"
            " 🔁 The Rule:\n\n"
            "`zₙ₊₁ = zₙ² + c`\n\n"
            "We start with **different `z` values for each pixel**, but `c` is a **fixed complex number**.\n\n"
            "📌 Every pixel becomes a starting point `z₀ = x + i·y`, and we check how it evolves using that fixed `c`.\n\n"
            "🔗 Unlike Mandelbrot (which explores all possible `c`), the Julia Set shows **how one specific `c` behaves everywhere**.\n\n"
            " 💣 Escape Condition:\n\n"
            "`|z| > 2` → The point escapes (not part of the set).\n\n"
            " 🎨 What You See:\n\n"
            "- **Black or dark regions** → points whose orbit stays bounded (they’re in the set)\n\n"
            "- **Colorful swirls** → points that escape after several iterations\n\n"
            "- More iterations before escape = deeper color\n\n"
            "🧿 Each `c` value gives a **unique Julia Set** — some are connected, others are shattered like dust.\n\n"
            "🧠 The shapes can be spirals, stars, eyes, lightning bolts, or mysterious clouds — all from math.\n\n"
            "♾️ Julia Sets are fractals too — infinite detail, self-similarity, and symmetry across scales.\n\n"
            "✨ You’re not just seeing a shape — you’re seeing the **behavior of complex numbers come to life.**"
        )
#----------------------------------------------------------------------------------
if st.session_state.clicked=='L':
    st.title("Hilbert Curve Fractal Set")
    st.write("A 1D fractal formed by repeatedly removing the middle third of a segment.")
    st.subheader("🎛️ Controls Section")
    col1, col2 = st.columns(2)
    with col1:
        depth = st.slider("Iterations", 1, 6, 4)
        s_col1, s_col2 = st.columns(2)
        with s_col1:
            st_color = st.color_picker("Starting color", "#06C5F3")
        with s_col2:
            bg_color = st.color_picker("background color", "#000000")
    with col2:
        frame_interval = st.slider("Animation speed (ms) ", 100, 1000, 500)
        option = st.radio("Grid", ('On', 'Off'))
        o = True if option == "On" else False
    st_bgr = hex_to_bgr(st_color)
    bg_bgr = hex_to_bgr(bg_color)
    if st.button("Generate"):
        frames = generate_hilbert(depth, st_bgr, bg_bgr, o)
        img_placeholder = st.empty()
        for frame in frames:
            img_placeholder.image(frame, channels="BGR")
            time.sleep(frame_interval / 1000.0)
        placeholder = st.empty()
        with st.spinner("Saving image and preparing downloads..."):
            final_image = frames[-1]

            _, buffer = cv2.imencode('.png', final_image)
            img_bytes = BytesIO(buffer)

            gif_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
            gif_bytes = BytesIO()

            imageio.mimsave(gif_bytes, gif_frames, format='GIF', duration=frame_interval / 1000.0)
            gif_bytes.seek(0)
            img_bytes.seek(0)
        with placeholder:
            c1, c2 = st.columns(2)
            with c1:
                st.download_button("📥 Download Final Image (PNG)", data=img_bytes, file_name="Hilbert.png",
                                   mime="image/png")
            with c2:
                st.download_button("📽️ Download Animation (GIF)", data=gif_bytes, file_name="Hilbert.gif",
                                   mime="image/gif")
    if st.button("🧮 Maths Behind the Fractal"):
        st.info(
            "➕ The **Hilbert Curve** is a fascinating fractal that completely fills space through a clever recursive pattern.\n\n"

            "🔁 The Idea:\n\n"
            "It starts with a simple line that bends into a U-shape.\n\n"
            "At every level, the curve replaces itself with four smaller U-shapes — rotated and flipped to connect continuously.\n\n"

            "📐 The Construction:\n\n"
            "- Divide a square into 4 smaller squares\n\n"
            "- Recursively draw smaller Hilbert curves in each one\n\n"
            "- Flip and rotate them so the path never crosses itself\n\n"

            "🧠 This is called a **space-filling curve** — it winds through every cell of the grid without missing or overlapping.\n\n"

            "🔗 Mathematically, we define the curve using recursion and direction vectors.\n\n"
            "These vectors control how the curve grows, rotates, and folds.\n\n"

            "🌀 What You See:\n\n"
            "- **Smooth, maze-like path** that visits every square\n\n"
            "- As the level increases, the path becomes denser and more complex\n\n"
            "- It fills the space without crossing over itself\n\n"

            "🎨 Every part of the image is touched — making it perfect for applications like:\n\n"
            "- Data storage (space-filling)\n\n"
            "- Image compression\n\n"
            "- Maze generation and signal routing\n\n"

            "♾️ Like all fractals, the Hilbert Curve has **self-similarity** — each part is a smaller version of the whole.\n\n"

            "✨ It’s not just a curve — it’s a deep connection between geometry, recursion, and the infinite."
        )
