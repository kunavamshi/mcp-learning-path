#!/usr/bin/env python3
"""
Simple deployment script for MCP Learning Path Generator
Works on any platform: Vercel, Heroku, Railway, Render, etc.
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False
    return True

def run_app():
    """Run the Streamlit app"""
    print("🚀 Starting the app...")
    try:
        # Set Streamlit config for deployment
        os.environ["STREAMLIT_SERVER_PORT"] = "8501"
        os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"
        os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
        
        subprocess.check_call([sys.executable, "-m", "streamlit", "run", "app.py"])
    except subprocess.CalledProcessError:
        print("❌ Failed to start the app")
        return False
    return True

def main():
    print("🚀 MCP Learning Path Generator - Deployment Script")
    print("=" * 50)
    
    if not install_dependencies():
        sys.exit(1)
    
    print("\n🎯 Ready to deploy!")
    print("The app will start automatically...")
    
    if not run_app():
        sys.exit(1)

if __name__ == "__main__":
    main()
