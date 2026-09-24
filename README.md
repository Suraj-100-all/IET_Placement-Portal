# IET Placement Portal

> A Flask-based prototype for the Training and Placement Cell of the Institute of Information Technology, Deen Dayal Upadhyaya Gorakhpur University.

## GitHub Description

An IET Placement Portal prototype that helps the Training and Placement Cell approach companies and publish placement-drive details such as job profile, eligibility criteria, package, visit date, schedule, notices, and application links for students.

## Overview

The purpose of this project is to provide a single digital platform for coordinating campus placements between the Training and Placement Cell, recruiting companies, and students.

Through this portal, the department can present company opportunities in an organized way, while students can quickly find the information they need before applying to a placement drive.

## Key Features

- Home dashboard with placement statistics, notices, quick links, and upcoming drives
- Company listing page with search and filters for status and branch
- Placement-drive details including:
  - Company name and industry
  - Job profile
  - Visit or drive date
  - Package offered
  - Eligible branches
  - Minimum academic criteria
  - Apply action
- Placement schedule page for upcoming recruitment drives
- Student guidelines page with eligibility and participation information
- Login and registration interface for students, companies, and administrators/TPO
- About page describing the role of the Training and Placement Cell
- Responsive frontend styled for an institutional placement portal

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Templating:** Jinja2 through Flask
- **Fonts:** Google Fonts

## Project Structure

```text
IET_Placement_Portal/
├── app.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── about.html
    ├── companies.html
    ├── index.html
    ├── login.html
    ├── schedule.html
    └── students.html
```

## Getting Started

### Prerequisites

- Python 3.9 or later
- `pip`

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd IET_Placement_Portal
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Flask:

   ```bash
   pip install Flask
   ```

4. Start the development server:

   ```bash
   python app.py
   ```

5. Open the portal at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Available Routes

| Route | Purpose |
| --- | --- |
| `/` | Home dashboard |
| `/companies` | Company and placement-drive listings |
| `/students` | Student placement guidelines |
| `/schedule` | Placement-drive schedule |
| `/about` | About the Training and Placement Cell |
| `/login` | Student, company, and admin login UI |

## Prototype Status

This repository currently contains a presentation-ready frontend prototype. The company data, notices, statistics, and schedule entries are static demo content rendered through Flask templates.

Authentication, database persistence, real company onboarding, admin approval workflows, email notifications, and production application processing are planned for future development.

## Future Scope

- Add a database for students, companies, drives, applications, and notices
- Implement secure authentication and role-based access control
- Allow companies to submit recruitment requirements through the portal
- Add TPO approval and publishing workflows
- Add student profiles, application tracking, and document uploads
- Send email or portal notifications for new drives and deadlines
- Add an admin dashboard for managing the complete placement cycle

## Intended Users

- **Training and Placement Cell:** Approach companies, verify opportunities, and publish recruitment information
- **Companies:** Share hiring requirements and campus-drive details
- **Students:** View eligibility, dates, packages, and application information in one place

## Disclaimer

This project is an academic/prototype implementation created for demonstration and presentation purposes. It is not an official production portal of DDUGU or IET unless separately deployed and authorized by the institution.

## License

No license has been specified yet. Add a license before distributing or accepting external contributions.