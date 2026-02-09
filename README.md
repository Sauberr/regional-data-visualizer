# 📊 Regional Data Visualizer

<div align="center">

**An elegant and powerful Python-based data visualization tool for regional analytics**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-green.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-6.3.1-red.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Transform your regional CSV data into stunning, interactive bar charts with just a few lines of code!

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [License](#-license)

</div>

---

## 🌟 Features

- 📈 **Interactive Visualizations** - Create dynamic, interactive bar charts with zoom, pan, and hover capabilities
- 🎨 **Beautiful Design** - Clean, professional charts with customizable colors and layouts
- 📂 **CSV Support** - Easy data import from CSV files
- 🌍 **Regional Focus** - Perfect for visualizing regional, district, or city-level data
- 🔧 **Highly Customizable** - Adjust colors, sizes, fonts, and layouts to match your needs
- ⚡ **Fast & Efficient** - Built on Pandas for efficient data processing
- 🖥️ **Browser-Based** - View your visualizations in any modern web browser

## 🛠️ Technologies Used

This project is built with modern, industry-standard libraries:

- **[Python 3.8+](https://www.python.org/)** - Core programming language
- **[Pandas 2.3.3](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[Plotly 6.3.1](https://plotly.com/)** - Interactive visualization library

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (usually comes with Python)

To verify your Python installation, run:
```bash
python --version
# or
python3 --version
```

## 🚀 Installation

Follow these simple steps to get started:

### 1. Clone the Repository

```bash
git clone https://github.com/Sauberr/regional-data-visualizer.git
cd regional-data-visualizer
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! You're ready to visualize your data. 🎉

## 📖 Usage

### Quick Start

1. **Prepare your CSV file** named `input_data.csv` with the following structure:

```csv
Область,Місто/Район,Значення
Київська,Район 1,150
Київська,Район 2,200
Львівська,Район 1,180
Львівська,Район 2,220
```

**Column meanings:**
- `Область` - Region/Oblast name
- `Місто/Район` - City/District name
- `Значення` - Numeric value to visualize

2. **Run the visualizer:**

```bash
python main.py
```

3. **View your chart** - The interactive visualization will automatically open in your default web browser!

### Understanding Your Data Format

The CSV file should have three columns:

| Column | Description | Example |
|--------|-------------|---------|
| **Область** (Region) | The main regional category | Київська, Львівська |
| **Місто/Район** (District) | Sub-category or district | Район 1, Центральний |
| **Значення** (Value) | Numeric data to visualize | 150, 200, 350 |

### Example Output

The script generates an interactive stacked bar chart with:
- ✅ Regions on the X-axis
- ✅ Values on the Y-axis
- ✅ Color-coded districts
- ✅ Interactive hover tooltips
- ✅ Zoom and pan capabilities
- ✅ Professional styling

## ⚙️ Configuration

You can customize the visualization by modifying `main.py`:

### Chart Dimensions
```python
height=800,  # Chart height in pixels
width=1200   # Chart width in pixels
```

### Bar Spacing
```python
bargap=0.5,        # Gap between bars (0-1)
bargroupgap=0.1    # Gap between bar groups (0-1)
```

### Colors and Styling
Plotly automatically assigns colors, but you can customize them:
```python
fig.update_traces(width=0.3)  # Bar width
```

### Fonts and Text
```python
font=dict(size=14)  # Global font size
xaxis_tickangle=-45  # Rotate X-axis labels
```

## 📁 Project Structure

```
regional-data-visualizer/
├── main.py              # Main visualization script
├── requirements.txt     # Python dependencies
├── input_data.csv       # Your data file (you create this)
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore          # Git ignore rules
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'pandas'`
- **Solution:** Make sure you've installed dependencies: `pip install -r requirements.txt`

**Issue:** `FileNotFoundError: 'input_data.csv'`
- **Solution:** Create an `input_data.csv` file in the project root directory

**Issue:** Chart doesn't open in browser
- **Solution:** Check if a firewall is blocking the local server, or manually open the HTML file that Plotly generates

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Dmitriy Birilko

## 👤 Author

**Dmitriy Birilko**

- GitHub: [@Sauberr](https://github.com/Sauberr)

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">
Made with ❤️ and Python
</div>
