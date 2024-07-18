import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="A-Frame VR Web App")

st.title("A-Frame VR Web App")
st.write("Create and customize VR scenes using A-Frame.")

# Sidebar selections
st.sidebar.title("Options")
choose = st.sidebar.selectbox("Choose a primitive", ["a-box", "a-sphere", "a-cylinder", "a-cone", "a-torus-knot", "a-ring", "a-dodecahedron", "a-icosahedron"])
choose2 = st.sidebar.radio("Choose a light type", ["ambient", "directional", "point", "spot"])
choose3 = st.sidebar.selectbox("Choose an environment preset", ["default", "forest", "contact", "egypt", "goaland"])
choose4 = st.sidebar.selectbox("Add fog?", ["yes", "no"])

fog = '<a-fog type="linear" color="#AAA" near="1" far="20"></a-fog>'

def writeHelp1():
    st.write('<br>')
    st.write('Generated HTML code:')
    st.code('''
<html>
<head>
    <script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>
    <script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>
    <script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script>
</head>
<body>
<a-scene>
''', language="html")

def writeHelp2():
    st.code('''
</a-scene>
</body>
</html>
    ''', language="html")
    st.write('<br>')
    st.write('---')
    st.write('© 2024 Shailendra Singh. All rights reserved.')

if choose == "a-box":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-box position="0 1 -5" rotation="0 45 45" color="red"></a-box>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-box position="0 1 -5" rotation="0 45 45" color="red"></a-box>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()
    
elif choose == "a-sphere":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-sphere position="0 1.25 -5" radius="1.25" color="green"></a-sphere>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-sphere position="0 1.25 -5" radius="1.25" color="green"></a-sphere>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()

elif choose == "a-cylinder":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-cylinder position="0 1 -5" radius="0.5" height="1" color="blue"></a-cylinder>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-cylinder position="0 1 -5" radius="0.5" height="1" color="blue"></a-cylinder>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()

elif choose == "a-cone":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-cone position="0 1 -5" radius-bottom="0.5" height="1" color="purple"></a-cone>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-cone position="0 1 -5" radius-bottom="0.5" height="1" color="purple"></a-cone>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()

elif choose == "a-torus-knot":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-torus-knot position="0 1 -5" radius="0.5" tube="0.2" p="2" q="3" color="orange"></a-torus-knot>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-torus-knot position="0 1 -5" radius="0.5" tube="0.2" p="2" q="3" color="orange"></a-torus-knot>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()

elif choose == "a-ring":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-ring position="0 1 -5" radius-inner="0.5" radius-outer="1" color="yellow"></a-ring>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-ring position="0 1 -5" radius-inner="0.5" radius-outer="1" color="yellow"></a-ring>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()

elif choose == "a-dodecahedron":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-dodecahedron position="0 1 -5" radius="1" color="cyan"></a-dodecahedron>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-dodecahedron position="0 1 -5" radius="1" color="cyan"></a-dodecahedron>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()

elif choose == "a-icosahedron":
    components.html(
        f'<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>'
        f'<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head>'
        f'<body><a-scene><a-icosahedron position="0 1 -5" radius="1" color="magenta"></a-icosahedron>'
        f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>'
        f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>'
        f'{fog if choose4 == "yes" else ""}</a-scene></body></html>', width=600, height=300)
    
    writeHelp1()
    st.write('<a-icosahedron position="0 1 -5" radius="1" color="magenta"></a-icosahedron>')
    st.write(f'<a-light type="{choose2}" color="blue" position="0 5 0"></a-light>')
    st.write(f'<a-entity environment="preset: {choose3}; groundColor: #445; grid: cross"></a-entity>')
    if choose4 == "yes":
        st.write(fog)
    writeHelp2()
