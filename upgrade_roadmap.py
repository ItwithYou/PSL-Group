import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Replace desktop roadmap CSS
pattern = re.compile(r'\.roadmap-path-container\s*{.*?}\s*\/\* The Winding Path \*\/\s*\.roadmap-path-container::before\s*{.*?}\s*\.roadmap-stop\s*{.*?}\s*\/\* Alternate Left and Right Stops \*\/\s*\.roadmap-stop\.left-stop\s*{.*?}\s*\.roadmap-card\s*{.*?}\s*\.roadmap-card:hover\s*{.*?}', re.DOTALL)

new_roadmap_css = """/* ==========================================================================
   Horizontal Roadmap Layout
   ========================================================================== */
.roadmap-path-container {
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12rem 2rem;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
}

/* The Horizontal Line */
.roadmap-path-container::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 2rem;
    right: 2rem;
    height: 2px;
    background: var(--accent-color);
    transform: translateY(-50%);
    z-index: 0;
    width: 0;
    animation: drawLine 1.5s ease-out forwards;
}

@keyframes drawLine {
    to { width: calc(100% - 4rem); }
}

.roadmap-stop {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 320px;
    z-index: 1;
}

/* The Connection Point */
.roadmap-point {
    width: 16px;
    height: 16px;
    background: #ffffff;
    border: 3px solid var(--accent-color);
    border-radius: 50%;
    box-shadow: 0 0 15px rgba(197, 160, 89, 0.6);
    position: relative;
    z-index: 2;
}

[data-theme="dark"] .roadmap-point {
    background: var(--bg-color);
}

/* The Glassmorphism Card */
.roadmap-card {
    position: absolute;
    width: 100%;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid var(--accent-color);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
    opacity: 0;
    animation: fadeInUpCard 0.8s ease forwards;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

[data-theme="dark"] .roadmap-card {
    background: rgba(10, 37, 64, 0.8);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

@keyframes fadeInUpCard {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Staggered Zig-Zag Layout */
.roadmap-stop:nth-child(1) .roadmap-card { bottom: 30px; animation-delay: 0.5s; }
.roadmap-stop:nth-child(2) .roadmap-card { top: 30px; animation-delay: 0.8s; }
.roadmap-stop:nth-child(3) .roadmap-card { bottom: 30px; animation-delay: 1.1s; }

.roadmap-card:hover {
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
}
.roadmap-stop:nth-child(1) .roadmap-card:hover { transform: translateY(-5px); }
.roadmap-stop:nth-child(2) .roadmap-card:hover { transform: translateY(5px); }
.roadmap-stop:nth-child(3) .roadmap-card:hover { transform: translateY(-5px); }"""

css = pattern.sub(new_roadmap_css, css)

# 2. Add Mobile Carousel CSS inside media query
mobile_pattern = re.compile(r'\.roadmap-path-container::before\s*{\s*left:\s*30px;\s*}\s*\.roadmap-point\s*{\s*left:\s*30px;\s*}\s*\.roadmap-stop\s*{\s*flex-direction:\s*column\s*!important;\s*align-items:\s*flex-end;\s*}\s*\.roadmap-card\s*{\s*width:\s*calc\(100%\s*-\s*70px\);\s*}\s*\.roadmap-card::before\s*{\s*display:\s*none;\s*}', re.DOTALL)

mobile_roadmap_css = """    .roadmap-path-container {
        padding: 14rem 2rem;
        overflow-x: auto;
        justify-content: flex-start;
        gap: 2rem;
        scroll-snap-type: x mandatory;
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none;  /* IE and Edge */
    }
    .roadmap-path-container::-webkit-scrollbar {
        display: none; /* Chrome, Safari and Opera */
    }
    .roadmap-path-container::before {
        width: 1000px !important; /* Force line to stretch across scrollable area */
        animation: none; /* Disable animation on mobile swipe */
    }
    .roadmap-stop {
        min-width: 280px;
        scroll-snap-align: center;
    }"""

css = mobile_pattern.sub(mobile_roadmap_css, css)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated style.css with horizontal roadmap")
