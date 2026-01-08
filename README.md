<h2>Title:</h2>
<h1>ATM Application Using Python Flask Framework</h1>
<h2>Objective:</h2>
<ol>
<li>
The objective of this project is to develop a simple ATM system using the Flask web framework in Python, where users can create accounts, deposit, withdraw, and delete accounts. </li>
<li>This application demonstrates basic CRUD operations and memory-based data storage without using a database. </li>
<li>It is suitable for beginners to understand form handling, routing, and dictionary-based storage in Flask.</li></ol>

<h2>Concept Flow</h2>
<pre>
| Feature                     | Meaning / Description                                                         |
| --------------------------- | ----------------------------------------------------------------------------- |
| Form Data Submission        | Takes input from an HTML form and sends the data to Flask using HTTP methods  |
| Memory Storage (Dictionary) | Stores account details temporarily in a Python dictionary (in-memory storage) |
| Dashboard Data Flow         | Shares and displays account data between different web pages                  |
| Read (Balance)              | Displays the current account balance to the user                              |
| Update (Deposit / Withdraw) | Adds or removes money from the account balance                                |
| Delete Account              | Removes the account details from the dictionary                               |
</pre>

<h2> Project Folder Structure</h2>
atm_app/
│ app.py
└─ templates/
    │ register.html
    │ dashboard.html
|.gitignore
|README.md


