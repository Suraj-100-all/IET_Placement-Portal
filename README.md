# IET Placement Portal

> A Flask-based prototype for the Training and Placement Cell of the Institute of Information Technology, Deen Dayal Upadhyaya Gorakhpur University.

## GitHub Description

An IET Placement Portal prototype that helps the Training and Placement Cell approach companies and publish placement-drive details such as job profile, eligibility criteria, package, visit date, schedule, notices, and application links for students.

## Overview

The purpose of this project is to provide a single digital platform for coordinating campus placements between the Training and Placement Cell, recruiting companies, and students.

Through this portal, the department can present company opportunities in an organized way, while students can quickly find the information they need before applying to a placement drive.

## Key Features

  - Company name and industry
  - Job profile
  - Visit or drive date
  - Package offered
  - Eligible branches
  - Minimum academic criteria
  - Apply action

## Tech Stack


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

An IET Placement Portal prototype that helps the Training and Placement Cell approach companies and publish placement-drive details such as job profile, eligibility criteria, package, visit date, schedule, notices, and application links for students.

Authentication, database persistence, real company onboarding, admin approval workflows, email notifications, and production application processing are planned for future development.

## Future Scope


## Intended Users


## Disclaimer

This project is an academic/prototype implementation created for demonstration and presentation purposes. It is not an official production portal of DDUGU or IET unless separately deployed and authorized by the institution.

## License

No license has been specified yet. Add a license before distributing or accepting external contributions.
