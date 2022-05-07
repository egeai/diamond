"""Command-line interface."""
import click
from scraper.pdf import PdfScraper

@click.command()
@click.version_option()
def main() -> None:
    """Diamond."""
    pdf_scraper = PdfScraper()
    pdf_scraper.scrape()

if __name__ == "__main__":
    main(prog_name="diamond")  # pragma: no cover
