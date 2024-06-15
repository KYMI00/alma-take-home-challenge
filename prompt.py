
prompt = {
    "award": 
    "You are an expert award extraction algorithm designed to parse key CV details." +\
    "Please accurately extract the following information from the text." +\
    "- Task: Identify awards and categorize them as 'international' or 'national' based on specific keywords including 'Distinction', 'Laurels', and 'Prize'." +\
    "- Keywords:"+\
    "- International: 'International', 'Global', 'World', 'Universal', 'Intercontinental'"+\
    "- National: 'National', 'Countrywide', 'Federal', 'Nationwide'"+\
    "- Output: Dictionary with keys as 'international' and 'national', and values as summary sentences of the awards."+\
    "- Example Input (Assume it comes from John's CV):"+\
    "- Text: " +\
    "- National Achievement Scholarship"+\
    "- International Achievement Award"+\
    "- Example Output:" +\
    "- {'International': ['John has earned the International Achievement Award'], 'National': ['John has won the National Achievement Scholarship']}" +\
    "This is the text: ",

    "membership":
    "You are an expert membership extraction algorithm designed to parse key CV details." +\
    "Please accurately extract the following information from the text." +\
    "- Task: Detect membership affiliations using keywords like 'Member', 'Fellow'." +\
    "- Output: Python list of descriptive sentences summarizing the memberships mentioned in the CV." +\
    "- Example Input (Assume it comes from John's CV):" +\
    "- Text: 'PROFESSIONAL MEMBERSHIPS: INFORMS, Institute for Operations Research and Management Science; SIAM, Society for Industrial and Applied Mathematics.'" +\
    "- Example Output:" +\
    "- ['John is a member of INFORMS, Institute for Operations Research and Management Science', 'John is a member of SIAM, Society for Industrial and Applied Mathematics']" +\
    "- Please return an empty python list ('[]') if no related information is provided." +\
    "This is the text: ",

    "press":
    "You are an expert information extraction algorithm designed to parse key CV details." +\
    "Please accurately extract the following information from the text." +\
    "- Task: Locate mentions of involvement in competitions or public media." +\
    "- Output: Python list of descriptive sentences summarizing the press mentions." +\
    "- Please return an empty python list ('[]') if no related information is provided." +\
    "This is the text: ",

    "judge":
    "You are an expert information extraction algorithm designed to parse key CV details." +\
    "Please accurately extract the following information from the text." +\
    "- Task: Detect if the person has served as a judge for certain events, using keywords such as 'judge', 'reviewer', or 'judger'." +\
    "- Output: Python list of descriptive sentences about their judging experiences." +\
    "- Please return an empty python list ('[]') if no related information is provided." +\
    "This is the text: ",

    "original_contribution":
    "You are an expert information extraction algorithm designed to parse key CV details." +\
    "Please accurately extract the following information from the text." +\
    "- Task: Identify significant contributions such as books or patents." +\
    "- Output: Python list of descriptive sentences about each contribution." +\
    "- Please return an empty python list ('[]') if no related information is provided." +\
    "This is the text: ",

    "paper":
    "You are an expert information extraction algorithm designed to parse key CV details." +\
    "Please accurately extract the following information from the text." +\
    "- Task: Detect any scholarly articles published by the person." +\
    "- Output: Python list containing the names of the scholarly articles." +\
    "- Example Input: " +\
    "E. Brock, L. Bruckstein, P. Connor, S. Nguyen, R. Kerestes, and M. Abdelhakim, 'An application of reinforcement learning to residential energy storage under real-time pricing,' 2021 IEEE PES Innovative Smart Grid Technologies Asia (ISGT-Asia), 2021. Available online here." +\
    "J. Zhang, E. Brock, Y. Ye, and J. Zhang, 'A Parallel Computing Infrastructure for Building Energy Simulation,' Pacific Northwest National Laboratory, 2020. Available online here." +\
    "E. Brock, S. Nguyen, K. Kelly, and R. Kerestes, 'Evaluating carbon reduction strategies for the University of Pittsburgh,' Ingenium: Undergraduate Research at the Swanson School of Engineering, 2020. Available online here." +\
    "- Example Output: [" +\
    "'An application of reinforcement learning to residential energy storage under real-time pricing', " +\
    "'A Parallel Computing Infrastructure for Building Energy Simulation', " +\
    "'Evaluating carbon reduction strategies for the University of Pittsburgh']" +\
    "- Please return an empty python list ('[]') if no related information is provided." +\
    "This is the text: ",

    "job_title":
    "You are an expert information extraction algorithm designed to parse key CV details." +\
    "Please accurately extract the following information from the text." +\
    "- Task: Identify high-ranking positions within organizations using indicators like 'dean', 'senior', and 'executive'." +\
    "- Output: Python list of descriptive sentences about the positions held." +\
    "- Example Input (Assume it comes from John's CV):" +\
    "- Text: 'Chief Executive Officer, XYZ Corp; Distinguished Professor, ABC University.'" +\
    "- Example Output:" +\
    "- ['John is the Chief Executive Officer at XYZ Corp', 'John was previously a Distinguished Professor at ABC University']" +\
    "- Please return an empty python list ('[]') if no related information is provided." +\
    "This is the text: " ,
    
}