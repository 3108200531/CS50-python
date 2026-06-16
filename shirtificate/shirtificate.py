from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        """Creates the header for the PDF."""
        self.set_font("Helvetica", "B", 45)
        # Moving to a position that leaves a nice margin at the top
        self.ln(15)
        # Title: centered, no border, line break afterward
        self.cell(0, 10, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(20)

    def create_shirt(self, name):
        """Places the shirt image and overlays the user's name in white text."""
        # A4 width is 210mm. Let's make the shirt 180mm wide.
        shirt_width = 180
        # Centering calculation: (Total Width - Image Width) / 2
        x_centered = (210 - shirt_width) / 2

        # Place the image (ensure 'shirtificate.png' is in your directory)
        self.image("shirtificate.png", x=x_centered, y=70, w=shirt_width)

        # Configure text settings for the overlay
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(255, 255, 255)  # White text

        # Absolute positioning to overlay the text directly onto the shirt
        # Adjust y=130 depending on where your specific image asset sits
        self.set_y(130)
        self.cell(0, 10, f"{name} took CS50", align="C")


def main():
    # Prompt the user for their name
    name = input("Name: ").strip()

    # Initialize FPDF with Portrait (P), millimeters (mm), and A4 format
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")

    # Disable auto page breaks to prevent content spilling into a 2nd page
    pdf.set_auto_page_break(auto=False)

    # Add a page (triggers header() automatically)
    pdf.add_page()

    # Draw the shirt and the user's customized name
    pdf.create_shirt(name)

    # Output the generated document
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
