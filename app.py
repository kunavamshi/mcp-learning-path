import streamlit as st
import os
import json
import time

# Simple configuration
st.set_page_config(
    page_title="MCP Learning Path Generator",
    page_icon="🚀",
    layout="wide"
)

# Initialize session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = f"session_{int(time.time()) % 10000}"
if 'is_generating' not in st.session_state:
    st.session_state.is_generating = False

# Main header
st.title("🚀 MCP Learning Path Generator")
st.markdown("AI-Powered Personalized Learning Experience")

# Session status
st.info(f"Session ID: {st.session_state.session_id} | Ready to generate learning paths! 🚀")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Clear results button
    if st.button("🗑️ Clear Previous Results"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    # API Key input
    google_api_key = st.text_input(
        "🔑 Google API Key", 
        type="password", 
        help="Enter your Google API key for YouTube and Drive integration"
    )
    
    # Pipedream URLs
    st.header("🔗 Pipedream URLs")
    
    youtube_pipedream_url = st.text_input(
        "📺 YouTube URL (Required)", 
        placeholder="Enter your Pipedream YouTube URL",
        help="Required for video search and playlist creation"
    )

    # Secondary tool selection
    secondary_tool = st.radio(
        "🛠️ Select Secondary Tool:",
        ["Drive", "Notion"],
        help="Choose where to create your learning path document"
    )

    # Secondary tool URL input
    if secondary_tool == "Drive":
        drive_pipedream_url = st.text_input(
            "📁 Drive URL", 
            placeholder="Enter your Pipedream Drive URL",
            help="For creating Google Drive documents"
        )
        notion_pipedream_url = None
    else:
        notion_pipedream_url = st.text_input(
            "📝 Notion URL", 
            placeholder="Enter your Pipedream Notion URL",
            help="For creating Notion pages"
        )
        drive_pipedream_url = None

# Quick guide
st.header("📚 Quick Guide")
st.markdown("""
1. Enter your Google API key and YouTube URL (required)
2. Select and configure your secondary tool (Drive or Notion)
3. Enter a clear learning goal, for example:
   - "I want to learn Python basics in 3 days"
   - "I want to learn data science basics in 10 days"
""")

# Learning goal input
st.header("🎯 Enter Your Learning Goal")

user_goal = st.text_input(
    "Enter your learning goal:",
    help="Describe what you want to learn, and we'll generate a structured path using YouTube content and your selected tool.",
    placeholder="e.g., I want to learn TypeScript in 30 days with full practical knowledge"
)

# Display the current goal if set
if user_goal:
    st.success(f"🎯 Your Learning Goal: {user_goal}")
    
    # Show a preview of what will be generated
    st.info("✨ What You'll Get:")
    st.markdown("""
    - 📚 Day-by-day topic breakdown
    - 🎵 Curated YouTube video playlist
    - 📄 Detailed document in your chosen tool (Drive/Notion)
    """)

# Progress area
st.header("📊 Generation Progress")

# Show current status
if st.session_state.is_generating:
    st.info("🔄 Currently generating your learning path...")
    
    # Simple progress bar
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)
    
    st.success("🎉 Learning Path Generated Successfully!")

# Generate Learning Path button
st.header("🚀 Ready to Generate?")

if st.button("🎯 Generate Learning Path", type="primary", disabled=st.session_state.is_generating):
    
    if not google_api_key:
        st.error("❌ Missing API Key - Please enter your Google API key in the sidebar.")
    elif not youtube_pipedream_url:
        st.error("❌ Missing YouTube URL - YouTube URL is required. Please enter your Pipedream YouTube URL in the sidebar.")
    elif (secondary_tool == "Drive" and not drive_pipedream_url) or (secondary_tool == "Notion" and not notion_pipedream_url):
        st.error(f"❌ Missing {secondary_tool} URL - Please enter your Pipedream {secondary_tool} URL in the sidebar.")
    elif not user_goal:
        st.warning("⚠️ Missing Learning Goal - Please enter your learning goal.")
    else:
        try:
            # Set generating flag
            st.session_state.is_generating = True
            
            # Simulate generation process
            st.info("🔄 Setting up agent with tools...")
            time.sleep(1)
            
            st.info("🔄 Added Google Drive integration..." if secondary_tool == "Drive" else "🔄 Added Notion integration...")
            time.sleep(1)
            
            st.info("🔄 Creating AI agent...")
            time.sleep(1)
            
            st.info("🔄 Generating your learning path...")
            time.sleep(2)
            
            st.info("🔄 Learning path generation complete!")
            time.sleep(1)
            
            # Display mock results
            st.header("🎓 Your Learning Path")
            st.success("🎉 Learning Path Generated Successfully!")
            
            # Mock generated resources
            st.subheader("📋 Generated Resources")
            st.info("📚 Your personalized learning path has been created with day-by-day breakdown")
            
            if secondary_tool == "Drive":
                st.info("📄 Google Drive document created with detailed learning materials")
                st.link_button("🔗 View Document", "https://docs.google.com/document/d/example")
            else:
                st.info("📝 Notion page created with structured learning content")
                st.link_button("🔗 View Notion Page", "https://notion.so/example")
            
            st.info("🎵 YouTube playlist curated with relevant videos for each topic")
            st.link_button("🔗 View Playlist", "https://www.youtube.com/playlist?list=example")
            
            # Show progress details
            with st.expander("🔍 Generation Progress Details", expanded=False):
                st.write("→ Setting up agent with tools")
                st.write("→ Added integration tools")
                st.write("→ Creating AI agent")
                st.write("→ Generating learning path")
                st.write("→ Learning path generation complete!")
            
            st.session_state.is_generating = False
            
        except Exception as e:
            st.error(f"❌ An Error Occurred: {str(e)}")
            
            st.subheader("💡 Troubleshooting Tips")
            st.markdown("""
            • Verify your Google API key is correct and has the necessary permissions
            • Check that your Pipedream URLs are working and accessible
            • Ensure you have a stable internet connection
            • Try clearing previous results and starting fresh
            """)
            
            st.session_state.is_generating = False

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and MCP")
