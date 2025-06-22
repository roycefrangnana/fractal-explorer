import streamlit as st
import base64

def get_base64_gif(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
def Home():
    st.title("Code, Chaos & Curves")
    st.caption("✨ Dive into the beauty of infinite patterns and the minds behind them.")
    st.divider()
    st.header("🌟 Welcome to Fractal Minds Where Math Turns into Art")
    st.write("""🔍 Explore iconic fractals like the Mandelbrot Set, Sierpiński Triangle, and Barnsley Fern.  
🧠 Discover the brilliant mathematicians who brought these concepts to life.  
🎨 Animate, interact, and even generate your own mesmerizing fractal artworks!""")
    st.subheader("💡 Curious Minds Section")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌀 What is a Fractal?"):
            st.info("A fractal is a never-ending pattern that repeats at different scales. It’s created by repeating a simple process over and over in an ongoing feedback loop. Fractals appear complex but are built from simple rules.")
        if st.button("🧮 Are Fractals Only Math?"):
            st.info("Not at all! Fractals are found in nature too — like trees, rivers, lightning, and even broccoli. Their repeating patterns make them both mathematically fascinating and naturally beautiful.")
        if st.button("🌿 Where is it in nature?"):
            st.info("Fractals are everywhere in nature — in trees, lightning, snowflakes, coastlines, clouds, and even blood vessels!")

    with col2:
        if st.button("🔍 Why Fractals Matter"):
            st.info("Fractals help us model complex systems in nature like clouds, trees, coastlines, and blood vessels. They're used in computer graphics, medicine, finance, and more!")
        if st.button("📐 What's Self-Similarity?"):
            st.info("Self-similarity means a shape looks similar at different scales. Zoom into a small section of a fractal, and you'll often see a mini version of the whole!")
        if st.button("🧩 Simplest fractal?"):
            st.info("The *Cantor Set* is one of the simplest fractals — just repeatedly remove the middle third of a line segment.")

    with col3:
        if st.button("🌍 Real-Life Applications"):
            st.info("Fractals are used in antenna design, image compression, nature simulations in movies, modeling population growth, and even diagnosing diseases with medical imaging.")
        if st.button("🧠 Fractals & Science?"):
            st.info("Fractals help model complex systems like weather patterns, galaxy formations, and even financial markets. They reveal hidden order in apparent chaos!")
        if st.button("🗣️ Who coined 'fractal'?"):
            st.info("The term 'fractal' was coined by Benoît B. Mandelbrot in 1975, from the Latin *fractus*, meaning broken or fractured.")
    st.markdown("🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽🔹◽")
    st.subheader("📚 Dive Deeper: Fractal Glossary")
    if st.button("📖 Open Glossary"):
        st.info(
            "🔁 **Recursion:** A process where the output feeds back as input, often seen in fractal generation.\n\n"
            "📏 **Self-Similarity:** A pattern that looks similar at different levels of zoom — like zooming into a coastline or fern.\n\n"
            "🔀 **IFS (Iterated Function System):** A technique using repeated transformations (like scaling, rotation, shifting) to create complex fractal shapes.\n\n"
            "🎲 **Chaos:** The appearance of randomness arising from very sensitive but deterministic rules — small changes can lead to wildly different outcomes.\n\n"
            "📐 **Affine Transformation:** A type of mathematical transformation that moves and reshapes objects through rotation, scaling, translation, or shearing.\n\n"
            "🌱 **Fractal Dimension:** A way to measure complexity — it's not a whole number! For example, a line is 1D, a square is 2D, but a fractal can be 1.58D!\n\n"
            "🔍 **Zoom Symmetry:** The idea that zooming in reveals more patterns similar to the original — an infinite loop of structure.\n\n"
            "🌐 **Complex Plane:** A 2D plane where each point represents a complex number — used heavily in fractal generation."
        )

    st.subheader("""🌀 Fractals whisper a truth:
    Complexity emerges not from chaos, but from simple rules repeated with patience.
    ✨ Dare to find your simple rule — and don’t fear the complexity it may create.
    🌱 That’s how life unfolds.""")
    st.caption("🔎 Zoom into the Chaos: Explore the Fractal World")

def Minds_Page():
    tabs = st.tabs([
        "Benoît B. Mandelbrot",
    "Michael Barnsley",
    "Wacław Sierpiński",
    "Helge von Koch",
    "Gaston Julia",
    "David Hilbert",
    "Felix Hausdorff",
    "Georg Cantor"
    ])

    with tabs[0]:
        st.header("Benoît B. Mandelbrot")
        st.write("💫 Father of fractals who revealed the hidden complexity of nature.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Mandelbrot.jpeg", width=300, caption="Benoît B. Mandelbrot")
        st.write("""Benoît B. Mandelbrot (1924–2010) was a Polish-born French-American mathematician best known for discovering the Mandelbrot Set and pioneering the field of fractal geometry. He proposed that many natural phenomena — like coastlines, mountain ranges, clouds, and even galaxies — could be better understood using patterns that repeat at different scales. These “fractals,” as he called them, broke from the smooth, idealized geometry of Euclid and introduced roughness as a new mathematical frontier.
\n\nWorking at IBM in the 1960s and 70s, Mandelbrot had access to cutting-edge computers, which helped visualize the complex shapes generated by fractal equations. His 1982 book *The Fractal Geometry of Nature* revolutionized how scientists, artists, and engineers view the world, showing that chaos has structure and that beauty lies in complexity.""")
        st.subheader("🧠 Did You Know?")
        st.info("Mandelbrot's last name actually comes from a type of almond cookie! His family name reflects the blend of culture and creativity that defined his mathematical thinking.")


    with tabs[1]:
        st.header("Michael Barnsley")
        st.write("💫 Pioneer of iterated function systems and the Barnsley Fern.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Barnsley.jpeg", width=300, caption="Michael Barnsley")
        st.write("""Michael Barnsley (b. 1946) is an Australian mathematician who introduced a powerful technique known as Iterated Function Systems (IFS) to model the recursive beauty of natural objects. His most famous creation, the Barnsley Fern, elegantly reproduces the structure of a real fern using only a few mathematical transformations applied repeatedly. It remains one of the most iconic examples of fractal modeling in nature.

Barnsley's work bridges mathematics, computer science, and art. He has written several influential books, including *Fractals Everywhere*, which introduces the deep mathematics behind seemingly simple patterns. His research has impacted areas such as image compression, chaos theory, and natural modeling.""")
        st.subheader("🧠 Did You Know?")
        st.info("The Barnsley Fern was so realistic that people didn’t believe it was purely mathematical — it’s generated by just four simple transformations!")

    with tabs[2]:
        st.header("Wacław Sierpiński")
        st.write("💫 Master of recursive beauty—creator of the Sierpiński triangle and carpet.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Sierpinski.jpeg", width=300, caption="Wacław Sierpiński")
        st.write("""Wacław Sierpiński (1882–1969) was a pioneering Polish mathematician whose work spanned number theory, set theory, and topology. He is best known for inventing the Sierpiński Triangle, a fractal created by recursively removing smaller triangles from a larger one. He also developed the Sierpiński Carpet and Sierpiński Curve, each demonstrating self-similarity and recursive structure.

Sierpiński authored over 700 papers and 50 books. His exploration of infinity and mathematical structures continues to inspire recursion-based learning and advanced mathematical research.""")
        st.subheader("🧠 Did You Know?")
        st.info("Sierpiński has a *planet* named after him! Asteroid 16010 Sierpiński honors his legacy in space as well as on paper.")


    with tabs[3]:
        st.header("Helge von Koch")
        st.write("💫 Introduced the world to infinite perimeter through the Koch Snowflake.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Koch.png", width=300, caption="Helge von Koch")
        st.write("""Helge von Koch (1870–1924) was a Swedish mathematician who introduced one of the earliest known fractals: the Koch Snowflake. Described in 1904, it is formed by repeatedly adding smaller equilateral triangles to the sides of an initial triangle. Despite its simplicity, the curve has infinite length yet encloses a finite area — a shocking idea that challenged the boundaries of classical geometry.

The Koch curve laid the groundwork for later fractals by demonstrating how simple rules could produce infinite complexity. Though von Koch published few papers, the impact of his snowflake was enormous.""")
        st.subheader("🧠 Did You Know?")
        st.info("The Koch Snowflake has an infinite perimeter but encloses a finite area — it can theoretically hold rainwater forever!")


    with tabs[4]:
        st.header("Gaston Julia")
        st.write("💫 Explored the depths of complex dynamics in the Julia set.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Julia.jpeg", width=300, caption="Gaston Julia")
        st.write("""Gaston Julia (1893–1978) was a French mathematician whose early work on complex numbers and iteration laid the foundation for what are now called Julia Sets — stunning fractals that reveal intricate structures under infinite zoom. His research, conducted during World War I despite severe injuries, gained global recognition.

Julia studied how repeating functions in the complex plane led to boundary regions of extreme sensitivity — what would later be formalized as chaos. Julia Sets are now central to fractal art and chaos theory.""")
        st.subheader("🧠 Did You Know?")
        st.info("Julia submitted his groundbreaking paper at just 25 years old — while recovering from serious war injuries that required over 30 facial surgeries.")

    with tabs[5]:
        st.header("David Hilbert")
        st.write("💫 Bridged geometry and recursion with the elegant Hilbert Curve.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Hilbert.jpeg", width=300, caption="David Hilbert")
        st.write("""David Hilbert (1862–1943) was a German mathematician whose contributions influenced nearly every area of modern mathematics. Among his many achievements is the Hilbert Curve — a space-filling fractal that visits every point in a grid without intersecting itself.

Originally theoretical, this curve is now applied in data storage, image processing, and spatial indexing. Hilbert's vision extended beyond geometry: his 23 famous unsolved problems, posed in 1900, guided the mathematical developments of the 20th century.""")
        st.subheader("🧠 Did You Know?")
        st.info("Hilbert once famously said, 'We must know, we will know!' — a defiant motto that embodies the spirit of mathematical discovery.")

    with tabs[6]:
        st.header("Felix Hausdorff")
        st.write("💫 Father of fractional dimensions — made measuring fractals possible.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Felix.png", width=300, caption="Felix Hausdorff")
        st.write("""Felix Hausdorff (1868–1942) was a German mathematician who laid the foundation for **dimension theory**, introducing what we now call the *Hausdorff Dimension*. This concept allows us to measure fractals that don’t fall into traditional dimensions — like a coastline that’s more than a line but less than a plane.\n
His work in set theory, topology, and functional analysis helped build the rigorous mathematical framework needed to describe complex, irregular shapes. Without Hausdorff's ideas, Mandelbrot’s vision of fractals wouldn't have had the mathematical support it needed to take off.""")
        st.subheader("🧠 Did You Know?")
        st.info(
            "Hausdorff originally published poetry and philosophical works under a pseudonym before fully turning to mathematics.")

    with tabs[7]:
        st.header("Georg Cantor")
        st.write("💫 Explorer of infinity — creator of the Cantor Set, an early fractal.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("images/Cantor.jpeg", width=300, caption="Georg Cantor")
        st.write("""Georg Cantor (1845–1918) was a German mathematician best known for developing **set theory** and introducing the concept of different sizes of infinity. He created the *Cantor Set*, a deceptively simple yet profoundly important fractal made by repeatedly removing the middle third of a line segment.
\nCantor’s work with infinite sets and recursion formed the philosophical and mathematical roots of fractal thinking. His ideas were controversial during his time but later became foundational to modern mathematics.""")
        st.subheader("🧠 Did You Know?")
        st.info(
            "Cantor’s work was so radical that many of his peers rejected it — even calling him 'insane'. Today, he’s celebrated as a visionary of modern math.")


def Nature_Page():
    st.title("⛰️ Nature’s Secret Code: Fractals")
    st.markdown("### Where Chaos Meets Pattern, and Math Dances with It.")

    st.markdown("""
    Imagine zooming into a leaf...  
    Then zooming into a branch...  
    And then a root...  
    What if everything... looks kinda the same? 👀  
    That's the magic of **fractals in nature**.
    """)
    st.subheader("🧠 Why Does Nature Use Fractals?")
    st.markdown("""
    Fractals aren’t random — they’re **nature’s blueprint** for survival and beauty.

    🔁 **Repetition** = Less effort, more structure  
    🌀 **Self-similarity** = Smart design at every level  
    💨 **Efficient systems** = Fast flow of water, air, and even data (yes, even in tech!)

    So from lungs to lightning, mountains to mushrooms...  
    Fractals are the **silent engineers** of the world.
    """)
    st.subheader("Unspoken Symmetry: The Language of Nature 🪐")
    st.markdown("_Fractals aren’t just patterns — they’re nature’s way of being brilliant._")

    with st.expander("🌌 Fractals go beyond Earth?"):
        st.success("""
        🌠 Galaxy clusters, nebulae, and even dark matter follow **fractal-like distributions**.  
        The **cosmic web** — a vast network of galaxies — shows self-similarity across astronomical scales.

        > The **universe itself** might just be a giant fractal!
        """)

    with st.expander("🧬 DNA uses fractals to fold efficiently?"):
        st.success("""
        Every cell in your body holds **2 meters of DNA**, folded inside a tiny nucleus.  
        How? Through **fractal folding** — a super-efficient way to pack information.

        🧬 DNA uses a model called the **fractal globule** to:
        - Avoid knots  
        - Fold and unfold easily  
        - Maximize space and speed

        > Nature literally folds your **blueprint** with fractal intelligence.
        """)

    with st.expander("🌩️ Lightning strikes in fractals?"):
        st.success("""
        ⚡ Lightning forks through the sky like a branching river.  
        Each bolt follows chaotic but **fractal branching**, modeled by algorithms like **L-systems**.

        > Even storms obey geometry — wild, beautiful geometry.
        """)

    with st.expander("🥦 Romanesco broccoli is a fractal you can eat?"):
        st.success("""
        🥦 Every spiral of this veggie is a miniature of the whole — a **logarithmic spiral** in the **Fibonacci sequence**.

        Its buds repeat the same shape at different scales. Yes, math is delicious!

        > Romanesco = Fractal you can eat 🌱
        """)

    with st.expander("🌳 Trees grow with fractal rules?"):
        st.success("""
        Trees branch recursively:  
        🌿 Branch ➝ Smaller branch ➝ Twigs ➝ Leaves ➝ Leaf veins.

        This self-similar structure helps:
        - Maximize sunlight ☀️  
        - Distribute water 🌊  
        - Grow efficiently 🌱

        > Trees = Organic **recursive algorithms**.
        """)

    with st.expander("🫁 Your lungs are fractals too?"):
        st.success("""
        🫁 With up to **23 levels of branching**, your lungs spread air to over 300 million alveoli.  
        This gives them the surface area of a **tennis court** — in your chest!

        > Breathing is made possible by **fractal biology**.
        """)

    with st.expander("🧠 Your brain is wired with fractals?"):
        st.success("""
        Your neurons branch like trees 🌳, connecting in patterns that **mirror themselves**.

        Even brain waves show **fractal rhythms** — thoughts happen in a self-similar dance.

        > The brain may think in fractals 🧠
        """)

    with st.expander("🌊 River systems follow fractal laws?"):
        st.success("""
        River tributaries branch recursively just like trees.

        🌊 They obey **Horton’s laws**, a kind of **natural fractal mathematics** that governs how water flows across Earth.

        > Rivers are nature’s water circuits — fractal and flowing.
        """)
    with st.expander("🦷 Your teeth & bones have fractal structure?"):
        st.success("""
        🦴 The internal structure of your **bones and teeth** shows self-similar, branching cavities.  
        This **trabecular pattern** (spongy inner bone) distributes stress and pressure efficiently.

        > Nature engineers **strength with recursion** — even in your jaw!
        """)

    with st.expander("🐚 Fractals in shells and spirals?"):
        st.success("""
        🐚 Shells like **nautilus** grow in perfect **logarithmic spirals**, a visual example of the **golden ratio**.  
        These spirals allow creatures to expand without changing shape.

        > Beauty meets math — naturally.
        """)

    with st.expander("🕸️ Spider webs use fractal tension?"):
        st.success("""
        🕷️ A spider’s web is a masterpiece of **radial symmetry** and **recursive tension zones**.  
        The web distributes force like a fractal — catching prey **efficiently** and **strongly**.

        > Webs are **living architecture**, optimized with geometry.
        """)

    with st.expander("🧊 Coastlines are infinite in length?"):
        st.success("""
        The more you zoom into a coastline, the more twists and edges you find 🌊  
        — this is called the **Coastline Paradox**, and it’s a perfect example of a **fractal boundary**.

        > The edge of the land... never ends. Just scales.
        """)

    with st.expander("🌿 Ferns are pure fractals?"):
        st.success("""
        🌿 Ferns replicate their shape at every level — frond ➝ leaflet ➝ sub-leaflet.  
        In fact, the famous **Barnsley Fern** fractal is modeled after this plant.

        > Ferns = Fractals in their **final form**.
        """)

    with st.expander("🏔️ Mountains follow rough fractal patterns?"):
        st.success("""
        Mountains might look chaotic — but their ruggedness follows a **fractal dimension**.  
        Elevation maps show **self-similarity** in the contours of hills, ridges, and valleys.

        > Chaos? Nah. Just **rough geometry**.
        """)

    with st.expander("🐾 Animal skin patterns are fractal too?"):
        st.success("""
        🐆 From leopard spots to zebra stripes, nature uses **reaction-diffusion systems** to create patterns that are often **fractal in shape**.

        These systems repeat similar designs across sizes and generations.

        > Evolution speaks the **language of fractals**.
        """)

    with st.expander("🌀 Hurricanes and galaxies share spiral fractals?"):
        st.success("""
        Look at a hurricane. Then look at a galaxy.  
        🌪️🌌 Both spin in a **logarithmic spiral**, governed by similar physics: angular momentum + pressure systems.

        > Fractals connect **weather and space** in one swirling formula.
        """)
    st.markdown("### 🌿 Nature Isn’t Just Pretty — It’s Smart.")

    st.markdown("""
        > _“Look deep into nature, and then you will understand everything better.”_  
        — **Albert Einstein**

        Fractals prove nature isn't random — it's **recursive, brilliant, and poetic**.  
        """)

def gallery():
    st.title("🖼️ Fractal Gallery")
    st.markdown("Explore all the beautiful fractals created using Chaos Game and Geometry-based rules:")
    col1,col2=st.columns(2)
    with col1:

        gif_b64 = get_base64_gif("Gallery/tree.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/Dragon_curve_animation.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/mandel1.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/Julia.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/hilbert_animation.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/barnsley.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.image("Gallery/Hexawing.png", width=300)
        st.image("Gallery/Bloom.png", width=300)
    with col2:
        gif_b64 = get_base64_gif("Gallery/triangle.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/square.webp")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/mandel2.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/Koch.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.write("\n\n")
        gif_b64 = get_base64_gif("Gallery/hilbert.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif_b64}" width="300" height="250">',
            unsafe_allow_html=True
        )
        st.image("Gallery/barley.png",width=300)
        st.image("Gallery/Hexabloom.png", width=300)
        st.image("Gallery/Cantor.png", width=300)