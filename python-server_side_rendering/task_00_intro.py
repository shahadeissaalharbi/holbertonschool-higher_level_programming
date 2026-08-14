#!/usr/bin/python3
"""Simple templating program that generates invitation files."""
import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries with attendee data.
    """
    if not isinstance(template, str):
        logging.error("Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        logging.error("Attendees must be a list of dictionaries.")
        return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace(
                "{" + placeholder + "}", str(value)
            )

        output_filename = "output_{}.txt".format(index)
        with open(output_filename, "w") as output_file:
            output_file.write(content)
