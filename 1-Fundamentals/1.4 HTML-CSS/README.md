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