from flask import Flask, render_template_string
import random

app = Flask("__name__")

@app.route("/home")


def home():

    rnum = random.randint(100, 1000)
    content = f"""


<!DOCTYPE html>
<html lang="en">
<head>
    <title>Java Script</title>
    <style>
        .image {{
        height: 300px;
        border: 1px solid black;
        float: right;
    }}
    #google {{
        font-size: 30px;
        background-color: white;
        transition: font-size .5s, background-color .5s;
    }}
    #google:hover {{
        font-size: 40px;
        background-color: rgb(224, 245, 238);
    }}


    </style>
        
    <script>
        function check() {{
    if(confirm("Are you sure?")){{
        alert("Ayt bet!")
        img = document.querySelector("img");
        img.remove();
}}else{{
    alert("oh okay cool")
}}
}}
    </script>
</head>
<body>
    <h1>
        Welcome to the Front!
    </h1>
    <a href="#bottompage" id="toppage">Take me to the bottom</a>
    
    <br><br>
    <a href="https://google.com" id="google" target="_blank" >Google</a>
    <br><br>
    <a href="#" onclick="check()" > Remove Image</a>

    <img src="https://images.unsplash.com/photo-1499914485622-a88fac536970?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Laptop" class="image">

    <p>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium voluptas quia sit similique! Deserunt esse animi, enim quis ex accusantium fugit recusandae blanditiis delectus in rem doloremque? Labore, eius quasi.


        your number is {rnum}


    </p>


    <a href="#toppage" id="bottompage">back up</a>


    
    <br>&copy; 2025

    
</body>
</html>

"""
    return content
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)





