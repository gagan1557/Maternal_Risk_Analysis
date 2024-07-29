from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
import xgboost as xgb
import pickle
#
#
#
#
# def home(request):
#     return render(request, 'home.html')
#
# def predict(request):
#     return render(request, 'predict.html')
#
# def result(request):
#     df = pd.read_csv(r"C:\Users\Gagan\Desktop\DiabetesPrediction\DiabetesPrediction\DiabetesPredictionProject\Template\diabetes.csv")
#     X = df.drop("Outcome", axis=1)
#     Y = df["Outcome"]
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
#
#     classifier = svm.SVC(kernel='linear')
#     classifier.fit(X_train, Y_train)
#
#     val1 = float(request.GET['n1'])
#     val2 = float(request.GET['n2'])
#     val3 = float(request.GET['n3'])
#     val4 = float(request.GET['n4'])
#     val5 = float(request.GET['n5'])
#     val6 = float(request.GET['n6'])
#     val7 = float(request.GET['n7'])
#     val8 = float(request.GET['n8'])
#
#     pred = classifier.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
#
#     result1 = ''
#     if pred ==[1]:
#         result1 = "Positive"
#     else:
#         result1 = "Negative"
#
#
#     return render(request,'predict.html',{"result2":result1})


from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score




def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def predict2(request):
    return render(request, 'predict2.html')
def hello(request):
    return render(request, 'hello.html')



def result(request):
    df = pd.read_csv(r"C:\Users\Gagan\Desktop\pregnantwomananalysis\MaternalRisk\pregnancy\Maternal_Health_Risk_Data_Set.csv")
    df['RiskLevel'].replace(['low risk', 'mid risk', 'high risk'], [0, 1, 2], inplace=True)
    X = df.drop('RiskLevel', axis=1)
    Y = df['RiskLevel']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    model_dt = DecisionTreeClassifier()
    model_dt.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])


    pred = model_dt.predict([[val1, val2, val3, val4, val5, val6]])

    result1 = ''
    if pred == [0]:
        result1 = "The patient has low risk"
    elif pred == [1]:
        result1 = "The patient has medium level risk"
    else:
        result1 = "The patient has High level risk"




    return render(request,'predict.html',{"result2":result1})





def mentalresult(request):
    da = pd.read_csv(r"C:\Users\Gagan\Desktop\pregnantwomananalysis\MaternalRisk\pregnancy\Mental_health.csv")

    age_mapping = {'25-30': 1,
                   '30-35': 2,
                   '35-40': 3,
                   '40-45': 4,
                   '45-50': 5
                   }
    Irritable_mapping = {
        'Yes': 2,
        'No': 0,
        'Sometimes': 1
    }
    Conc_mapping = {
        'Yes': 2,
        'No': 0,
        'Often': 1
    }
    Anxious_mapping = {
        'Yes': 1,
        'No': 0
    }
    Bonding_mapping = {
        'Yes': 2,
        'No': 0,
        'Sometimes': 1
    }

    Feeling_mapping = {
        'Yes': 2,
        'Sometimes': 1,
        'No': 0,
    }
    Sleeping_mapping = {
        'Yes': 2,
        'Two or more days a week': 1,
        'No': 0,
    }

    Overeating_mapping = {
        'Yes': 2,
        'No': 1,
        'Not at all': 0,
    }

    Guilt_mapping = {
        'Yes': 2,
        'Maybe': 1,
        'No': 0,
    }

    da['Age'] = da['Age'].map(age_mapping)
    da['Irritable towards partner'] = da['Irritable towards partner'].map(Irritable_mapping)
    da['Problems concentrating or making decision'] = da['Problems concentrating or making decision'].map(Conc_mapping)
    da['Feeling anxious'] = da['Feeling anxious'].map(Anxious_mapping)
    da['Problems of bonding '] = da['Problems of bonding '].map(Bonding_mapping)
    da['Feeling sad or Tearful'] = da['Feeling sad or Tearful'].map(Feeling_mapping)
    da['Trouble sleeping at night'] = da['Trouble sleeping at night'].map(Sleeping_mapping)
    da['Overeating or loss of appetite'] = da['Overeating or loss of appetite'].map(Overeating_mapping)
    da['Feeling of guilt'] = da['Feeling of guilt'].map(Guilt_mapping)

    x = da.drop(columns=['Feeling anxious']).values

    y = da['Feeling anxious'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, stratify=y )

    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])
    val14 = float(request.GET['n14'])
    val15 = float(request.GET['n15'])
    val16 = float(request.GET['n16'])
    val17 = float(request.GET['n17'])
    val18 = float(request.GET['n18'])

    xgb_model = xgb.XGBClassifier(n_estimators=1000, random_state=1, n_jobs=-1)
    xgb_model.fit(x_train, y_train)

    prediction = xgb_model.predict([[val11, val12, val13, val14, val15, val16, val17, val18 ]])

    mentalresult1 = ''

    if prediction[0] == 0:
        mentalresult1 ="Congrats! You are a fit mother, you just need to maintain it."

    else:
        mentalresult1 = "The patient requires happy pills to stay healthy"


    return render(request, 'predict2.html', {"mresult2": mentalresult1})


#
#
#
#
# from .chatbot_script import answer_question
#
#
#
# def chatbot(request):
#     if request.method == 'POST':
#         print("working")
#         question = request.POST.get('question')
#         context = { "trimesters": "Pregnancy is divided into three trimesters: The first trimester lasts from week 1 to week 12. The second trimester lasts from week 13 to week 26. The third trimester lasts from week 27 to the end of pregnancy.",
#         "symptoms of pregnancy": "Early symptoms of pregnancy may include missed periods, tender breasts, nausea and vomiting, hunger, and frequent urination.",
#         "confirm pregnancy": "Pregnancy may be confirmed with a pregnancy test.",
#         "prenatal care": "Prenatal care improves pregnancy outcomes and typically includes regular visits to a healthcare provider, nutritional advice, and monitoring of the mother and fetus's health.",
#         "stages of labor": "Labor is divided into three stages: The first stage is the dilation of the cervix. The second stage is the delivery of the baby. The third stage is the delivery of the placenta.",
#         "diet during pregnancy": "A balanced diet during pregnancy includes fruits, vegetables, whole grains, lean proteins, and dairy products. It's important to avoid alcohol, caffeine, and certain fish high in mercury.",
#         "exercise during pregnancy": "Regular exercise during pregnancy can help with weight management, reduce back pain, and improve mood. Recommended activities include walking, swimming, and prenatal yoga.",
#         "common discomforts": "Common discomforts during pregnancy include morning sickness, heartburn, constipation, and back pain. These can often be managed with diet, exercise, and proper hydration.",
#         "high-risk pregnancy": "A high-risk pregnancy may involve conditions such as preeclampsia, gestational diabetes, or multiple pregnancies. Regular monitoring and specialized care are essential for managing high-risk pregnancies.",
#         "prenatal vitamins": "Prenatal vitamins, including folic acid, iron, and calcium, support the health of the mother and the developing baby. They are usually recommended before and during pregnancy.",
#         "fetal development": "Fetal development progresses through distinct stages: The first trimester focuses on basic cell differentiation. The second trimester involves the development of organs and systems. The third trimester is characterized by significant growth and maturation.",
#         "postpartum care": "Postpartum care includes physical recovery, mental health support, and newborn care. It's important for new mothers to attend postnatal check-ups and seek support as needed.",
#         "breastfeeding": "Breastfeeding provides essential nutrients and antibodies to the baby. It also promotes bonding and has health benefits for both the mother and the child.",
#         "gestational diabetes": "Gestational diabetes is a condition where blood sugar levels become elevated during pregnancy. It requires dietary management, regular monitoring, and sometimes medication.",
#         "morning sickness": "Morning sickness involves nausea and vomiting, typically occurring in the first trimester. Eating small, frequent meals and staying hydrated can help manage symptoms.",
#         "swelling during pregnancy": "Swelling, especially in the feet and ankles, is common during pregnancy due to increased fluid retention. Elevating the feet and reducing salt intake can help.",
#         "weight gain during pregnancy": "Weight gain during pregnancy varies but generally ranges from 25-35 pounds for a woman with a normal BMI. It's important to follow healthcare provider guidelines for a healthy pregnancy.",
#         "ultrasound during pregnancy": "Ultrasound scans are used to monitor fetal development, check for any abnormalities, and determine the baby's position and size. They are typically done at various stages of pregnancy.",
#         "birth plan": "A birth plan outlines your preferences for labor and delivery, including pain management, the presence of a birth partner, and any specific requests for the birth process.",
#         "preterm labor": "Preterm labor occurs when labor begins before 37 weeks of pregnancy. Signs include regular contractions and changes in vaginal discharge. Immediate medical attention is required.",
#         "c-section": "A Cesarean section (C-section) is a surgical procedure to deliver a baby through incisions in the abdomen and uterus. It may be planned or performed in an emergency.",
#         "preeclampsia": "Preeclampsia is a pregnancy complication characterized by high blood pressure and signs of damage to other organs, usually the liver and kidneys. It requires close monitoring and management.",
#         "miscarriage": "Miscarriage is the loss of a pregnancy before the 20th week. It can be caused by genetic factors, health conditions, or other reasons. Support and medical care are important.",
#         "mental health during pregnancy": "Mental health during pregnancy is crucial. It's common to experience a range of emotions, and support from healthcare providers, family, and friends is important.",
#         "vaccinations during pregnancy": "Certain vaccinations, like the flu shot and Tdap, are recommended during pregnancy to protect both the mother and the baby from infections.",
#         "travel during pregnancy": "Travel during pregnancy is generally safe, but it's important to consult with a healthcare provider. Stay hydrated, move frequently, and be aware of medical facilities at the destination."
#     }
#         answer = answer_question(question, context)
#         print(answer)
#         return render(request, 'hello.html', {'answer': answer})
#     else:
#         return render(request, 'hello.html')





from .chatbot_script import answer_question

def chatbot(request):
    if request.method == 'POST':

        question = request.POST.get('question')
        context = """
        Pregnancy, also known as gestation, is the time during which one or more offspring develops inside a woman. A multiple pregnancy involves more than one offspring, such as with twins. Pregnancy can occur by sexual intercourse or assisted reproductive technology. It usually lasts around 40 weeks from the last menstrual period (LMP) and ends in childbirth.

        Symptoms of early pregnancy may include missed periods, tender breasts, nausea and vomiting, hunger, and frequent urination. Pregnancy may be confirmed with a pregnancy test. Prenatal care improves pregnancy outcomes.

        Pregnancy is divided into three trimesters:
        - The first trimester lasts from week 1 to week 12. During this period, the body undergoes significant changes, and the risk of miscarriage is higher.
        - The second trimester lasts from week 13 to week 26. It is often considered the most comfortable period, as morning sickness usually subsides and energy levels increase.
        - The third trimester lasts from week 27 to the end of pregnancy. The fetus grows rapidly, and the mother may experience discomfort due to the increased size of the abdomen.

        Prenatal care typically includes regular visits to a healthcare provider, nutritional advice, and monitoring of the mother and fetus's health. It is crucial for ensuring the health and well-being of both the mother and the baby.

        Labor is divided into three stages: The first stage is the dilation of the cervix. The second stage is the delivery of the baby. The third stage is the delivery of the placenta.

        A balanced diet during pregnancy includes fruits, vegetables, whole grains, lean proteins, and dairy products. It's important to avoid alcohol, caffeine, and certain fish high in mercury.

        Regular exercise during pregnancy can help with weight management, reduce back pain, and improve mood. Recommended activities include walking, swimming, and prenatal yoga.

        Common discomforts during pregnancy include morning sickness, heartburn, constipation, and back pain. These can often be managed with diet, exercise, and proper hydration.

        A high-risk pregnancy may involve conditions such as preeclampsia, gestational diabetes, or multiple pregnancies. Regular monitoring and specialized care are essential for managing high-risk pregnancies.

        Prenatal vitamins, including folic acid, iron, and calcium, support the health of the mother and the developing baby. They are usually recommended before and during pregnancy.

        Fetal development progresses through distinct stages: The first trimester focuses on basic cell differentiation. The second trimester involves the development of organs and systems. The third trimester is characterized by significant growth and maturation.

        Postpartum care includes physical recovery, mental health support, and newborn care. It's important for new mothers to attend postnatal check-ups and seek support as needed.

        Breastfeeding provides essential nutrients and antibodies to the baby. It also promotes bonding and has health benefits for both the mother and the child.

        Gestational diabetes is a condition where blood sugar levels become elevated during pregnancy. It requires dietary management, regular monitoring, and sometimes medication.

        Morning sickness involves nausea and vomiting, typically occurring in the first trimester. Eating small, frequent meals and staying hydrated can help manage symptoms.

        Swelling, especially in the feet and ankles, is common during pregnancy due to increased fluid retention. Elevating the feet and reducing salt intake can help.

        Weight gain during pregnancy varies but generally ranges from 25-35 pounds for a woman with a normal BMI. It's important to follow healthcare provider guidelines for a healthy pregnancy.

        Ultrasound scans are used to monitor fetal development, check for any abnormalities, and determine the baby's position and size. They are typically done at various stages of pregnancy."""

        answer = answer_question(question, context)

        return render(request, 'hello.html', {'answer': answer})
    else:
        return render(request, 'hello.html')