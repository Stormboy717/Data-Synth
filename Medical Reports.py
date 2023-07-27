import openai 
import time
import datetime
while True:
    from fpdf import FPDF

    # Set up OpenAI API credentials
    openai.api_key = 'Your API Key here'

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
        patient_name = generate_unique_value("Generate a random but uncommon patient name:")
        date_of_incident = generate_unique_value("Generate a random date:")
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

            def add_content(self, content):
                self.set_font('Arial', '', 12)
                self.multi_cell(0, 7, content.encode('latin-1', 'ignore').decode('latin-1'))
                self.ln(10)
        pdf = PDF()
        pdf.add_page()
        if medical_assessment.startswith("Medical Assessment:"):
            medical_assessment = medical_assessment.replace("Medical Assessment:", "")
            
        if treatment_plan.startswith("Treatment Plan:"):
            treatment_plan = treatment_plan.replace("Treatment Plan:", "")

        medical_assessment = medical_assessment.lstrip("\n")
        treatment_plan = treatment_plan.lstrip("\n")
        # Add patient details in a text box
        pdf.set_fill_color(235, 244, 253)  # Light gray color
        pdf.cell(0, 10, 'Incident Details', 0, 1, 'L', 1)
        pdf.add_content('Patient Name: {}'.format(patient_name))
        pdf.add_content('Date of Incident: {}'.format(date_of_incident))
        pdf.add_content('Description of Incident:')
        pdf.add_content(description_of_incident)

        # Add medical assessment in a text box
        pdf.set_fill_color(252, 241, 221)  # Light yellow color
        pdf.cell(0, 10, 'Medical Assessment', 0, 1, 'L', 1)
        pdf.add_content(medical_assessment)

        # Add treatment plan in a text box
        pdf.set_fill_color(235, 249, 234)  # Light green color
        pdf.cell(0, 10, 'Treatment Plan', 0, 1, 'L', 1)
        pdf.add_content(treatment_plan)
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

    generate_pdf_report(report_text, patient_name, date_of_incident, description_of_incident, medical_assessment, treatment_plan)

    print("PDF report generated successfully!")

