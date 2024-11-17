# Project README for EcoGauge

This repository contains the codebase for the EcoGauge project, a data-driven application designed to explore and analyze vehicle fuel economy and environmental metrics.

## Directory Structure

### 1. **AdminPanel**
- Contains administrative tools and features for managing backend operations.
- Likely includes functionality for handling user accounts, data ingestion, and monitoring.

### 2. **MobileApp**
- The primary Flutter application codebase for EcoGauge.
- Features include:
  - Interactive graphs for data visualization.
  - Chatbot integration (Miles and Finn).
  - Dynamic query processing for vehicle metrics.

### 3. **toyota_ecogauge**
- Includes project resources and supporting assets.
- Likely contains shared components, libraries, or additional configurations for the project.

## Setup Instructions

### Prerequisites
- **Flutter SDK**: Ensure you have the latest Flutter SDK installed for the MobileApp.
- **Flask/Backend Environment**: Required for the AdminPanel (if applicable).

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-link>
   cd EcoGauge
   ```
2. **Setup MobileApp**
   ```cd MobileApp
   flutter pub get
   flutter run
   ```
3. **Setup AdminPanel**
   ```cd AdminPanel
   npm install
   npm start
   ```
### Additional Configuration
- Check the toyota_ecogauge directory for any specific assets or configuration files that need to be integrated into the MobileApp or AdminPanel.

### License
- This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgement
- Special thanks to contributors and the open-source community for their support.
