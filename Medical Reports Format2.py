
import openai
import time
import datetime
from fpdf import FPDF
while True:
    

    # Set up OpenAI API credentials
    openai.api_key = 'your key here'

    # Generate a unique value using ChatGPT
    def generate_unique_value(prompt):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=200,
            temperature=0.7,
            n=1,
            stop=None,
        )

        value = response.choices[0].text.strip()
        return value

    # Generate the medical report using ChatGPT
    def generate_medical_report():
        prompt = """
        Generate a fake medical incident report.

        Incident Details:
        Patient Name: {}
        Date of Incident: {}
        Description of Incident: {}

        Medical Assessment:
        {}

        Treatment Plan:
        {}

        """

        # Generate unique values
        patient_name = generate_unique_value("Generate a random patient name:")
        date_of_incident = generate_unique_value("Generate a random date after from 2022 to 2023:")
        description_of_incident = generate_unique_value("Generate a random description of the medical incident:")
        medical_assessment = generate_unique_value("Generate Medical assessment based on. " + description_of_incident + ":")
        treatment_plan = generate_unique_value("Generate a treatment plan based on. " + description_of_incident + " and " + medical_assessment + ":")

        report = prompt.format(patient_name, date_of_incident, description_of_incident, medical_assessment, treatment_plan)
        return report, patient_name, date_of_incident, description_of_incident, medical_assessment, treatment_plan

    # Generate PDF report
    def generate_pdf_report(report_text, patient_name, date_of_incident, description_of_incident, medical_assessment, treatment_plan):
        class PDF(FPDF):
            def header(self):
                # Set up logo with transparent background
                self.image('logo.png', 10, 8, 33, 0, 'PNG')

                # Add blank space for the full image
                self.ln(30)  # Adjust the value based on your needs

                # Add title
                self.set_font('Arial', 'B', 16)
                self.cell(0, 20, 'Medical Incident Report', 0, 1, 'C')
                self.ln(10)

            def footer(self):
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')
                self.set_y(-15)
                self.set_font('Arial', 'B', 12)
                self.cell(0, 10, 'Medic 1', 0, 0, 'R')

            def add_content(self, content):
                self.set_font('Arial', '', 12)
                self.multi_cell(0, 7, content)

        pdf = PDF()
        pdf.add_page()
        
        if medical_assessment.startswith("Medical Assessment:"):
            medical_assessment = medical_assessment.replace("Medical Assessment:", "")
            
        if treatment_plan.startswith("Treatment Plan:"):
            treatment_plan = treatment_plan.replace("Treatment Plan:", "")

        medical_assessment = medical_assessment.lstrip("\n")
        treatment_plan = treatment_plan.lstrip("\n")
        # Set up pamphlet-style design with Incident Details on top
        pdf.set_fill_color(235, 244, 253)  # Light gray color
        pdf.cell(0, 10, 'Incident Details', 0, 1, 'L', 1)
        pdf.add_content('Patient Name: {}'.format(patient_name))
        pdf.add_content('Date of Incident: {}'.format(date_of_incident))
        pdf.add_content('Description of Incident:\n{}'.format(description_of_incident))

        # Add spacer between Medical Assessment and Treatment Plan
        pdf.ln(7)

        # Set up shaded text boxes for Medical Assessment and Treatment Plan side by side
        pdf.set_fill_color(252, 241, 221)  # Light yellow color
        pdf.cell(95, 10, 'Medical Assessment', 0, 0, 'L', 1)
        pdf.set_fill_color(235, 249, 234)  # Light green color
        pdf.cell(95, 10, 'Treatment Plan', 0, 1, 'L', 1)
        pdf.set_fill_color(255, 255, 255)  # White color

        # Get the current y position of the document
        y_position = pdf.get_y()
        pdf.set_fill_color(252, 241, 221)  # Light yellow color
        # Add Medical Assessment text
        pdf.set_font('Arial', 'I', 10)
        pdf.multi_cell(95, 7, medical_assessment, fill=True)

        # Move to the same y position as Medical Assessment and add Treatment Plan text
        pdf.set_y(y_position)
        pdf.set_x(105)
        pdf.set_fill_color(235, 249, 234)  # Light green color
        pdf.set_font('Arial', 'I', 10)
        pdf.multi_cell(95, 7, str(treatment_plan), fill=True)  # Convert treatment_plan to string
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        pdf.output('medical_report-'+ timestamp +'.pdf', 'F')


    # Generate and save the PDF report
    report_text, patient_name, date_of_incident, description_of_incident, medical_assessment, treatment_plan = generate_medical_report()

    # Print variable values for verification
    print("Patient Name:", patient_name)
    print("Date of Incident:", date_of_incident)
    print("Description of Incident:", description_of_incident)
    print("Medical Assessment:", medical_assessment)
    print("Treatment Plan:", treatment_plan)
    try:
        generate_pdf_report(report_text, patient_name, date_of_incident, description_of_incident, medical_assessment, treatment_plan)
        print("PDF report generated successfully!")
    except Exception as e: 
        print(e)
