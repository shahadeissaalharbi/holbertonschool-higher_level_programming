cat << 'EOF' > README.md
# JavaScript - DOM Manipulation

## Description
This project covers basic DOM manipulation using JavaScript.
Each task focuses on selecting HTML elements and modifying their
style, content, or attributes using vanilla JavaScript (no frameworks).

## Requirements
- All files interpreted/compiled on Ubuntu 20.04 LTS
- All files should end with a new line
- Code should use the .js extension
- Semi-colons are compulsory

## Tasks

### 0. Color Me
File: `0-script.js`
Update the text color of the `header` HTML tag to red (#FF0000)
using `document.querySelector`.

Test with `0-main.html` in a browser.

cat << 'EOF' >> README.md

### 1. Click and turn red
File: \`1-script.js\`
Update the text color of the \`header\` HTML tag to red (#FF0000)
when the user clicks on the element with id \`red_header\`.

Test with \`1-main.html\` in a browser.
EOF

cat << 'EOF' >> README.md

### 2. Add .red class
File: \`2-script.js\`
Add the class \`red\` to the \`header\` HTML tag when the user
clicks on the element with id \`red_header\`.

Test with \`2-main.html\` in a browser.
EOF

cat << 'EOF' >> README.md

### 3. Toggle classes
File: \`3-script.js\`
Toggle the class of the \`header\` HTML tag between \`red\` and
\`green\` when the user clicks on the element with id
\`toggle_header\`. The header always has exactly one of these
classes, never both, never neither.

Test with \`3-main.html\` in a browser.
EOF


cat << 'EOF' >> README.md

### 4. List of elements
File: \`4-script.js\`
Add a new \`<li>Item</li>\` element to the \`ul\` element with
class \`my_list\` when the user clicks on the element with id
\`add_item\`.

Test with \`4-main.html\` in a browser.
EOF

cat << 'EOF' >> README.md

### 5. Change the text
File: \`5-script.js\`
Update the text of the \`header\` HTML tag to \`New Header!!!\`
when the user clicks on the element with id \`update_header\`.

Test with \`5-main.html\` in a browser.
EOF

cat << 'EOF' >> README.md

### 6. Star wars character
File: \`6-script.js\`
Fetch the character \`name\` from
\`https://swapi-api.hbtn.io/api/people/5/?format=json\` using the
Fetch API and display it in the HTML tag with id \`character\`.

Test with \`6-main.html\` in a browser.
EOF


cat << 'EOF' >> README.md

### 7. Star Wars movies
File: \`7-script.js\`
Fetch and list the \`title\` of all Star Wars movies from
\`https://swapi-api.hbtn.io/api/films/?format=json\` using the
Fetch API. All titles are listed in the \`ul\` element with id
\`list_movies\`.

Test with \`7-main.html\` in a browser.
EOF

cat << 'EOF' >> README.md

### 8. Say Hello!
File: \`8-script.js\`
Fetch from \`https://hellosalut.stefanbohacek.com/?lang=fr\` and
display the value of \`hello\` in the HTML element with id
\`hello\`. Works when imported from the \`<head>\` tag by waiting
for \`DOMContentLoaded\`.

Test with \`8-main.html\` in a browser.
EOF



## Author
Shahad Alharbi
EOF
