# 🤖 Multi-Agent Job Search System with CrewAI

An intelligent job application automation system that uses multiple AI agents to analyze job postings, tailor resumes, generate cover letters, and create personalized outreach messages for USAJobs listings.

## 🌟 Features

- **🔍 Smart Job Search**: Fetch job listings from USAJobs API with keyword and location filters
- **📋 JD Analysis**: AI-powered job description analysis to extract key requirements and qualifications
- **📝 Resume Tailoring**: Automatically customize resume summaries to match job requirements
- **✉️ Cover Letter Generation**: Create personalized cover letters for each application
- **📬 Outreach Messaging**: Generate professional email/LinkedIn messages for networking
- **📊 Application Tracking**: Log all applications and save generated documents
- **🖥️ Web Interface**: User-friendly Streamlit dashboard for easy interaction

## 🏗️ Architecture

The system uses **CrewAI** to orchestrate multiple specialized AI agents:

### 🤖 AI Agents

1. **JD Analyst Agent** - Analyzes job postings and extracts key information
2. **Resume & Cover Letter Writer** - Tailors application materials to match job descriptions  
3. **Outreach Messaging Specialist** - Creates professional networking messages

### 📁 Project Structure

```
job_hunt_assistant/
├── agents/                    # AI agent definitions
│   ├── jd_analyst.py         # Job description analysis agent
│   ├── resume_cl_agent.py    # Resume & cover letter agent
│   └── messaging_agent.py    # Outreach messaging agent
├── utils/                    # Utility modules
│   ├── config.py            # API keys and configuration
│   ├── tracking.py           # Application logging and file management
│   └── .env                 # Environment variables (API keys)
├── data/                     # Generated outputs and logs
│   ├── cover_letters/       # Generated cover letters
│   ├── applications_log.csv # Application tracking
│   └── sample_resume.txt    # Sample resume for testing
├── streamlit_app.py          # Web application interface
├── orchestrator.py           # Main workflow orchestration
├── usajobs_api.py           # USAJobs API integration
└── requirements.txt         # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API Key
- USAJobs API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/multi-agent-job-search-system.git
   cd multi-agent-job-search-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys**
   
   Create `utils/.env` file with your API keys:
   ```env
   USAJOBS_API_KEY=your_usajobs_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   **Getting API Keys:**
   - **Gemini API**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **USAJobs API**: Register at [USAJobs Developer Portal](https://developer.usajobs.gov/)

5. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

   Or use the provided batch file (Windows):
   ```bash
   run.bat
   ```

## 📖 Usage

### Via Web Interface

1. **Open the app**: Navigate to `http://localhost:8501`
2. **Search Jobs**: Enter job keywords and location
3. **Select Jobs**: Choose which positions to apply for
4. **Provide Resume**: Paste your current resume
5. **Add Bio**: Include a short professional bio for personalization
6. **Generate Applications**: Click "Apply to Selected Jobs" to generate:
   - Tailored resume summaries
   - Personalized cover letters
   - Professional outreach messages

### Generated Outputs

- **Resume summaries** optimized for each position
- **Cover letters** saved in `data/cover_letters/`
- **Outreach messages** for networking
- **Application log** in `data/applications_log.csv`

## 🔧 Configuration

### Customizing Agents

Edit agent configurations in the `agents/` directory:

- **Temperature**: Adjust creativity (0.0-1.0)
- **Models**: Change AI models in agent files
- **Prompts**: Modify task descriptions for different outputs

### API Settings

Update API configurations in `utils/config.py`:
```python
# Add additional API keys or settings
```

## 📊 Example Workflow

1. **Input**: "Business Analyst" jobs in "New York"
2. **Fetch**: 5 relevant job postings from USAJobs
3. **Analyze**: Each job description processed by JD Analyst
4. **Tailor**: Resume customized for each position
5. **Generate**: Cover letters and outreach messages
6. **Save**: All outputs stored with timestamps

## 🛠️ Technologies Used

- **CrewAI**: Multi-agent orchestration framework
- **Streamlit**: Web application framework
- **LangChain**: LLM integration and prompt management
- **Google Gemini**: AI model for content generation
- **USAJobs API**: Federal job listings
- **Python**: Core programming language

## 📝 Development

### Adding New Agents

1. Create new agent file in `agents/`
2. Define agent and task functions
3. Import and integrate in `orchestrator.py`

### Extending Functionality

- Add new job boards (LinkedIn, Indeed)
- Implement additional AI models
- Create email automation features
- Add interview preparation tools

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- **API Rate Limits**: Be mindful of USAJobs API rate limits
- **Data Privacy**: Store API keys securely and never commit them to version control
- **Quality Review**: Always review AI-generated content before sending
- **Professional Use**: Use generated materials as templates, personalize further for best results

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **API Failures**: Check API key validity and network connectivity
3. **Empty Outputs**: Verify resume text and job data are properly formatted
4. **Streamlit Issues**: Clear cache or restart the application

### Debug Mode

Enable verbose logging in agents:
```python
verbose=True  # In agent definitions
```

## 📞 Support

For questions, issues, or feature requests:
- Create an issue on GitHub
- Check the troubleshooting section
- Review agent logs for detailed error information

---

**Built with ❤️ using CrewAI and Streamlit**
