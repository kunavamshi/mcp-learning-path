import streamlit as st
from utils import run_agent_sync

st.set_page_config(page_title="MCP POC", page_icon="🤖", layout="wide")

# Main Header
st.title("🤖 MCP Learning Path Generator")
st.markdown("AI-Powered Personalized Learning Experience")

# Add a session status indicator
if 'session_id' not in st.session_state:
    st.session_state.session_id = f"session_{hash(str(id(st))) % 10000}"

st.info(f"Session ID: {st.session_state.session_id} | Ready to generate learning paths! 🚀")

# Initialize session state for progress
if 'current_step' not in st.session_state:
    st.session_state.current_step = ""
if 'progress' not in st.session_state:
    st.session_state.progress = 0
if 'last_section' not in st.session_state:
    st.session_state.last_section = ""
if 'is_generating' not in st.session_state:
    st.session_state.is_generating = False

# Sidebar for API and URL configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Clear results button
    if st.button("🗑️ Clear Previous Results", help="Clear all previous results and start fresh"):
        # Clear session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    # API Key input
    google_api_key = st.text_input("🔑 Google API Key", type="password", 
                                  help="Enter your Google API key for YouTube and Drive integration")
    
    # Pipedream URLs
    st.header("🔗 Pipedream URLs")
    
    youtube_pipedream_url = st.text_input("📺 YouTube URL (Required)", 
        placeholder="Enter your Pipedream YouTube URL",
        help="Required for video search and playlist creation")

    # Secondary tool selection
    secondary_tool = st.radio(
        "🛠️ Select Secondary Tool:",
        ["Drive", "Notion"],
        help="Choose where to create your learning path document"
    )

    # Secondary tool URL input
    if secondary_tool == "Drive":
        drive_pipedream_url = st.text_input("📁 Drive URL", 
            placeholder="Enter your Pipedream Drive URL",
            help="For creating Google Drive documents")
        notion_pipedream_url = None
    else:
        notion_pipedream_url = st.text_input("📝 Notion URL", 
            placeholder="Enter your Pipedream Notion URL",
            help="For creating Notion pages")
        drive_pipedream_url = None

# Quick guide before goal input
st.header("📚 Quick Guide")
st.markdown("""
1. Enter your Google API key and YouTube URL (required)
2. Select and configure your secondary tool (Drive or Notion)
3. Enter a clear learning goal, for example:
   - "I want to learn python basics in 3 days"
   - "I want to learn data science basics in 10 days"
""")

# Main content area
st.header("🎯 Enter Your Learning Goal")

user_goal = st.text_input("Enter your learning goal:",
                        help="Describe what you want to learn, and we'll generate a structured path using YouTube content and your selected tool.",
                        placeholder="e.g., I want to learn TypeScript in 30 days with full practical knowledge")

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

progress_container = st.container()
progress_bar = st.empty()

# Show current status
if st.session_state.current_step:
    st.info(f"🔄 Current Status: {st.session_state.current_step}")

def update_progress(message: str):
    """Update progress in the Streamlit UI"""
    st.session_state.current_step = message
    
    # Determine section and update progress
    if "Setting up agent with tools" in message:
        section = "Setup"
        st.session_state.progress = 0.1
    elif "Added Google Drive integration" in message or "Added Notion integration" in message:
        section = "Integration"
        st.session_state.progress = 0.2
    elif "Creating AI agent" in message:
        section = "Setup"
        st.session_state.progress = 0.3
    elif "Generating your learning path" in message:
        section = "Generation"
        st.session_state.progress = 0.5
    elif "Learning path generation complete" in message:
        section = "Complete"
        st.session_state.progress = 1.0
        st.session_state.is_generating = False
    else:
        section = st.session_state.last_section or "Progress"
    
    st.session_state.last_section = section
    
    # Show progress bar
    progress_percentage = int(st.session_state.progress * 100)
    progress_bar.progress(st.session_state.progress)
    st.write(f"Progress: {progress_percentage}%")
    
    # Update progress container with current status
    with progress_container:
        # Show section header if it changed
        if section != st.session_state.last_section and section != "Complete":
            st.subheader(f"{section}")
        
        # Show message with tick for completed steps
        if message == "Learning path generation complete!":
            st.success("🎉 All Steps Completed!")
        else:
            prefix = "✓" if st.session_state.progress >= 0.5 else "→"
            st.write(f"{prefix} {message}")

# Generate Learning Path button
st.header("🚀 Ready to Generate?")

if st.button("🎯 Generate Learning Path", type="primary", disabled=st.session_state.is_generating, 
             help="Click to generate your personalized learning path"):
    
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
            
            # Clear previous results completely
            if 'previous_result' in st.session_state:
                del st.session_state.previous_result
            if 'current_step' in st.session_state:
                del st.session_state.current_step
            if 'progress' in st.session_state:
                del st.session_state.progress
            if 'last_section' in st.session_state:
                del st.session_state.last_section
            
            # Reset progress
            st.session_state.current_step = ""
            st.session_state.progress = 0
            st.session_state.last_section = ""
            
            # Clear the page to remove old results
            st.empty()
            
            result = run_agent_sync(
                google_api_key=google_api_key,
                youtube_pipedream_url=youtube_pipedream_url,
                drive_pipedream_url=drive_pipedream_url,
                notion_pipedream_url=notion_pipedream_url,
                user_goal=user_goal,
                progress_callback=update_progress
            )
            
            # Store the new result
            st.session_state.previous_result = result
            
            # Display results
            st.header("🎓 Your Learning Path")
            
            if result and "messages" in result:
                # Show all messages but organize them better
                st.success("🎉 Learning Path Generated Successfully!")
                
                # Separate progress messages from final results
                progress_messages = []
                final_messages = []
                
                for msg in result["messages"]:
                    content = msg.content
                    # Categorize messages
                    if any(keyword in content.lower() for keyword in [
                        "learning path document link", 
                        "youtube playlist link",
                        "google docs",
                        "document link",
                        "playlist link",
                        "here is your learning path",
                        "here is your youtube playlist"
                    ]):
                        final_messages.append(msg)
                    else:
                        progress_messages.append(msg)
                
                # Show final results prominently
                if final_messages:
                    st.subheader("📋 Generated Resources")
                    
                    for msg in final_messages:
                        st.info(f"📚 {msg.content}")
                
                # Show progress messages in an expandable section
                if progress_messages:
                    with st.expander("🔍 Generation Progress Details", expanded=False):
                        for msg in progress_messages:
                            st.write(f"→ {msg.content}")
                
                # Extract and display links prominently
                content_text = " ".join([msg.content for msg in result["messages"]])
                
                # Look for Google Docs link
                if "docs.google.com" in content_text:
                    st.markdown("---")
                    st.subheader("📄 Google Drive Document")
                    import re
                    docs_match = re.search(r'https://docs\.google\.com/document/d/[a-zA-Z0-9_-]+', content_text)
                    if docs_match:
                        st.link_button("🔗 View Document", docs_match.group(0))
                
                # Look for YouTube playlist link
                if "youtube.com/playlist" in content_text:
                    st.subheader("🎵 YouTube Playlist")
                    playlist_match = re.search(r'https://www\.youtube\.com/playlist\?list=[a-zA-Z0-9_-]+', content_text)
                    if playlist_match:
                        st.link_button("🔗 View Playlist", playlist_match.group(0))
                
                # Show YouTube video suggestions if available
                if "youtube.com/watch" in content_text:
                    st.subheader("🎥 Suggested Videos")
                    video_matches = re.findall(r'https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]+', content_text)
                    if video_matches:
                        for i, video_url in enumerate(video_matches[:10], 1):  # Show first 10 videos
                            st.link_button(f"🎬 Video {i}", video_url)
                    
            else:
                st.error("❌ No Results Generated - Please try again or check your configuration.")
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
