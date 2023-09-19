### Notes
- [Source](https://youtu.be/4sosXZsdy-s?si=50lLNNJjgtsBSgLz "video")
- [Bootstrap](https://getbootstrap.com/ "weblink")
- Click on **Docs** to learn more about it
- In Bootstrap 5, you dont need to install JQuery.
- Sass is a CSS preprocessor
- If you want to change default bootstrap settings, you have to download source code, edit the changes and compile it with a saas compiler.

### Quickstart
- step1: create a new index.html
- step2: Include Bootstrap’s CSS and JS.
- step3: Hello, world! Open the page in your browser of choice to see your Bootstrapped page. You may use Live Server extension in VS code.
- step4: Nav Bar
  - ```nav.navbar.navbar-expand-lg```
  - ```nav``` is HTML tag, navbar is the bootstrap class, ```navbar-expand``` is used to make it responsive based on device width, ```lg``` indicates it will expand when it hits large breakpoint as defined in [layout](https://getbootstrap.com/docs/5.3/layout/breakpoints/).
  - ```nav.navbar.navbar-expand-lg.bg-dark.navbar-dark```
  - ```bg-dark``` will make the color dark and ```navbar-dark``` will make the text white
  - add a container to store every ```<a>``` tag of navbar.
  - to seperate ```navbar-brand``` and ```navbar-menu``` write ```ms-auto``` (means: margin start auto) in the ```ul``` tag.
  - to add a hamburger menu, use the class ```navbar-toggler``` in a ```button``` tag.
  - add ```data-bs-toggle``` attribute to ```collapse```and also add a target to toggle ```data-bs-target```
  - to add an icon ```navbar-toggler-icon```
  - to fix navbar on top, just add a class ```fixed-top```
- Step4: Showcase
  - add a section
  - ```pt``` means padding top, ```pb``` padding bottom whose value is 1 (min) to 5 (max). ```px``` means padding in x direction and ```py``` is padding in y direction. ```p-5``` means padding 5 in all direction.
  - to use flexbox we can use ```d-flex``` which means use flex in all sizes. It will convert a row with side by side. to disabe flexbox on a small device we can add size class by ```d-sm-flex```
  - image will breakout of container even with bootstrap, so to bound into the container we will add a class named ``` img-fluid```. ```w-50``` is a size class of width which turns the image 50% of the original width.
  - ```my-4``` is a margin class which will make space 4
  - ```d-none``` will display nothing, ```d-sm-block``` will display anything bigger than small.

- step4: Newsletter section
  - ```mb-3``` means margin bottom 3
  - ```p-lg-0``` means padding on large display 0
  - ```pt-lg-5``` means padding from top is 5
  - example to make it responsive using custom css file as below
  ```css
  @media(min-width: 768px){
    .news-input{
      width:50%;
    }
  }
  ```
- Boxes
  - to use the grid first use ```.row``` which houses the columns.
  - ```col-md``` indicates column will trigger for at least medium or more size, otherwise those will stack.
  - bootstrap icon cdn
  - ```g-4``` means gutter 4 in all direction
- Question Accordion
- Instructors