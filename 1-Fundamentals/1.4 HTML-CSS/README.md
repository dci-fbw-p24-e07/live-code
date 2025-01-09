# Intro to HTML & CSS

- Categories of languages
- Markup languages
- HTML(HyperText Markup Language) Basics
    - Elements
    - Everything is a box
    - Attributes
- CSS (Cascading Stylesheet) Basics
    - Inline CSS
    - Internal CSS
    - External CSS

## Categories

- Markup Languages: 

    - Used to mainly display information. Have no computational properties. 

- Programming Languages: 

    - Have computational properties
    - Mainly used to create algorithms
    - Usually backend languages

- Scripting Languages:

    - Have computational properties
    - Usually don't require compiling
    - Can be run in a linear format

## HTML - HyperText Markup Language

- any file with the `.html` extension
- ALL HTML documents must start with the type declaration: `<!DOCTYPE html>`
- The HTML document begins with `<html>` and ends with `</html>`
- The visible part of the document is declared using `<body>` and `</body>`

### HTML Elements

![HTML Element](1-Fundamentals/example_imgs/fundamentals/1.4/html-element.png)

1. The opening tag: Consists of the name of the element, wrapped in opening and closing angle brackets. The opening tag marks where the element begins or starts to take effect.

2. The content: The content or information to be displayed by the element

3. The closing tag: The same as the opening tag, except that it includes a forward slash  before the element name. This marks where the element ends. 

## CSS - Cascading Stylesheet

1. Inline: Defined in the opening tag of the target element by accessing the style attribute.

2. Internal: Defined in the `<head>` tag using the `<style>` tag with CSS syntax.

3. External: invoked using a `.css` file. Must be linked to the html using the `<link>` tag in the `<head>` tag. You can either use a local file or an online link.

### CSS Classes

- Defined in the `.css` file using a dot before the name of the class.
    > for example `.grey-heading`

- Will be accessible to the html file where it is linked.
- the style properties of CSS classes are only applied to elements where the class name is declared in  the `class` attribute of an HTML element. 
    > for example: `<h1 class="grey-heading">This is a heading</h1>`

### 08/01/2025 - HTML & CSS continuation

- Simple form
- Adding images to HTML
- Standard structure of a website
- Validating form input with JavaScript
- Website vs. Web App

### HTML Forms

- An HTML Form is a webpage section used to collect data from users and send it to the server for further processing.
- HTML Forms are collections of interactive controls and various input types, for example: text, numbers, radio buttons, passwords, email, etc.
- Are created by using the `<form>` tag, all the input-related tags are placed within the `<form>` tag.

```html
<form action="<url>" method="<method_type>">
    <!--- Input tags --->
</form>
```

1. Create - POST
2. Read/Retrieve - GET
3. Update - PUT/PATCH
4. Delete - DELETE

**Common usage of HTML Forms:**

- Authentication: Registration forms and login forms
- Data Collection: Through the use of a contact form or a survey.
- Uploading media: images, files, videos, audio, etc

### Form Validation with JavaScript

- Validation is checking whether the information entered by the user in the correct format and within the constraints set by the application.
- Client-side validation: done in the browser. Before the form is submitted.
- Server-side validation: done at the backend/server.

- If the information is correctly formatted the application allows submitting of data to the server and it is usually saved in a database.
If the information is not correctly formatted the user will get an error message.

1. To use external JavaScript and plugin to the HTML document.

    > Add the the following tag to the bottom of the HTML document. Right before the closing body tag: `<script src="<path-to-JS-file>"></script>`

2. By including JavaScript in the `<script>` tag at the bottom of the HTML document.

    ```html
    <script>
        const email = document.getElementById("email");

        email.addEventListener("input", (event) => {
            if (email.validity.typeMismatch) {
                // perform if true
                email.setCustomValidity("I am expecting an email address!");
            } else {
                // perform if false
                email.setCustomValidity("");
            }
        });
    </script>
    ```

## Website vs Web App

| Differences |
|-------------|

| Website | Web App |
|---------|---------|
| A collection of webpages linked together with HTML. |  A software program |
| Generally static content | Dynamic content, user-driven interactions |
| Display content | Enable actions, transactions, and completing user tasks |
| View and read | View, read, and manipulate information |

## 09/01/2025 - Advanced CSS & JS

- Advanced CSS
- Advanced JS
- Publishing to Github Pages

## Advanced CSS 

### CSS Positioning

- The CSS position property specifies the type of method used for positioning an element

> To define an element position add the CSS property `position: <method>`

1. static

    - The default positioning for all elements
    - It is positioned in the normal flow of the website

    ```css
    p {
        position: static;
    }
    ```

2. relative

    - An element is positioned relative to its normal/natural position
    - Setting the margin properties on ana element with the relative position  will cause it to be adjusted away from its normal position. Any other content around the element will not be adjusted to fit the gap left by the element

    ```css
    p {
        left: 30px;
        position: relative;
    }
    ```

3. fixed

    - Positioned relative to the viewport, which means it always stays in the same place even if the page is scrolled.
    - It does not leave a gap in the page where it would normally have been positioned.
    - The top, right, bottom and left properties are used to the position the element.

    ```css
    p {
        position: fixed;
        bottom: 0px;
        right: 0px;
    }
    ```

4. sticky

    - Positioned based on the users scroll position.
    - Toggles between `relative` and `fixed`, depending on the scroll position.
    > NOTE: You must specify at least one of top, bottom, left, or right.

    ```css
    p {
        position: sticky;
        top: 0;
    }
    ```

5. absolute

### Grid Layout

- CCS Grid layout is a 2-dimensional layout system for the web.
- It allows tom organize content into rows and columns.
- When defining a grid it will only take effect when at least on of the dimensions has been specified.
- In order to specify flexible columns with the grid use fractional values `fr`. These are flexible and distribute space proportionally on the display page.
- In order to take care of the gaps between rows and columns you must use the `gap` property.

    ```css
    .container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 20px;
    }
    ```

### Adding effects using CSS

- You can add effects that are implemented according to user interaction
- You can add an effect by attaching to the desired CSS class, element or ID.
- You can attach an effect by adding `:<effect-name>` as a separate CSS class

    ```css
    p {
        background-color: red;
    }

    p:hover {
        opacity: 1;
    }

    .new-class {
        color: blue;
    }

    .new-class:hover {
        color: red;
    }
    ```

## Advanced JS

- A webpage is created in 3 layers:

1. HTML: is a markup that we use to structure and give meaning to our web content. e.g defining paragraphs, headings and tables.

2. CSS: styling the HTML. e.g setting background colours, fonts and dividing the content into multiple columns.

3. JavaScript: is scripting language that allows you to create dynamic updated content, control media and animate content.

    ```html
    <button type="button">Name</button>
    ```

    ```css
    button {
        letter-spacing: 1px;
        cursor: pointer;
        background-color: aliceblue;
        text-transform: uppercase;
        border: 2px solid;
    }
    ```

    ```js
    // Get hold of button element
    const button = document.querySelector("button");

    // Listen for a click on the button
    button.addEventListener("click", updateName);

    // Define updateName function
    function updateName() {
        // Ask user for input
        const name = prompt("Enter a new name:");
        // change the content of the button element
        button.textContent = name;
    }
    ```

## Deploying to GitHub Pages

1. Ensure that the repo is active on GitHub.

2. Navigate to the repository settings

3. In the Code and Automation section click `Pages`

4. Under "Build and Deployment" select `Deploy from a branch`

5. Under "Build and deployment" use the branch dropdown menu to select the publishing source

6. Optionally, you can use the folder dropdown to select a folder to publish from.

7. Save

8. In your browser navigate to `https://username.github.io/<repository-name>`
 
### Extra Resources

- https://www.w3schools.com/
- https://developer.mozilla.org/en-US/
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
