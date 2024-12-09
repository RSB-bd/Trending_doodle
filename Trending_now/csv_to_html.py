# converting the csv to a nicely formated webpage
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default file to load
    file_name = 'product_data.csv'
    dataFrame = None

    if request.method == 'POST':
        uploaded_file = request.files['csv_file']
        if uploaded_file.filename != '':
            dataFrame = pd.read_csv(uploaded_file)
    else:
        # Load default file
        dataFrame = pd.read_csv(file_name)

    if dataFrame is not None:
        # Add image rendering for the table
        if 'IMG' in dataFrame.columns:
            dataFrame['IMG'] = dataFrame['IMG'].apply(
                lambda x: f'<img src="{x}" alt="Product Image" width="100">' if pd.notnull(x) else 'No Image'
            )
        # Convert DataFrame to an HTML table
        html_table = dataFrame.to_html(escape=False, classes='table table-striped table-bordered', index=False)
        return render_template('index.html', table=html_table)

    return render_template('index.html', table=None)

if __name__ == '__main__':
    app.run(debug=True)

