# Python - Server-Side Rendering

## Description
This project covers server-side rendering concepts in Python,
starting with basic string templating and Flask/Jinja templating.

## Tasks

### 0. Creating a Simple Templating Program
File: `task_00_intro.py`
Function `generate_invitations(template, attendees)` generates
personalized invitation files from a template with placeholders
(`{name}`, `{event_title}`, `{event_date}`, `{event_location}`)
and a list of attendee dictionaries. Handles empty template/list,
missing data (replaced with "N/A"), and invalid input types with
appropriate error logging. Output files are named `output_X.txt`.

### 1. Creating a Basic HTML Template in Flask
File: `task_01_jinja.py`
Basic Flask application with routes `/`, `/about`, and
`/contact`, each rendering a Jinja template from the
`templates/` folder. Reusable `header.html` and `footer.html`
components are included in every page via `{% include %}` to
avoid duplicating markup.

## Author
Shahad Alharbi

### 2. Creating a Dynamic Template with Loops and Conditions in Flask
File: `task_02_logic.py`
Adds a `/items` route that reads `items.json` and renders
`items.html` using Jinja's `{% for %}` loop to list items and
`{% if %}` to show "No items found" when the list is empty.
