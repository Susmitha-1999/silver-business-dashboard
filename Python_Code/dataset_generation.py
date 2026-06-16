import pandas as pd
import numpy as np
import random
from datetime import timedelta, date
import os

random.seed(42)
np.random.seed(42)

OUTPUT_DIR = "TRC_Silvers"
os.makedirs(OUTPUT_DIR, exist_ok=True)

GST_RATE = 3

unique_names = [
    "Arjun Murugesan","Karthik Krishnasamy","Murugan Govindaraj","Selvam Subramanian",
    "Rajan Palaniswamy","Suresh Venkatesan","Vijay Ramamoorthy","Balan Thangavel",
    "Ganesh Narayanan","Prakash Ponnusamy","Senthil Arumugam","Anand Subramaniam",
    "Kumar Elumalai","Ramesh Duraisamy","Arun Ganesan","Manoj Ramasamy",
    "Dinesh Muthukrishnan","Sathish Mariappan","Vignesh Selvaraj","Praveen Chinnaswamy",
    "Thilak Ayyappan","Gokul Balakrishnan","Saravanan Jayaraman","Prabhu Somasundaram",
    "Deepak Srinivasan","Rajesh Sundaram","Kamal Palanivel","Ashwin Sakthivel",
    "Surya Periyasamy","Bharath Soundararajan","Mani Rathinam","Shankar Marimuthu",
    "Venkat Shanmugam","Mohan Kaliyaperumal","Naresh Kupusamy","Pradeep Thirumeni",
    "Vasanth Murugesan","Balaji Krishnasamy","Muthu Govindaraj","Ezhil Subramanian",
    "Pandian Palaniswamy","Sekar Venkatesan","Arul Ramamoorthy","Durai Thangavel",
    "Natarajan Narayanan","Sivakumar Ponnusamy","Harish Arumugam","Priya Subramaniam",
    "Kavitha Elumalai","Meena Duraisamy","Saranya Ganesan","Deepa Ramasamy",
    "Lakshmi Muthukrishnan","Revathi Mariappan","Sudha Selvaraj","Anitha Chinnaswamy",
    "Viji Ayyappan","Parvathi Balakrishnan","Malathi Jayaraman","Radha Somasundaram",
    "Nirmala Srinivasan","Kamala Sundaram","Geetha Palanivel","Suganya Sakthivel",
    "Sangeetha Periyasamy","Divya Soundararajan","Nithya Rathinam","Pavithra Marimuthu",
    "Soundarya Shanmugam","Mythili Kaliyaperumal","Jayanthi Kupusamy","Sumathi Thirumeni",
    "Vijayalakshmi Murugesan","Kalaiselvi Krishnasamy","Indira Govindaraj","Thenmozhi Subramanian",
    "Selvi Palaniswamy","Ponni Venkatesan","Kala Ramamoorthy","Rajeswari Thangavel",
    "Bhuvana Narayanan","Amudha Ponnusamy","Gomathi Arumugam","Rani Subramaniam",
    "Arjun Elumalai","Karthik Duraisamy","Murugan Ganesan","Selvam Ramasamy",
    "Rajan Muthukrishnan","Suresh Mariappan","Vijay Selvaraj","Balan Chinnaswamy",
    "Ganesh Ayyappan","Prakash Balakrishnan","Senthil Jayaraman","Anand Somasundaram",
    "Kumar Srinivasan","Ramesh Sundaram","Arun Palanivel","Manoj Sakthivel",
    "Dinesh Periyasamy","Sathish Soundararajan","Vignesh Rathinam","Praveen Marimuthu",
    "Thilak Shanmugam","Gokul Kaliyaperumal","Saravanan Kupusamy","Prabhu Thirumeni",
    "Deepak Murugesan","Rajesh Krishnasamy","Kamal Govindaraj","Ashwin Subramanian",
    "Surya Palaniswamy","Bharath Venkatesan","Mani Ramamoorthy","Shankar Thangavel",
    "Venkat Narayanan","Mohan Ponnusamy","Naresh Arumugam","Pradeep Subramaniam",
    "Vasanth Elumalai","Balaji Duraisamy","Muthu Ganesan","Ezhil Ramasamy",
    "Pandian Muthukrishnan","Sekar Mariappan","Arul Selvaraj","Durai Chinnaswamy",
    "Natarajan Ayyappan","Sivakumar Balakrishnan","Harish Jayaraman","Priya Somasundaram",
    "Kavitha Srinivasan","Meena Sundaram","Saranya Palanivel","Deepa Sakthivel",
    "Lakshmi Periyasamy","Revathi Soundararajan","Sudha Rathinam","Anitha Marimuthu",
    "Viji Shanmugam","Parvathi Kaliyaperumal","Malathi Kupusamy","Radha Thirumeni",
    "Nirmala Murugesan","Kamala Krishnasamy","Geetha Govindaraj","Suganya Subramanian",
    "Sangeetha Palaniswamy","Divya Venkatesan","Nithya Ramamoorthy","Pavithra Thangavel",
    "Soundarya Narayanan","Mythili Ponnusamy","Jayanthi Arumugam","Sumathi Subramaniam",
    "Vijayalakshmi Elumalai","Kalaiselvi Duraisamy","Indira Ganesan","Thenmozhi Ramasamy",
    "Selvi Muthukrishnan","Ponni Mariappan","Kala Selvaraj","Rajeswari Chinnaswamy",
    "Bhuvana Ayyappan","Amudha Balakrishnan","Gomathi Jayaraman","Rani Somasundaram",
    "Arjun Srinivasan","Karthik Sundaram","Murugan Palanivel","Selvam Sakthivel",
    "Rajan Periyasamy","Suresh Soundararajan","Vijay Rathinam","Balan Marimuthu",
    "Ganesh Shanmugam","Prakash Kaliyaperumal","Senthil Kupusamy","Anand Thirumeni",
    "Kumar Murugesan","Ramesh Krishnasamy","Arun Govindaraj","Manoj Subramanian",
    "Dinesh Palaniswamy","Sathish Venkatesan","Vignesh Ramamoorthy","Praveen Thangavel",
    "Thilak Narayanan","Gokul Ponnusamy","Saravanan Arumugam","Prabhu Subramaniam",
    "Deepak Elumalai","Rajesh Duraisamy","Kamal Ganesan","Ashwin Ramasamy",
    "Surya Muthukrishnan","Bharath Mariappan","Mani Selvaraj","Shankar Chinnaswamy",
    "Venkat Ayyappan","Mohan Balakrishnan","Naresh Jayaraman","Pradeep Somasundaram",
    "Vasanth Srinivasan","Balaji Sundaram","Muthu Palanivel","Ezhil Sakthivel",
    "Pandian Periyasamy","Sekar Soundararajan","Arul Rathinam","Durai Marimuthu",
    "Natarajan Shanmugam","Sivakumar Kaliyaperumal","Harish Kupusamy","Priya Thirumeni",
    "Kavitha Murugesan","Meena Krishnasamy","Saranya Govindaraj","Deepa Subramanian",
    "Lakshmi Palaniswamy","Revathi Venkatesan","Sudha Ramamoorthy","Anitha Thangavel",
    "Viji Narayanan","Parvathi Ponnusamy","Malathi Arumugam","Radha Subramaniam",
    "Nirmala Elumalai","Kamala Duraisamy","Geetha Ganesan","Suganya Ramasamy",
    "Sangeetha Muthukrishnan","Divya Mariappan","Nithya Selvaraj","Pavithra Chinnaswamy",
    "Soundarya Ayyappan","Mythili Balakrishnan","Jayanthi Jayaraman","Sumathi Somasundaram",
    "Vijayalakshmi Srinivasan","Kalaiselvi Sundaram","Indira Palanivel","Thenmozhi Sakthivel",
    "Selvi Periyasamy","Ponni Soundararajan","Kala Rathinam","Rajeswari Marimuthu",
    "Bhuvana Shanmugam","Amudha Kaliyaperumal","Gomathi Kupusamy","Rani Thirumeni",
    "Arjun Narayanan","Karthik Ponnusamy","Murugan Arumugam","Selvam Subramaniam",
    "Rajan Elumalai","Suresh Duraisamy","Vijay Ganesan","Balan Ramasamy",
    "Ganesh Muthukrishnan","Prakash Mariappan","Senthil Selvaraj","Anand Chinnaswamy",
    "Kumar Ayyappan","Ramesh Balakrishnan","Arun Jayaraman","Manoj Somasundaram",
    "Dinesh Srinivasan","Sathish Sundaram","Vignesh Palanivel","Praveen Sakthivel",
    "Thilak Periyasamy","Gokul Soundararajan","Saravanan Rathinam","Prabhu Marimuthu",
    "Deepak Shanmugam","Rajesh Kaliyaperumal","Kamal Kupusamy","Ashwin Thirumeni",
    "Surya Murugesan","Bharath Krishnasamy","Mani Govindaraj","Shankar Subramanian",
    "Venkat Palaniswamy","Mohan Venkatesan","Naresh Ramamoorthy","Pradeep Thangavel",
    "Vasanth Narayanan","Balaji Ponnusamy","Muthu Arumugam","Ezhil Subramaniam",
    "Pandian Elumalai","Sekar Duraisamy","Arul Ganesan","Durai Ramasamy",
    "Natarajan Muthukrishnan","Sivakumar Mariappan","Harish Selvaraj","Priya Chinnaswamy",
    "Kavitha Ayyappan","Meena Balakrishnan","Saranya Jayaraman","Deepa Somasundaram",
    "Lakshmi Srinivasan","Revathi Sundaram","Sudha Palanivel","Anitha Sakthivel",
    "Viji Periyasamy","Parvathi Soundararajan","Malathi Rathinam","Radha Marimuthu",
    "Nirmala Shanmugam","Kamala Kaliyaperumal","Geetha Kupusamy","Suganya Thirumeni",
    "Sangeetha Narayanan","Divya Ponnusamy","Nithya Arumugam","Pavithra Subramaniam",
    "Soundarya Elumalai","Mythili Duraisamy","Jayanthi Ganesan","Sumathi Ramasamy",
    "Vijayalakshmi Muthukrishnan","Kalaiselvi Mariappan","Indira Selvaraj","Thenmozhi Chinnaswamy",
    "Selvi Ayyappan","Ponni Balakrishnan","Kala Jayaraman","Rajeswari Somasundaram",
    "Bhuvana Srinivasan","Amudha Sundaram","Gomathi Palanivel","Rani Sakthivel",
    "Arjun Periyasamy","Karthik Soundararajan","Murugan Rathinam","Selvam Marimuthu",
    "Rajan Shanmugam","Suresh Kaliyaperumal","Vijay Kupusamy","Balan Thirumeni",
    "Ganesh Murugesan","Prakash Krishnasamy","Senthil Govindaraj","Anand Subramanian",
    "Kumar Palaniswamy","Ramesh Venkatesan","Arun Ramamoorthy","Manoj Thangavel",
    "Dinesh Narayanan","Sathish Ponnusamy","Vignesh Arumugam","Praveen Subramaniam",
    "Thilak Elumalai","Gokul Duraisamy","Saravanan Ganesan","Prabhu Ramasamy",
    "Deepak Muthukrishnan","Rajesh Mariappan","Kamal Selvaraj","Ashwin Chinnaswamy",
    "Surya Ayyappan","Bharath Balakrishnan","Mani Jayaraman","Shankar Somasundaram",
    "Venkat Srinivasan","Mohan Sundaram","Naresh Palanivel","Pradeep Sakthivel",
    "Vasanth Periyasamy","Balaji Soundararajan","Muthu Rathinam","Ezhil Marimuthu",
    "Pandian Shanmugam","Sekar Kaliyaperumal","Arul Kupusamy","Durai Thirumeni",
    "Natarajan Murugesan","Sivakumar Krishnasamy","Harish Govindaraj","Priya Subramanian",
    "Kavitha Palaniswamy","Meena Venkatesan","Saranya Ramamoorthy","Deepa Thangavel",
    "Lakshmi Narayanan","Revathi Ponnusamy","Sudha Arumugam","Anitha Subramaniam",
    "Viji Elumalai","Parvathi Duraisamy","Malathi Ganesan","Radha Ramasamy",
    "Nirmala Muthukrishnan","Kamala Mariappan","Geetha Selvaraj","Suganya Chinnaswamy",
    "Sangeetha Ayyappan","Divya Balakrishnan","Nithya Jayaraman","Pavithra Somasundaram",
    "Soundarya Srinivasan","Mythili Sundaram","Jayanthi Palanivel","Sumathi Sakthivel",
    "Vijayalakshmi Periyasamy","Kalaiselvi Soundararajan","Indira Rathinam","Thenmozhi Marimuthu",
    "Selvi Shanmugam","Ponni Kaliyaperumal","Kala Kupusamy","Rajeswari Thirumeni",
    "Bhuvana Murugesan","Amudha Krishnasamy","Gomathi Govindaraj","Rani Subramanian",
    "Arjun Venkatesan","Karthik Ramamoorthy","Murugan Thangavel","Selvam Narayanan",
    "Rajan Ponnusamy","Suresh Arumugam","Vijay Subramaniam","Balan Elumalai",
    "Ganesh Duraisamy","Prakash Ganesan","Senthil Ramasamy","Anand Muthukrishnan",
    "Kumar Mariappan","Ramesh Selvaraj","Arun Chinnaswamy","Manoj Ayyappan",
    "Dinesh Balakrishnan","Sathish Jayaraman","Vignesh Somasundaram","Praveen Srinivasan",
    "Thilak Sundaram","Gokul Palanivel","Saravanan Sakthivel","Prabhu Periyasamy",
    "Deepak Soundararajan","Rajesh Rathinam","Kamal Marimuthu","Ashwin Shanmugam",
    "Surya Kaliyaperumal","Bharath Kupusamy","Mani Thirumeni","Shankar Murugesan",
    "Venkat Krishnasamy","Mohan Govindaraj","Naresh Subramanian","Pradeep Palaniswamy",
    "Vasanth Venkatesan","Balaji Ramamoorthy","Muthu Thangavel","Ezhil Narayanan",
    "Pandian Ponnusamy","Sekar Arumugam","Arul Subramaniam","Durai Elumalai",
    "Natarajan Duraisamy","Sivakumar Ganesan","Harish Ramasamy","Priya Muthukrishnan",
    "Kavitha Mariappan","Meena Selvaraj","Saranya Chinnaswamy","Deepa Ayyappan",
    "Lakshmi Balakrishnan","Revathi Jayaraman","Sudha Somasundaram","Anitha Srinivasan",
    "Viji Sundaram","Parvathi Palanivel","Malathi Sakthivel","Radha Periyasamy",
    "Nirmala Soundararajan","Kamala Rathinam","Geetha Marimuthu","Suganya Shanmugam",
    "Sangeetha Kaliyaperumal","Divya Kupusamy","Nithya Thirumeni","Pavithra Murugesan",
    "Soundarya Krishnasamy","Mythili Govindaraj","Jayanthi Subramanian","Sumathi Palaniswamy",
    "Vijayalakshmi Venkatesan","Kalaiselvi Ramamoorthy","Indira Thangavel","Thenmozhi Narayanan",
    "Selvi Ponnusamy","Ponni Arumugam","Kala Subramaniam","Rajeswari Elumalai",
    "Bhuvana Duraisamy","Amudha Ganesan","Gomathi Ramasamy","Rani Muthukrishnan",
    "Arjun Mariappan","Karthik Selvaraj","Murugan Chinnaswamy","Selvam Ayyappan",
    "Rajan Balakrishnan","Suresh Jayaraman","Vijay Somasundaram","Balan Srinivasan",
    "Ganesh Sundaram","Prakash Palanivel","Senthil Sakthivel","Anand Periyasamy",
    "Kumar Soundararajan","Ramesh Rathinam","Arun Marimuthu","Manoj Shanmugam",
    "Dinesh Kaliyaperumal","Sathish Kupusamy","Vignesh Thirumeni","Praveen Murugesan",
    "Thilak Krishnasamy","Gokul Govindaraj","Saravanan Subramanian","Prabhu Palaniswamy",
    "Deepak Venkatesan","Rajesh Ramamoorthy","Kamal Thangavel","Ashwin Narayanan",
    "Surya Ponnusamy","Bharath Arumugam","Mani Subramaniam","Shankar Elumalai",
    "Venkat Duraisamy","Mohan Ganesan","Naresh Ramasamy","Pradeep Muthukrishnan",
    "Vasanth Mariappan","Balaji Selvaraj","Muthu Chinnaswamy","Ezhil Ayyappan",
    "Pandian Balakrishnan","Sekar Jayaraman","Arul Somasundaram","Durai Srinivasan",
    "Natarajan Sundaram","Sivakumar Palanivel","Harish Sakthivel","Priya Periyasamy",
    "Kavitha Soundararajan","Meena Rathinam","Saranya Marimuthu","Deepa Shanmugam",
    "Lakshmi Kaliyaperumal","Revathi Kupusamy","Sudha Thirumeni","Anitha Murugesan",
    "Viji Krishnasamy","Parvathi Govindaraj","Malathi Subramanian","Radha Palaniswamy",
    "Nirmala Venkatesan","Kamala Ramamoorthy","Geetha Thangavel","Suganya Narayanan",
    "Sangeetha Ponnusamy","Divya Arumugam","Nithya Subramaniam","Pavithra Elumalai",
    "Soundarya Duraisamy","Mythili Ganesan","Jayanthi Ramasamy","Sumathi Muthukrishnan",
    "Vijayalakshmi Mariappan","Kalaiselvi Selvaraj","Indira Chinnaswamy","Thenmozhi Ayyappan",
    "Selvi Balakrishnan","Ponni Jayaraman","Kala Somasundaram","Rajeswari Srinivasan",
    "Bhuvana Sundaram","Amudha Palanivel","Gomathi Sakthivel","Rani Periyasamy",
    "Arjun Soundararajan","Karthik Rathinam","Murugan Marimuthu","Selvam Shanmugam",
    "Rajan Kaliyaperumal","Suresh Kupusamy","Vijay Thirumeni","Balan Murugesan",
    "Ganesh Krishnasamy","Prakash Govindaraj","Senthil Subramanian","Anand Palaniswamy",
    "Kumar Venkatesan","Ramesh Ramamoorthy","Arun Thangavel","Manoj Narayanan",
    "Dinesh Ponnusamy","Sathish Arumugam","Vignesh Subramaniam","Praveen Elumalai",
    "Thilak Duraisamy","Gokul Ganesan","Saravanan Ramasamy","Prabhu Muthukrishnan",
    "Deepak Mariappan","Rajesh Selvaraj","Kamal Chinnaswamy","Ashwin Ayyappan",
    "Surya Balakrishnan","Bharath Jayaraman","Mani Somasundaram","Shankar Srinivasan",
    "Venkat Sundaram","Mohan Palanivel","Naresh Sakthivel","Pradeep Periyasamy",
    "Vasanth Soundararajan","Balaji Rathinam","Muthu Marimuthu","Ezhil Shanmugam",
    "Pandian Kaliyaperumal","Sekar Kupusamy","Arul Thirumeni","Durai Murugesan",
    "Natarajan Krishnasamy","Sivakumar Govindaraj","Harish Subramanian","Priya Palaniswamy",
    "Kavitha Venkatesan","Meena Ramamoorthy","Saranya Thangavel","Deepa Narayanan",
    "Lakshmi Ponnusamy","Revathi Arumugam","Sudha Subramaniam","Anitha Elumalai",
    "Viji Duraisamy","Parvathi Ganesan","Malathi Ramasamy","Radha Muthukrishnan",
    "Nirmala Mariappan","Kamala Selvaraj","Geetha Chinnaswamy","Suganya Ayyappan",
    "Sangeetha Balakrishnan","Divya Jayaraman","Nithya Somasundaram","Pavithra Srinivasan",
    "Soundarya Sundaram","Mythili Palanivel","Jayanthi Sakthivel","Sumathi Periyasamy",
    "Vijayalakshmi Soundararajan","Kalaiselvi Rathinam","Indira Marimuthu","Thenmozhi Shanmugam",
    "Selvi Kaliyaperumal","Ponni Kupusamy","Kala Thirumeni","Rajeswari Murugesan",
    "Bhuvana Krishnasamy","Amudha Govindaraj","Gomathi Subramanian","Rani Palaniswamy",
    "Arjun Ramamoorthy","Karthik Thangavel","Murugan Narayanan","Selvam Ponnusamy",
    "Rajan Arumugam","Suresh Subramaniam","Vijay Elumalai","Balan Duraisamy",
    "Ganesh Ganesan","Prakash Ramasamy","Senthil Muthukrishnan","Anand Mariappan",
    "Kumar Selvaraj","Ramesh Chinnaswamy","Arun Ayyappan","Manoj Balakrishnan",
    "Dinesh Jayaraman","Sathish Somasundaram","Vignesh Srinivasan","Praveen Sundaram",
    "Thilak Palanivel","Gokul Sakthivel","Saravanan Periyasamy","Prabhu Soundararajan",
    "Deepak Rathinam","Rajesh Marimuthu","Kamal Shanmugam","Ashwin Kaliyaperumal",
    "Surya Kupusamy","Bharath Thirumeni","Mani Murugesan","Shankar Krishnasamy",
    "Venkat Govindaraj","Mohan Subramanian","Naresh Palaniswamy","Pradeep Venkatesan",
    "Vasanth Ramamoorthy","Balaji Thangavel","Muthu Narayanan","Ezhil Ponnusamy",
    "Pandian Arumugam","Sekar Subramaniam","Arul Elumalai","Durai Duraisamy",
    "Natarajan Ganesan","Sivakumar Ramasamy","Harish Muthukrishnan","Priya Mariappan",
    "Kavitha Selvaraj","Meena Chinnaswamy","Saranya Ayyappan","Deepa Balakrishnan",
    "Lakshmi Jayaraman","Revathi Somasundaram","Sudha Srinivasan","Anitha Sundaram",
    "Viji Palanivel","Parvathi Sakthivel","Malathi Periyasamy","Radha Soundararajan",
    "Nirmala Rathinam","Kamala Marimuthu","Geetha Shanmugam","Suganya Kaliyaperumal",
    "Sangeetha Kupusamy","Divya Thirumeni","Nithya Murugesan","Pavithra Krishnasamy",
    "Soundarya Govindaraj","Mythili Subramanian","Jayanthi Palaniswamy","Sumathi Venkatesan",
    "Vijayalakshmi Ramamoorthy","Kalaiselvi Thangavel","Indira Narayanan","Thenmozhi Ponnusamy",
    "Selvi Arumugam","Ponni Subramaniam","Kala Elumalai","Rajeswari Duraisamy",
    "Bhuvana Ganesan","Amudha Ramasamy","Gomathi Muthukrishnan","Rani Mariappan",
    "Sindhu Venkatesan","Keerthana Subramanian","Abinaya Palaniswamy","Kiruthika Ramamoorthy",
    "Nivetha Thangavel","Oviya Narayanan","Ranjitha Ponnusamy","Sharmila Arumugam",
    "Tamizharasi Subramaniam","Usha Elumalai","Vanitha Duraisamy","Yazhini Ganesan",
    "Abinav Ramasamy","Akash Muthukrishnan","Aakash Mariappan","Balamurugan Selvaraj",
    "Chandru Chinnaswamy","Dhanush Ayyappan","Elango Balakrishnan","Faisal Jayaraman",
    "Gowtham Somasundaram","Hari Srinivasan","Ilavarasan Sundaram","Jagan Palanivel",
    "Kannan Sakthivel","Logesh Periyasamy","Madhan Soundararajan","Nirmal Rathinam",
    "Oviyam Marimuthu","Prabu Shanmugam","Qadhar Kaliyaperumal","Rithish Kupusamy",
    "Stalin Thirumeni","Tharun Murugesan","Udayakumar Krishnasamy","Xavier Govindaraj",
    "Yokesh Subramanian","Zentil Palaniswamy","Aruna Venkatesan","Brindha Ramamoorthy",
    "Chandra Thangavel","Dharini Narayanan","Eswari Ponnusamy","Fathima Arumugam",
]

city_data = {
    "Coimbatore":   {"weight": 38, "state": "Tamil Nadu"},
    "Tiruppur":     {"weight": 12, "state": "Tamil Nadu"},
    "Erode":        {"weight":  9, "state": "Tamil Nadu"},
    "Salem":        {"weight":  7, "state": "Tamil Nadu"},
    "Pollachi":     {"weight":  7, "state": "Tamil Nadu"},
    "Mettupalayam": {"weight":  5, "state": "Tamil Nadu"},
    "Karur":        {"weight":  4, "state": "Tamil Nadu"},
    "Namakkal":     {"weight":  3, "state": "Tamil Nadu"},
    "Dharapuram":   {"weight":  3, "state": "Tamil Nadu"},
    "Chennai":      {"weight":  2, "state": "Tamil Nadu"},
    "Madurai":      {"weight":  2, "state": "Tamil Nadu"},
    "Bengaluru":    {"weight":  3, "state": "Karnataka"},
    "Hyderabad":    {"weight":  2, "state": "Telangana"},
    "Mumbai":       {"weight":  2, "state": "Maharashtra"},
    "Kochi":        {"weight":  1, "state": "Kerala"},
}

cities       = list(city_data.keys())
city_weights = [city_data[c]["weight"] for c in cities]

supplier_df = pd.DataFrame([
    ["SUP001", "BMC Silvers",             "Salem"],
    ["SUP002", "Neha Arts",               "Coimbatore"],
    ["SUP003", "BBC Silvers",             "Rajkot"],
    ["SUP004", "SS Plates",               "Salem"],
    ["SUP005", "Temple Crafts India",     "Kumbakonam"],
    ["SUP006", "Coimbatore Silver Works", "Coimbatore"],
], columns=["SupplierID", "SupplierName", "City"])

products_raw = [
    ["P001", "Kuttu Vilakku",  "80%",   "Temple",    700,  4500, 3,  "SUP005"],
    ["P002", "Anklet",         "80%",   "Jewellery",  28,   120, 3,  "SUP001"],
    ["P003", "Khusbhu Anklet", "80%",   "Jewellery",  32,   130, 3,  "SUP001"],
    ["P004", "S Chain",        "80%",   "Jewellery",  16,    60, 4,  "SUP003"],
    ["P005", "Karab Chain",    "80%",   "Jewellery",  18,    70, 4,  "SUP003"],
    ["P006", "Earring",        "80%",   "Jewellery",   3,    15, 3,  "SUP001"],
    ["P007", "Lion Kada",      "80%",   "Jewellery",  50,   140, 3,  "SUP001"],
    ["P008", "Plain Kaap",     "80%",   "Jewellery",  38,   120, 3,  "SUP001"],
    ["P009", "Metti",          "80%",   "Jewellery",   5,    15, 3,  "SUP001"],
    ["P010", "Ring",           "80%",   "Jewellery",   3,    12, 3,  "SUP001"],
    ["P011", "Kumkum Box",     "80%",   "Utility",    40,   150, 3,  "SUP006"],
    ["P012", "Glass",          "80%",   "Utility",   150,   450, 3,  "SUP006"],
    ["P013", "Plate",          "80%",   "Utility",   180,  1400, 3,  "SUP004"],
    ["P014", "Anklet",         "92.5%", "Jewellery",  45,   150, 9,  "SUP002"],
    ["P015", "Metti",          "92.5%", "Jewellery",   6,    22, 9,  "SUP002"],
    ["P016", "Kaap",           "92.5%", "Jewellery",  50,   160, 9,  "SUP002"],
    ["P017", "Chain",          "92.5%", "Jewellery",  25,    85, 10, "SUP003"],
    ["P018", "Ring",           "92.5%", "Jewellery",   4,    16, 9,  "SUP002"],
    ["P019", "Earring",        "92.5%", "Jewellery",   4,    18, 9,  "SUP002"],
    ["P020", "Kuttu Vilakku",  "92.5%", "Temple",    900,  5500, 10, "SUP005"],
    ["P021", "Plate",          "92.5%", "Utility",   250,  1800, 10, "SUP004"],
    ["P022", "Cow Idol",       "92.5%", "Temple",     80,   800, 10, "SUP005"],
    ["P023", "Glass",          "92.5%", "Utility",   180,   500, 10, "SUP006"],
    ["P024", "Purse",          "92.5%", "Utility",   120,   450, 10, "SUP006"],
]
product_df = pd.DataFrame(products_raw, columns=[
    "ProductID", "ProductName", "Purity", "Category",
    "MinWeight", "MaxWeight", "MakingChargePercent", "SupplierID"
])

def get_silver_rate(d: date) -> float:
    y, m = d.year, d.month
    if y == 2024:
        base = {1:70,2:72,3:74,4:76,5:80,6:83,7:86,8:88,9:91,10:95,11:100,12:104}
        noise = random.gauss(0, 2.5)
    elif y == 2025:
        base = {1:100,2:108,3:118,4:132,5:148,6:162,7:178,8:195,9:205,10:208,11:200,12:190}
        spike = random.uniform(5, 18) if random.random() < 0.05 else 0
        noise = random.gauss(0, 5) + spike
    else:
        base = {1:183,2:185,3:188,4:192}
        noise = random.gauss(0, 4)
    return round(max(60, base.get(m, 100) + noise), 2)

all_dates = pd.date_range("2024-01-01", "2026-04-30", freq="D")
calendar_rows    = []
silver_rate_rows = []

for dt in all_dates:
    d    = dt.date()
    rate = get_silver_rate(d)
    calendar_rows.append({
        "Date":      d,
        "Year":      dt.year,
        "Month":     dt.month,
        "MonthName": dt.strftime("%B"),
        "Quarter":   f"Q{dt.quarter}",
    })
    silver_rate_rows.append({"Date": d, "SilverRate_PerGram": rate})

calendar_df    = pd.DataFrame(calendar_rows)
silver_rate_df = pd.DataFrame(silver_rate_rows)
rate_lookup    = {r["Date"]: r["SilverRate_PerGram"] for r in silver_rate_rows}

FESTIVAL_MONTHS = {1:1.35, 4:1.25, 5:1.20, 10:1.45, 11:1.30, 12:1.20}

def season_boost(month):
    return FESTIVAL_MONTHS.get(month, 1.0)

shuffled_names = unique_names[:800]
random.shuffle(shuffled_names)
customer_rows = []

for i in range(800):
    city      = random.choices(cities, weights=city_weights)[0]
    cust_type = random.choices(["Retail", "Wholesale"], weights=[72, 28])[0]
    customer_rows.append({
        "CustomerID":       f"CUST{i+1:04}",
        "CustomerName":     shuffled_names[i],
        "City":             city,
        "CustomerType":     cust_type,
        "PreferredPayment": random.choices(
            ["Cash", "UPI", "Card", "Bank Transfer"], weights=[35, 40, 10, 15]
        )[0],
    })

customer_df = pd.DataFrame(customer_rows)

BASE_DEMAND = {
    "Kuttu Vilakku":3,"Anklet":12,"Khusbhu Anklet":10,"S Chain":9,"Karab Chain":8,
    "Earring":11,"Lion Kada":5,"Plain Kaap":8,"Metti":13,"Ring":12,
    "Kumkum Box":6,"Glass":5,"Plate":5,"Kaap":7,"Chain":10,"Cow Idol":4,"Purse":5,
}

def product_demand_weights(rate):
    weights = []
    for _, p in product_df.iterrows():
        base = BASE_DEMAND.get(p["ProductName"], 5)
        name = p["ProductName"]
        if rate > 190:
            if name in ["Kuttu Vilakku","Plate","Cow Idol","Glass","Lion Kada"]: base *= 0.30
            elif name in ["Metti","Ring","Earring"]:                             base *= 2.0
            elif name in ["Anklet","Khusbhu Anklet","S Chain","Karab Chain"]:    base *= 1.5
            if p["Purity"] == "92.5%" and name in ["Kaap","Chain","Anklet","Kuttu Vilakku"]:
                base *= 0.70
        elif rate > 160:
            if name in ["Kuttu Vilakku","Plate","Cow Idol"]: base *= 0.55
            elif name in ["Metti","Ring","Earring"]:         base *= 1.6
            elif name in ["Anklet","Khusbhu Anklet"]:        base *= 1.3
        elif rate > 130:
            if name in ["Kuttu Vilakku","Plate"]: base *= 0.75
            elif name in ["Metti","Ring"]:        base *= 1.3
        weights.append(max(0.1, base))
    return weights

def anklet_weight(size, purity, rate):
    base = (28 + size * 5) if purity == "80%" else (45 + size * 6)
    if rate > 190:   base *= 0.68
    elif rate > 160: base *= 0.80
    elif rate > 130: base *= 0.90
    return round(random.uniform(base, base + 18), 2)

active_customers  = customer_df.sample(550, random_state=42)["CustomerID"].tolist()
onetime_customers = customer_df[~customer_df["CustomerID"].isin(active_customers)]["CustomerID"].tolist()
onetime_used      = set()

sales_periods = [
    (date(2024,1,1), date(2024,12,31), 3000),
    (date(2025,1,1), date(2025,12,31), 2500),
    (date(2026,1,1), date(2026,4,30),   800),
]

sales_rows      = []
invoice_counter = 1

for (start_dt, end_dt, total_bills) in sales_periods:
    date_pool = []
    for offset in range((end_dt - start_dt).days + 1):
        d     = start_dt + timedelta(days=offset)
        count = max(1, int(season_boost(d.month) * 10))
        date_pool.extend([d] * count)

    for _ in range(total_bills):
        sale_date = random.choice(date_pool)
        rate      = rate_lookup.get(sale_date, get_silver_rate(sale_date))

        if random.random() < 0.85:
            cust_id  = random.choice(active_customers)
        else:
            available = [c for c in onetime_customers if c not in onetime_used]
            cust_id   = random.choice(available) if available else random.choice(active_customers)
            if available:
                onetime_used.add(cust_id)

        customer  = customer_df[customer_df["CustomerID"] == cust_id].iloc[0]
        product   = product_df.sample(1, weights=product_demand_weights(rate)).iloc[0]
        purity    = product["Purity"]
        purity_f  = 0.925 if purity == "92.5%" else 0.80
        cust_type = customer["CustomerType"]

        if product["ProductName"] in ["Anklet","Khusbhu Anklet"]:
            avg_weight = anklet_weight(random.randint(5, 11), purity, rate)
        else:
            min_w, max_w = product["MinWeight"], product["MaxWeight"]
            if rate > 190:   max_w = min_w + (max_w - min_w) * 0.55
            elif rate > 160: max_w = min_w + (max_w - min_w) * 0.70
            elif rate > 130: max_w = min_w + (max_w - min_w) * 0.85
            avg_weight = round(random.uniform(min_w, max_w), 2)

        if cust_type == "Wholesale":
            quantity = random.randint(3,20) if rate>180 else (random.randint(5,30) if rate>140 else random.randint(8,45))
        else:
            quantity = random.randint(1, 5)

        
        total_weight  = round(avg_weight * quantity, 2)
        metal_cost    = round(total_weight * rate * purity_f, 2)

        making_charge = round(metal_cost * product["MakingChargePercent"] / 100, 2)
        margin        = (random.uniform(0.12,0.24) if cust_type=="Retail"
                         else (random.uniform(0.03,0.07) if rate>180 else random.uniform(0.05,0.10)))
        base_selling  = (metal_cost + making_charge) * (1 + margin)
        discount_amt  = round(base_selling * random.choices([0,0.01,0.02,0.03,0.05], weights=[50,20,15,10,5])[0], 2)
        taxable_value = round(base_selling - discount_amt, 2)
        invoice_value = round(taxable_value * (1 + GST_RATE / 100), 2)

        sales_rows.append({
            "InvoiceNo":    f"INV{invoice_counter:07}",
            "Date":         sale_date,
            "CustomerID":   customer["CustomerID"],
            "CustomerType": cust_type,
            "ProductID":    product["ProductID"],
            "Quantity":     quantity,
            "MetalCost":    metal_cost,
            "TotalWeightGrams": total_weight,
            "InvoiceValue": invoice_value,
            
            
        })
        invoice_counter += 1

sales_df = pd.DataFrame(sales_rows)
sales_df.sort_values("Date", inplace=True)
sales_df.reset_index(drop=True, inplace=True)

purchase_rows = []
pur_id   = 1
pur_date = date(2024, 1, 1)

while pur_date <= date(2026, 4, 30):
    for _ in range(random.randint(1, 3)):
        supplier  = supplier_df.sample(1).iloc[0]
        sup_prods = product_df[product_df["SupplierID"] == supplier["SupplierID"]]
        if len(sup_prods) == 0:
            continue
        product    = sup_prods.sample(1).iloc[0]
        rate       = rate_lookup.get(pur_date, get_silver_rate(pur_date))
        qty        = random.randint(20, 120)
        avg_wt     = random.uniform(product["MinWeight"], product["MaxWeight"])
        purity_f   = 0.925 if product["Purity"] == "92.5%" else 0.80
        metal_cost = round(qty * avg_wt * rate * purity_f, 2)
        lead_days  = random.randint(2, 10)

        purchase_rows.append({
            "PurchaseID":    f"PUR{pur_id:06}",
            "PurchaseDate":  pur_date,
            "LeadTimeDays":  lead_days,
            "SupplierID":    supplier["SupplierID"],
            "ProductID":     product["ProductID"],
            "PurchaseValue": round(metal_cost * random.uniform(1.01, 1.035), 2),
        })
        pur_id += 1
    pur_date += timedelta(days=random.randint(3, 5))

purchase_df = pd.DataFrame(purchase_rows)

products_80  = product_df[product_df["Purity"] == "80%"]
products_925 = product_df[product_df["Purity"] == "92.5%"]
open_80      = 600_000 / len(products_80)
open_925     = 400_000 / len(products_925)

purchased_by_product = purchase_df.groupby("ProductID")["PurchaseValue"].count()
sold_by_product      = sales_df.groupby("ProductID")["Quantity"].sum()
latest_rate          = silver_rate_df["SilverRate_PerGram"].iloc[-1]

inventory_rows = []
for _, p in product_df.iterrows():
    pid       = p["ProductID"]
    base      = open_80 if p["Purity"] == "80%" else open_925
    open_s    = round(base * random.uniform(0.85, 1.15))
    purchased_g = purchase_df[purchase_df["ProductID"] == pid].shape[0] * random.uniform(
        p["MinWeight"], p["MaxWeight"]) * random.randint(20,120)
    sold_g    = sales_df[sales_df["ProductID"] == pid]["Quantity"].sum() * random.uniform(
        p["MinWeight"], p["MaxWeight"])
    purchased_g = round(purchased_g, 2)
    sold_g    = round(sold_g, 2)
    closing   = round(open_s + purchased_g - sold_g, 2)
    reorder   = round(open_s * 0.20, 2)

    inventory_rows.append({
        "ProductID":         pid,
        "SupplierID":        p["SupplierID"],
        "OpeningStockGrams": open_s,
        "PurchasedGrams":    purchased_g,
        "SoldGrams":         sold_g,
        "ClosingStockGrams": closing,
        "ReorderLevelGrams": reorder,
        "ReorderFlag":       "Reorder" if closing < reorder else "Healthy",
        "InventoryValue":    round(closing * latest_rate, 2),
    })

inventory_df = pd.DataFrame(inventory_rows)

def save(df, name):
    df.to_csv(os.path.join(OUTPUT_DIR, name), index=False)
    print(f"  {name:<30} {len(df):>6} rows")
print("\n====================================================")
print("  TRC SILVERS — EXPORTING DATASET")
print("====================================================")
save(customer_df,    "Customers.csv")
save(product_df,     "Products.csv")
save(supplier_df,    "Suppliers.csv")
save(calendar_df,    "Calendar.csv")
save(silver_rate_df, "SilverRates.csv")
save(purchase_df,    "Purchases.csv")
save(sales_df,       "Sales.csv")
save(inventory_df,   "Inventory.csv")
print(f"\n  ALL FILES SAVED TO: {OUTPUT_DIR}")
