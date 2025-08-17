# Deployment Guide for MCP Learning Path Generator

This guide will help you deploy your Streamlit application to Vercel, Netlify, and GitHub Pages.

## ⚠️ Important Note
**Streamlit applications cannot be directly deployed to Vercel, Netlify, or GitHub Pages** as these platforms are designed for static sites and Node.js applications. However, we've provided alternative solutions below.

## 🚀 Vercel Deployment

### Option 1: Static Site (Recommended)
1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. The `vercel.json` file will handle the routing.

### Option 2: Serverless Functions
Vercel supports Python serverless functions, but Streamlit requires a persistent server which isn't suitable.

## 🌐 Netlify Deployment

### Option 1: Static Site
1. Push your code to GitHub
2. Connect your repository to Netlify
3. Set build command: `echo "Static site ready"`
4. Set publish directory: `.`

### Option 2: Netlify Functions (Limited)
Netlify supports Python functions but not full Streamlit apps.

## 📚 GitHub Pages

1. Push your code to GitHub
2. Go to Settings > Pages
3. Select "GitHub Actions" as source
4. The workflow in `.github/workflows/deploy.yml` will automatically build and deploy

## 🔧 Alternative Deployment Solutions

### For Full Streamlit Functionality:

#### 1. Streamlit Cloud (Recommended)
```bash
# Install Streamlit
pip install streamlit

# Deploy to Streamlit Cloud
streamlit deploy
```

#### 2. Heroku
```bash
# Install Heroku CLI
# Create app
heroku create your-app-name

# Deploy
git push heroku main
```

#### 3. Railway
1. Connect your GitHub repository
2. Railway will automatically detect Python
3. Deploy with one click

#### 4. DigitalOcean App Platform
1. Connect your repository
2. Select Python as runtime
3. Deploy

## 📁 Files Created for Deployment

- `vercel.json` - Vercel configuration
- `netlify.toml` - Netlify configuration  
- `.github/workflows/deploy.yml` - GitHub Actions workflow
- `Procfile` - Process file for some platforms
- `runtime.txt` - Python version specification
- `DEPLOYMENT.md` - This deployment guide

## 🚨 Current Limitations

1. **Vercel**: No native Python/Streamlit support
2. **Netlify**: No native Python/Streamlit support  
3. **GitHub Pages**: Static sites only

## 💡 Recommendations

1. **For Development**: Use Streamlit Cloud (free tier available)
2. **For Production**: Use Heroku, Railway, or DigitalOcean
3. **For Static Demo**: Use the GitHub Pages workflow we created

## 🔄 Next Steps

1. Choose your preferred deployment platform
2. Follow the specific instructions above
3. Update the deployment URLs in the static HTML file
4. Test your deployment

## 📞 Need Help?

If you encounter issues:
1. Check the platform's documentation
2. Verify your Python version compatibility
3. Ensure all dependencies are properly specified
4. Consider using Streamlit Cloud for the easiest deployment
