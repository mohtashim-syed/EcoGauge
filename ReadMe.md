# EcoGauge
### EcoGauge is a Flutter-based application designed to provide users with insightful data visualizations and interactions related to environmental metrics. Leveraging the power of large language models (LLMs), EcoGauge offers a user-friendly interface to explore and analyze environmental data effectively.

## What it does
Toyota EcoGauge is a cross-platform application that allows users to:
- Query and visualize vehicle fuel economy data for Toyota models from 2021-2025.
- Compare different models and trims over the years to spot trends or improvements.
- Leverage AI-powered and fine-tuned chatbots to interact conversationally with the data, gaining tailored insights and analysis.
- View interactive graphs and data tables for better decision-making.

## How we built it
Frontend: Developed with Flutter to ensure a responsive and consistent experience across mobile and web platforms. 
Backend: Utilized open government datasets on fuel economy, processed and served via a structured API for querying with endpoints that allow users to retrieve vehicle-specific data, compare fuel efficiency metrics, and analyze trends based on parameters like make, model, and year.
Flask Visualization: Integrated libraries for interactive graphing and tabular data representation. 
AI Chatbot: Incorporated GPT-based chatbots (Miles and Finn) to provide natural language data querying and insights. 
Modular Architecture: Designed for scalability and easy integration of future datasets and features.

## Challenges we ran into
Data Parsing: Extracting and structuring data from static PDFs (2021-2025 datasets) into a format optimized for querying and visualization. 
UI Consistency: Ensuring a seamless, visually appealing interface across different devices and platforms. 
AI Integration: Creating a conversational interface that accurately interprets user queries and interacts with the structured data. 
Time Constraints: Balancing feature implementation and testing within a tight 24-hour hackathon timeline.

## Accomplishments that we're proud of
Successfully implemented a fine-tuned AI-powered chatbot integration for natural language querying. Developed an intuitive and visually consistent *cross-platform* interface using Flutter within 24 hours. Processed and visualized large volumes of fuel economy data into meaningful, user-friendly formats.

## What we learned
The importance of data cleaning and preparation when working with unstructured sources like PDFs. 
How to leverage Flutter for building scalable, cross-platform applications efficiently.
Best practices for integrating AI tools (GPT-based chatbots) with structured backend systems. 
The value of teamwork and effective communication when working under tight deadlines.

