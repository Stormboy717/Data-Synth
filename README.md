# Medical Incident Report Generator

This repository contains three Python scripts for generating medical incident reports and a selection of logo images. Each script uses OpenAI's GPT-3 language model to generate a fake medical incident report and saves it as a PDF document. The reports include incident details, medical assessment, and a treatment plan. The generated PDF reports follow a pamphlet-style design with incident details on top and shaded text boxes for medical assessment and treatment plan side by side.

## Scripts

### 1. HSE Reports.py

This script generates a fake medical incident report following the Health, Safety, and Environment (HSE) format. The incident details, medical assessment, and treatment plan are organized in a structured manner suitable for HSE reporting.

### 2. Medical Reports Format2.py

This script generates a fake medical incident report with a different layout from the HSE format. The report includes incident details, medical assessment, and treatment plan in a user-friendly format.

### 3. Medical Reports.py

This script also generates a fake medical incident report. It may follow a format similar to Medical Reports Format2.py or a custom layout based on user preferences.

## Logo Images

Three logo images, namely `logo1.png`, `logo2.png`, and `logo3.png`, are provided as options for the PDF report's logo placement. You can choose the most suitable logo for your medical incident reports.

## Prerequisites

Before running the scripts, ensure you have the following components installed:

- Python 3.x
- `openai` Python package
- `fpdf` Python package

You will also need an API key from OpenAI to access their language model. Make sure to set up your OpenAI API key in each script before running it.

## Setup

1. Clone this repository to your local machine:
``` git clone https://github.com/your-username/medical-incident-report-generator.git
cd medical-incident-report-generator ``` 
2. Install the required Python packages:
``` pip install openai fpdf ```

3. Set up your OpenAI API key:

You can obtain your OpenAI API key by signing up on their website (https://beta.openai.com/signup/). Replace the empty string `openai.api_key = ''` in each script with your API key.

## Usage

Choose the script (`HSE Reports.py`, `Medical Reports Format2.py`, or `Medical Reports.py`) you want to use and execute it by running the following command:


The script will generate a PDF report with a filename in the format `medical_report-YYYYMMDDHHMMSS.pdf`, where `YYYYMMDDHHMMSS` represents the current timestamp.

## Customization

You can customize the generation of the medical incident report by modifying the respective `generate_medical_report` function in each script. The function currently generates random patient names, dates of incident, and descriptions of the incident. You can edit the prompts to ask for specific information or provide fixed values.

## Acknowledgments

The scripts use OpenAI's GPT-3 language model to generate text. Special thanks to OpenAI for providing this powerful language model.

Please note that these scripts generate fake medical reports for demonstration purposes only and should not be used for any actual medical documentation.



