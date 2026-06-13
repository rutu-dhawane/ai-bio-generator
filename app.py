import streamlit as st

st.set_page_config(page_title="AI Bio Generator", page_icon="🤖")

st.title("🤖 AI Bio Generator")
st.write("Generate professional bios for different platforms.")

name = st.text_input("Name")
profession = st.text_input("Profession")
skills = st.text_input("Skills (comma separated)")
hobbies = st.text_input("Hobbies")
goal = st.text_input("Career Goal")

platform = st.selectbox(
    "Target Platform",
    ["LinkedIn", "Twitter", "Instagram", "Personal Website"]
)

if st.button("Generate Bio"):

    if name and profession and skills and hobbies and goal:

        if platform == "LinkedIn":
            bio = f"""
{name} is a passionate {profession} with expertise in {skills}. 
Dedicated to continuous learning and innovation, {name} enjoys {hobbies} and is focused on achieving the goal of {goal}. 
Always eager to solve real-world challenges through creativity, technology, and data-driven thinking.
"""

        elif platform == "Twitter":
            bio = f"""
🚀 {profession} | {skills}
📚 Loves {hobbies}
🎯 Goal: {goal}
Building skills and sharing the journey one step at a time.
"""

        elif platform == "Instagram":
            bio = f"""
✨ {profession}
💡 Passionate about {skills}
❤️ {hobbies}
🎯 Dreaming big: {goal}
🌟 Learning, growing, and creating every day.
"""

        else:  # Personal Website
            bio = f"""
Hello! I'm {name}, a {profession} passionate about {skills}.
Beyond my professional interests, I enjoy {hobbies}.
My mission is to {goal} and make a meaningful impact through my work.
Welcome to my personal space where I share my journey, projects, and experiences.
"""

        st.success("Bio Generated Successfully!")
        st.text_area("Generated Bio", bio, height=250)

    else:
        st.warning("Please fill all fields.")