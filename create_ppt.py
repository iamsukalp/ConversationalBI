import pyppt
import plotly.io as pio
import pandas as pd
import tempfile
import os

# Assuming your project folder is named "MyProject"
project_folder = os.getcwd()


def create_pptx(slides_data):
    # Create a presentation object
    prs = pyppt.Presentation()

    for slide_data in slides_data:
        question, dataframe, insight, chart = slide_data

        # Add a slide
        slide = prs.add_slide()

        # Add the question as the slide title
        slide.add_text(question, x=1, y=1, width=8.5, height=1, font_size=24, bold=True)

        # Add the insight as the content
        slide.add_text(insight, x=1, y=1.5, width=8.5, height=1)

        # Add the dataframe as a table
        rows, cols = dataframe.shape
        table = slide.add_table(
            dataframe.values.tolist(), x=1, y=3, width=8.5, height=2.5
        )
        table.set_column_titles(dataframe.columns.tolist())

        # Save the Plotly chart as an image and add it to the slide
        if chart is not None:
            with tempfile.NamedTemporaryFile(
                suffix=".png", dir=project_folder, delete=False
            ) as tmpfile:
                chart_image_path = tmpfile.name
                pio.write_image(chart, chart_image_path)
                slide.add_image(chart_image_path, x=1, y=5.5, width=8.5, height=3)

    # Save the presentation
    ppt_path = "presentation.pptx"
    prs.save(ppt_path)
    return ppt_path
