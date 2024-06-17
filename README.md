# alma-take-home-challenge

This repository contains a system for processing PDF CVs using FastAPI and integrating with Azure OpenAI. The system evaluates candidates for O1-A visa qualification by parsing their CVs, generating prompts, and producing a final score along with supporting evidence.

## Project Structure

- `app.py`: Uses FastAPI to create a web API for the RAG (Retrieval-Augmented Generation) system.
- `assessment.py`: The final module that calls `pdfparser` and `openai_client` to process PDF CVs into text. It combines prompts with the parsed text and feeds them into the assessor to output the final score and supporting evidence.
- `base.py`: Acts as the parent node where the final score of the candidate, their supporting evidence for O1-A qualification, and the parsed PDF text are saved and updated.
- `config.py`: Contains the parameters needed to connect to Azure OpenAI.
- `openai_client.py`: Defines the connection with Azure OpenAI, uses the GPT model to process the text of PDFs, and combines it with corresponding prompts to generate the final combined prompt.
- `pdfparser.py`: Parses PDF CVs into text for better processing. The results are updated in `base.py` as a child node.
- `prompt.py`: Contains the prompts designed for each O1-A visa criterion to evaluate candidates based on their uploaded CVs.

## Criteria Evaluation

For all seven different criteria (except for salary), individual prompts are designed in `prompt.py`. The overall thinking process for evaluating these criteria is as follows:

1. **Determine the Level of Each Criteria**: Identify the level of achievement for each criterion. For example, for awards, we look at the level and number of the awards comprehensively.
2. **Calculate Scores**: Use different coefficients to calculate the final score for each specific field.
3. **Combine Scores**: Combine the scores for each criterion. Based on the number of high, medium, and low scores, determine the candidate's overall chances of passing the O1-A visa evaluation.

### Detailed Implementation

Note: Each criterion will be marked as either "high", medium", or "low" based on what we identified in their CV. 

- **Award**:
  - Identify the level of the award. If any international awards are identified, the candidate is directly marked as "high".
  - If only national awards are present, count the number of national awards and calculate a score for the final award level with my designed threshold.

- **Membership**:
  - Evaluate the level of organization and membership type to determine the score.
 
- **Other Criteria (e.g., Press, Judging, Scholarly Articles, Original Contribution, Job Titles)**:
  - For these criteria, count their appearances due to time constraints.
  - **Press**: The number of competitions and corporate social media work will be used to evaluate their press exposure.
  - **Judging**: The number of reviewing experiences identified.
  - **Scholarly Articles**: The number of papers published.
  - **Original Contribution**: The number of books or patents they have published and filed.
  - **Job Titles**: Very important job titles are indicated by keywords such as senior, dean, chief, and executive.

### Summary

The system uses the number of high, medium, and low scores across all criteria to classify candidates into high, medium, and low chances of passing the O1-A visa evaluation.

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Azure OpenAI credentials

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/rag-system.git
   cd rag-system
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up your Azure OpenAI credentials in `config.py`.

### Running the Application

To start the FastAPI server, run:

```sh
uvicorn app:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### Usage

1. Upload a PDF CV using the provided endpoint.
2. The system will parse the PDF into text.
3. Prompts will be generated based on the O1-A visa criteria.
4. The combined prompt will be sent to the OpenAI model to evaluate the candidate.
5. The final score and supporting evidence will be returned and stored.
