# MCP Learning Path Generator

A Streamlit application that generates personalized learning paths using AI and various integrations (YouTube, Google Drive, Notion).

## 🚀 Features

- **AI-Powered Learning Path Generation**: Creates comprehensive day-by-day learning plans
- **YouTube Integration**: Automatically curates relevant video playlists
- **Google Drive Integration**: Creates detailed documents with learning content
- **Notion Integration**: Alternative document creation option
- **Progress Tracking**: Real-time progress updates during generation
- **Clean UI**: Improved user interface with better result display

## 🛠️ Recent Improvements

- ✅ **Fixed Import Errors**: Resolved `langchain_core` and `langgraph` dependency issues
- ✅ **Cleaner Output**: Filtered out intermediate progress messages for cleaner results
- ✅ **Better Progress Display**: Clear status indicators and progress tracking
- ✅ **Session Management**: Clear previous results button and session tracking
- ✅ **Enhanced Error Handling**: Better error messages and troubleshooting tips
- ✅ **Improved UI**: Better organization and user feedback

## 📋 Requirements

```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**:
   ```bash
   streamlit run app.py
   ```

3. **Configure API Keys**:
   - Add your Google API key
   - Configure Pipedream URLs for YouTube and Drive/Notion

4. **Generate Learning Path**:
   - Enter your learning goal
   - Click "Generate Learning Path"
   - Wait for the AI to create your personalized plan

## 🔧 Configuration

### Required:
- **Google API Key**: For YouTube and Drive integration
- **YouTube Pipedream URL**: For video search and playlist creation

### Optional:
- **Google Drive Pipedream URL**: For document creation
- **Notion Pipedream URL**: Alternative to Drive

## 📱 Usage

1. **Enter Learning Goal**: Describe what you want to learn (e.g., "I want to learn TypeScript in 30 days")
2. **Select Tools**: Choose between Google Drive or Notion for document creation
3. **Generate**: Click the button and wait for your personalized learning path
4. **Access Results**: Get links to your document and YouTube playlist

## 🎯 Example Goals

- "I want to learn Python basics in 3 days"
- "I want to learn data science fundamentals in 10 days"
- "I want to master React in 21 days"
- "I want to learn machine learning in 30 days"

## 🚨 Troubleshooting

### Common Issues:
- **Import Errors**: Make sure all dependencies are installed correctly
- **API Errors**: Verify your API keys and Pipedream URLs
- **Slow Generation**: The AI needs time to research and create content

### Solutions:
- Use the "Clear Previous Results" button to start fresh
- Check your internet connection
- Verify API key permissions

## 🌐 Deployment

### Streamlit Cloud (Recommended):
```bash
streamlit deploy
```

### Other Platforms:
- **Vercel**: Limited Python support
- **Netlify**: Limited Python support  
- **GitHub Pages**: Static sites only
- **Heroku/Railway**: Full Python support

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── utils.py            # Core logic and agent functions
├── prompt.py           # AI prompts and instructions
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment config
├── netlify.toml        # Netlify deployment config
├── .github/workflows/  # GitHub Actions for deployment
└── DEPLOYMENT.md       # Detailed deployment guide
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your configuration
3. Try clearing previous results
4. Check the deployment guide for platform-specific issues

---

**Happy Learning! 🎓✨**
