import openai 
import time
import datetime
from fpdf import FPDF

# Set up OpenAI API credentials
openai.api_key = 'Your API Key here'

# Generate a unique value using ChatGPT
def generate_unique_value(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7,
        n=1,
        stop=None,
    )
    value = response.choices[0].text.strip()
    return value

# Generate the medical report using ChatGPT
def generate_medical_report():
    # Your prompt here...
    prompt = """
    "Please generate a quniue incident reports using the following as examples, but the reuslts must be unuque and long, around 1000 words at least anything in perenthesis  a should be generated by you for example  (Your Name) should be a random name generated by you  :

Date: 25th July 2023
Location: Manufacturing Plant, Bristol, South West Region
Inspector: John Smith, Field Accident Inspector - South West Region

Description of Accident:

On the aforementioned date, 17th August 2023, at approximately 10:30 AM, a severe accident occurred at the manufacturing plant located in Bristol, South West Region, involving the factory worker, Mark Johnson. The incident resulted in severe burns to the said worker due to a chemical spill.

Chronology of Events:



At 10:30 AM, an unforeseen chemical spill incident occurred in the manufacturing plant's production area. The specific chemical involved was identified as Hydrochloric Acid, which is known for its hazardous properties.

Mark Johnson, an experienced factory worker, was in the immediate vicinity of the chemical spill at the time of the accident. The exact cause of the spill is currently under investigation, and a thorough examination will be conducted to determine the contributing factors.

Upon immediate realization of the spill, the plant's emergency response team was activated, and the on-site first-aid personnel were dispatched to the accident scene.

Mark Johnson was promptly attended to by the first-aid responders. He was found to have sustained severe burns on his upper limbs, face, and upper torso due to direct exposure to the spilled chemical.

Emergency medical services were promptly summoned to the manufacturing plant, and Mr. Johnson was transported to the nearest medical facility for urgent medical attention and specialized treatment.

The manufacturing plant's safety protocols were followed to contain and neutralize the chemical spill. Additionally, the relevant authorities were notified about the incident as per the legal requirements.

Injuries Sustained:

Mark Johnson suffered severe burns as a result of direct contact with the spilled chemical. The extent of his injuries will be assessed by medical professionals at the medical facility, and further details will be available from their medical report.

Recommendations:



An immediate halt to the operations in the affected area until the cause of the chemical spill and the potential safety lapses are identified and rectified.

A comprehensive investigation to determine the root cause of the chemical spill and a thorough review of the manufacturing plant's safety protocols, training procedures, and hazard management measures.

A mandatory review of the safety equipment provided to the workers, including personal protective equipment (PPE), and its proper utilization during hazardous operations.

Reassessment of the emergency response plan and measures to ensure a more efficient and prompt response to any future accidents.

Additional training and awareness programs for all factory workers on chemical safety, hazard identification, and proper emergency response protocols.

Conclusion:

The accident involving Mark Johnson at the manufacturing plant in Bristol, South West Region, on 17th August 2023, resulted in severe burns due to a chemical spill. The incident is under investigation, and all necessary measures will be taken to prevent such accidents in the future. The management of the manufacturing plant is fully cooperating with the investigation and is committed to implementing the recommended safety measures to ensure the well-being of its employees.

As the Field Accident Inspector - South West Region, I will closely monitor the progress of the investigation and work with the relevant stakeholders to ensure that corrective actions are promptly taken.

Inspector's Name:
John Smith
Field Accident Inspector - South West Region
Date: 25th July 2023

Date: 25th July 2023
Location: High-Rise Building, 123 Main Street, London
Incident Date: 5th October 2022
Investigator: Jane Williams, Fire Safety Investigator - London Metropolitan Fire Brigade

Executive Summary:

On 5th October 2022, a major fire broke out at a high-rise building located at 123 Main Street, London. The incident resulted in several injuries and extensive property damage. As the Fire Safety Investigator for the London Metropolitan Fire Brigade, I was assigned to conduct a thorough investigation to determine the cause, origin, and contributing factors of the fire. The purpose of this report is to present the findings of the investigation.

Incident Overview:

At approximately 2:30 PM on 5th October 2022, emergency services received multiple calls reporting a fire at the high-rise building in question. The building was a commercial and residential complex, consisting of 25 floors.

Response:

The London Metropolitan Fire Brigade responded promptly to the incident, dispatching several fire crews, including ladder units and specialized teams, to the scene. The fire was characterized as a high-intensity blaze, and its rapid spread posed significant challenges to the firefighting efforts.

Casualties and Injuries:

During the incident, 12 individuals sustained injuries of varying degrees. Emergency medical services were on-site to provide immediate medical assistance to the injured, and they were subsequently transported to nearby hospitals for further treatment. Tragically, 3 fatalities were reported as a result of the fire.

Investigation Findings:



Origin and Cause:

The investigation determined that the fire originated on the 15th floor of the building. The exact cause of the fire is yet to be definitively established, and it remains a subject of ongoing investigation. Potential ignition sources in the area of origin, including electrical equipment, heating systems, and flammable materials, have been identified and will be closely examined for any signs of malfunction or misuse.



Fire Spread:

The fire quickly escalated due to the presence of combustible materials, inadequate fire compartmentalization, and a lack of fire-resistant barriers in the building's structure. The building's ventilation system, while designed to maintain air circulation, inadvertently aided the rapid spread of smoke and flames to higher floors.



Fire Safety Systems and Equipment:

Preliminary observations suggest that some of the building's fire safety systems and equipment were not functioning optimally. Fire alarms on certain floors failed to activate, impeding early detection of the fire. Additionally, there were reports of malfunctioning fire hydrants, which hindered firefighting efforts.



Evacuation Procedures:

The evacuation procedures in place at the building were not efficiently executed. Some occupants were unsure of the designated evacuation routes, leading to delays and confusion during the evacuation process. Proper fire drills and regular safety training for building occupants could have improved their response and facilitated a more organized evacuation.



Building Maintenance and Compliance:

A thorough examination of building maintenance records and compliance documents revealed several discrepancies related to fire safety measures. It was evident that the building had not undergone regular fire safety audits, and some fire safety installations, such as fire doors and fire extinguishers, were not up to standard.

Recommendations:

Based on the findings of the investigation, the following recommendations are made to prevent similar incidents and enhance fire safety:



Conduct a detailed investigation into the cause of the fire, involving specialists and relevant authorities, to ascertain the ignition source definitively.

Conduct a comprehensive review of the building's fire safety systems, including fire alarms, sprinkler systems, and fire suppression equipment, to ensure they are fully functional and well-maintained.

Implement regular fire safety drills and training for all building occupants to familiarize them with evacuation procedures and enhance their preparedness during emergencies.

Review and enhance the building's fire compartmentalization and fire-resistant barriers to prevent the rapid spread of fire between floors.

Perform a thorough inspection of fire doors, fire hydrants, and other fire safety installations to ensure compliance with safety regulations.

Establish a maintenance schedule for all fire safety equipment and systems, conducting regular audits to ensure compliance with fire safety standards.

Collaborate with building management to improve communication and dissemination of emergency information to all occupants.

Conclusion:

The major fire incident at the high-rise building in London on 5th October 2022 resulted in numerous injuries and significant property damage. The investigation has shed light on several factors contributing to the severity of the incident, including potential fire safety system malfunctions, inadequate evacuation procedures, and a lack of regular maintenance and compliance checks.

As the Fire Safety Investigator for the London Metropolitan Fire Brigade, I recommend implementing the aforementioned measures to enhance fire safety and prevent similar incidents in the future. The collaboration of all relevant stakeholders, including building management, regulatory authorities, and fire safety professionals, is essential to ensuring the safety of occupants and properties in high-rise buildings throughout the city.

Investigator's Name:
Jane Williams
Fire Safety Investigator - London Metropolitan Fire Brigade
Date: 25th July 2023




    Remember to provide comprehensive details and findings in each report based on your expertise as the designated investigator."
        """
    report_text = generate_unique_value(prompt)
    return report_text

# Generate PDF report
def generate_pdf_report(report_text):
    class PDF(FPDF):
        def header(self):
            # Set up logo with transparent background
            self.image('logo.png', 10, 8, 33, 0, 'PNG')

            # Add blank space for the full image
            self.ln(30)  # Adjust the value based on your needs

            # Add title
            self.set_font('Arial', 'B', 16)
            self.cell(0, 20, 'HSE Incident Report ', 0, 1, 'C')
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
    pdf.set_fill_color(235, 244, 253)  # Light gray color
    pdf.cell(0, 10, 'Incident Report', 0, 1, 'L', 1)
    pdf.add_content(report_text)

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pdf.output('incident-report-'+ timestamp +'.pdf', 'F')

# Generate and save the PDF report
while True:
    report_text = generate_medical_report()
    generate_pdf_report(report_text)
    print("PDF report generated successfully!")
