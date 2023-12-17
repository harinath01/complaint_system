# Complaint Management System

The **Complaint Management System** is a web application designed to handle complaints related to improper attire in an educational institution.

![Demo](https://github.com/harinath01/complaint_system/assets/89839073/0f8dc241-e3eb-4291-afca-c6bbf53b8965)

## Features

- Submit complaints about improper attire.
- Scan student ID using a barcode scanner.
- Choose the type of complaint from a predefined list.
- View and manage submitted complaints.

## Technologies Used

- **Django**: Web framework for building the backend.
- **HTML/CSS**: Frontend design and structure.
- **Tailwind CSS**: Utility-first CSS framework for styling.
- **QuaggaJS**: Barcode scanner library.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/complaint-management-system.git```

2. **Install dependencies**:

   ```bash
   pip install -r requirements/prod.txt
   ```

3. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**

   ```bash
   python manage.py runserver
   ```
5. Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Usage
  - Visit the homepage to submit a complaint.
  - Use the barcode scanner to scan student IDs.
  - Choose the type of complaint from the dropdown menu.
  - Click "Submit" to submit the complaint.
