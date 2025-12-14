# Structural Damage Analysis AI 🏗️

A powerful AI-powered web application that detects structural damage (cracks, corrosion, wear) in real-time using your mobile camera or uploaded images. Powered by **FastAPI** and **Google Gemini 2.0 Flash**.

![App Screenshot](https://via.placeholder.com/800x400?text=App+Screenshot+Placeholder) 
*(Replace this with a real screenshot if you have one)*

## 🌟 Features

*   **Real-time Analysis**: Instant feedback on structural integrity.
*   **Dual Input**: Use your device's camera or upload existing photos.
*   **Detailed Reports**:
    *   **Damage Score** (0-10)
    *   **Safety Rating** (Safe / Caution / Danger)
    *   **Identified Issues** (Specific cracks, spalling, etc.)
    *   **Maintenance Suggestions** (Actionable repair steps)
*   **Premium UI**: Modern "Glassmorphism" design with dark mode.
*   **Mobile First**: Optimized for use on smartphones and tablets.

## 🚀 Tech Stack

*   **Backend**: FastAPI (Python)
*   **AI Model**: Google Gemini 2.0 Flash
*   **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript
*   **Containerization**: Docker & Docker Compose

## 🛠️ Local Setup

### Prerequisites
*   Docker Desktop installed.
*   A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/)).

### Steps
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/moiz2405/StructureAI.git
    cd StructureAI
    ```

2.  **Set your API Key**:
    Create a `.env` file in the root directory:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

3.  **Run with Docker**:
    ```bash
    docker-compose up --build
    ```

4.  **Access the App**:
    Open `http://localhost:8000` in your browser.

## 📱 Mobile Usage (Local)

To use this on your phone while running locally on your PC, you need a secure tunnel (HTTPS).

**Option 1: Pinggy (Easiest)**
Run this command in your terminal:
```bash
ssh -p 443 -R0:localhost:8000 a.pinggy.io
```
Open the generated URL on your phone.

**Option 2: VS Code Port Forwarding**
If using VS Code, go to the "Ports" tab, right-click port 8000, and select "Port Forwarding".

## ☁️ Deployment (Render.com)

This project is ready for 1-click deployment on Render.

1.  Push your code to GitHub (you've already done this!).
2.  Go to [Render.com](https://render.com) and create a new **Web Service**.
3.  Connect your GitHub repository (`moiz2405/StructureAI`).
4.  Select **Docker** as the runtime.
5.  **Important**: Scroll down to "Environment Variables" and add:
    *   Key: `GOOGLE_API_KEY`
    *   Value: `your_actual_api_key`
6.  Click **Create Web Service**.

Render will build and deploy your app. You'll get a permanent URL like `https://structure-ai.onrender.com`.

## 📄 License

MIT License. Free to use for educational and commercial purposes.
