"""
Generate PDF reports from data included in several Pandas DataFrames
From pbpython.com

To run: $ python pdf_maker.py sales-funnel.xlsx test.pdf

What I did to make this work (maybe needed)
pip install --upgrade weasyprint
brew update #(change permissions if needed: sudo chown -R $USER:admin /usr/local/)
brew install cairo
brew link --force cairo
brew install py2cairo
brew install pango
"""
from __future__ import print_function
import pandas as pd
import numpy as np
import argparse
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def create_pivot(df, infile, index_list=["Manager", "Rep", "Product"], value_list=["Price", "Quantity"]):
    """Create a pivot table from a raw DataFrame and return it as a DataFrame"""
    table = pd.pivot_table(df, index=index_list, values=value_list, aggfunc=[np.sum, np.mean], fill_value=0)
    return table


def get_summary_stats(df,product):
    """For certain products we want National Summary level information on the reports
    Return a list of the average quantity and price"""
    results = []
    results.append(df[df["Product"] == product]["Quantity"].mean())
    results.append(df[df["Product"] == product]["Price"].mean())
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate PDF report')
    parser.add_argument('infile', type=argparse.FileType('r'), help="report source file in Excel")
    parser.add_argument('outfile', type=argparse.FileType('w'), help="output file in PDF")
    args = parser.parse_args()

    # Read in the file and get our pivot table summary
    df = pd.read_excel(args.infile.name)
    sales_report = create_pivot(df, args.infile.name)

    # Get some national summary to include as well
    manager_df = []
    for manager in sales_report.index.get_level_values(0).unique():
        manager_df.append([manager, sales_report.xs(manager, level=0).to_html()])

    # Do our templating now
    # We can specify any directory for the loader but for this example, use current directory
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("myreport.html")
    template_vars = {"title" : "National Sales Funnel Report", "CPU" : get_summary_stats(df, "CPU"),
					 "Software": get_summary_stats(df, "Software"), "national_pivot_table": sales_report.to_html(),
					 "Manager_Detail": manager_df}

    # Render our file and create the PDF using our css style file
    html_out = template.render(template_vars)
    HTML(string=html_out).write_pdf(args.outfile.name, stylesheets=["style.css"])
