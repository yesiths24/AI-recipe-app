# SnapCook - AI Recipe App

An AI-powered recipe finder that uses computer vision to identify food items from camera images and suggests delicious recipes.

## Features
- Camera integration for capturing food images
- AI-powered food item recognition using OpenAI's GPT-4 Vision
- Recipe suggestions based on identified ingredients
- Modern, responsive web interface built with Tailwind CSS

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Backend**: Python Flask API
- **AI**: OpenAI GPT-4 Vision API
- **Deployment**: Vercel

## Setup

### Prerequisites
- Python 3.x
- Node.js (for Tailwind CSS)
- OpenAI API key

### Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd AI-recipe-app
```

2. Install Python dependencies
```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies
```bash
npm install
```

4. Set up environment variables
```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

5. Build Tailwind CSS
```bash
npx tailwindcss -i src/input.css -o src/output.css --watch
```

6. Run the application locally
```bash
python api/foodItemsAndRecipesFinder.py
```

## Deployment
This app is configured for deployment on Vercel with the included `vercel.json` configuration.

## Usage
1. Open the app in your browser
2. Allow camera permissions
3. Point your camera at food items
4. Click the capture button
5. Wait for AI analysis and recipe suggestions