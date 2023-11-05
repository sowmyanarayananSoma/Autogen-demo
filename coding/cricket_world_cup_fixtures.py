# filename: cricket_world_cup_fixtures.py
from fpdf import FPDF

pdf = FPDF()
pdf.set_font("Arial", size=12)
pdf.add_page()

fixtures_data = [
    "Fixture 1",
    "Fixture 2",
    "Fixture 3",
    # Add more fixtures here
]

for fixture in fixtures_data:
    pdf.cell(0, 10, txt=fixture, ln=True)

pdf.output("2023_cricket_world_cup_fixtures.pdf")