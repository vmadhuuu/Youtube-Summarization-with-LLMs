# **LLM-based YouTube Video Summarization and Question-Answering System**

This project builds a **Natural Language Processing (NLP)** system to extract and summarize YouTube video transcripts and provide detailed answers to user queries. Leveraging **T5** and **RoBERTa models**, it integrates external knowledge through APIs like **YouTube Transcript, Wikipedia**, and **Google Generative AI**, deployed via a user-friendly **Streamlit interface**.

---

## **Features**
- **Summarization**: Extract and generate concise summaries of YouTube video transcripts using **T5** and **RoBERTa models**.
- **Question Answering**: Provides detailed answers to user queries based on video content and external knowledge.
- **API Integration**: Uses **YouTube Transcript API**, **Wikipedia API**, and **Google Generative AI** for enhanced content understanding.
- **Web Application**: Deployed with Streamlit for an intuitive and interactive user interface.

---

## **Tech Stack**
- **Programming Language**: Python
- **Libraries**: 
  - NLP Models: T5, RoBERTa (Hugging Face Transformers)
  - APIs: YouTube Transcript API, Wikipedia API, Google Generative AI
  - Deployment: Streamlit
  - Data Processing: pandas, NumPy
- **Deployment**: Streamlit for front-end application

---

## **How to Run**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/youtube-summarization-qa.git
   cd youtube-summarization-qa
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the Web Application**:
   Open your browser and navigate to `http://127.0.0.1:8501`.

---

## **Workflow**
1. **Data Extraction**:
   - Extracts transcripts from YouTube videos using the **YouTube Transcript API**.
   
2. **Summarization**:
   - Summarizes transcripts using pre-trained **T5** and **RoBERTa** models.

3. **Question Answering**:
   - Integrates external knowledge via **Wikipedia API** and **Google Generative AI** for accurate responses.

4. **Deployment**:
   - Deployed via Streamlit for an interactive user experience.

---

## **Usage**
- Input a YouTube video URL into the application.
- View a concise summary and ask detailed questions related to the video content.

---

## **Results**
- Delivered concise summaries and accurate answers, enhancing user engagement with video content.
- Demonstrated robust integration of APIs to enrich content understanding.

---

## **Future Enhancements**
- Extend support for additional video platforms.
- Add advanced visualizations for content insights.
- Enhance model performance with larger pre-trained models.

---

## **Screenshots**
_Screenshots of the Streamlit interface, example outputs, and user interaction._

---

## **Contributors**
- [Madhumitha Venkatesan](https://github.com/vmadhuuu)

---

## **License**
This project is licensed under the MIT License.
