'''
🧠 What is SMOTE?
SMOTE stands for Synthetic Minority Over-sampling Technique.

It is used when your dataset is imbalanced — meaning you have a lot of data for one category (like "No fraud") and very little data for the other (like "Fraud").

📊 Real-life Example:
Email	Spam or Not?
Email 1	Not Spam
Email 2	Not Spam
Email 3	Not Spam
Email 4	Spam

Here, only 1 spam email and 3 not spam = imbalanced data.

If you train a model like this, it will become lazy and say “Not Spam” always and still be 75% accurate. 😞

✅ Why We Need SMOTE?
SMOTE helps by:

Creating new synthetic (fake but realistic) examples of the minority class.

So the dataset becomes balanced, and your machine learning model learns fairly.

🤖 How Does SMOTE Work (Simple Words)?
It looks at a minority class example (e.g., "Spam").

Finds its nearest neighbors in the minority class.

Creates new, similar but slightly different points between them.

It’s like making artificial data that looks like real ones to balance things out.

🧪 Simple Code Example (Using Python)
We’ll use a fake dataset to demonstrate:


📍 Where Can You Use SMOTE?
Fraud Detection: Very few frauds compared to legit transactions.

Medical Diagnosis: Very few cancer patients vs many healthy ones.

Spam Detection: Most emails are not spam.

Credit Default: Most customers pay, few don't.

💼 Why Big Companies Need SMOTE Skills
Big companies like Amazon, JPMorgan, PayPal, or insurance firms work with imbalanced datasets all the time.

They need analysts and data scientists who can:

Identify class imbalance ⚖️

Apply techniques like SMOTE

Improve model fairness and accuracy

So, if you know SMOTE, you're already one step ahead in solving real-world ML problems.
'''


from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
from collections import Counter

# ----------------------- STEP 1: Create Imbalanced Data -----------------------

# Create dataset with 1000 samples, 2 features, all informative, no redundancy
X, y = make_classification(n_samples=1000, 
                           n_features=2, 
                           n_informative=2, 
                           n_redundant=0, 
                           weights=[0.9, 0.1], 
                           random_state=42)

# Print before SMOTE (expected: {0: 900, 1: 100})
print("Before SMOTE:", Counter(y))

# ----------------------- STEP 2: Apply SMOTE -----------------------

# Create SMOTE object
sm = SMOTE(random_state=42)

# Resample the dataset
X_res, y_res = sm.fit_resample(X, y)

# Print after SMOTE (expected: {0: 900, 1: 900})
print("After SMOTE:", Counter(y_res))
