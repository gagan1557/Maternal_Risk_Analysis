#
# import torch
# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
#
# model_name = "distilbert-base-uncased-distilled-squad"
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
#
#
# qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
#
#
# def answer_question(question, context):
#
#     keyword_responses = {
#         "trimesters": "Pregnancy is divided into three trimesters: The first trimester lasts from week 1 to week 12. The second trimester lasts from week 13 to week 26. The third trimester lasts from week 27 to the end of pregnancy.",
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
#
#     for keyword, response in keyword_responses.items():
#         if keyword in question.lower():
#             return response
#     return "Please rephrase your question or provide more context."
#
#
#
#     response = qa_pipeline({
#         'question': question,
#         'context': context
#     })
#     return response['answer']
#
#
# context = """
# Pregnancy, also known as gestation, is the time during which one or more offspring develops inside a woman. A multiple pregnancy involves more than one offspring, such as with twins. Pregnancy can occur by sexual intercourse or assisted reproductive technology. It usually lasts around 40 weeks from the last menstrual period (LMP) and ends in childbirth.
#
# Symptoms of early pregnancy may include missed periods, tender breasts, nausea and vomiting, hunger, and frequent urination. Pregnancy may be confirmed with a pregnancy test. Prenatal care improves pregnancy outcomes.
#
# Pregnancy is divided into three trimesters:
# - The first trimester lasts from week 1 to week 12. During this period, the body undergoes significant changes, and the risk of miscarriage is higher.
# - The second trimester lasts from week 13 to week 26. It is often considered the most comfortable period, as morning sickness usually subsides and energy levels increase.
# - The third trimester lasts from week 27 to the end of pregnancy. The fetus grows rapidly, and the mother may experience discomfort due to the increased size of the abdomen.
#
# Prenatal care typically includes regular visits to a healthcare provider, nutritional advice, and monitoring of the mother and fetus's health. It is crucial for ensuring the health and well-being of both the mother and the baby.
#
# Labor is divided into three stages: The first stage is the dilation of the cervix. The second stage is the delivery of the baby. The third stage is the delivery of the placenta.
#
# A balanced diet during pregnancy includes fruits, vegetables, whole grains, lean proteins, and dairy products. It's important to avoid alcohol, caffeine, and certain fish high in mercury.
#
# Regular exercise during pregnancy can help with weight management, reduce back pain, and improve mood. Recommended activities include walking, swimming, and prenatal yoga.
#
# Common discomforts during pregnancy include morning sickness, heartburn, constipation, and back pain. These can often be managed with diet, exercise, and proper hydration.
#
# A high-risk pregnancy may involve conditions such as preeclampsia, gestational diabetes, or multiple pregnancies. Regular monitoring and specialized care are essential for managing high-risk pregnancies.
#
# Prenatal vitamins, including folic acid, iron, and calcium, support the health of the mother and the developing baby. They are usually recommended before and during pregnancy.
#
# Fetal development progresses through distinct stages: The first trimester focuses on basic cell differentiation. The second trimester involves the development of organs and systems. The third trimester is characterized by significant growth and maturation.
#
# Postpartum care includes physical recovery, mental health support, and newborn care. It's important for new mothers to attend postnatal check-ups and seek support as needed.
#
# Breastfeeding provides essential nutrients and antibodies to the baby. It also promotes bonding and has health benefits for both the mother and the child.
#
# Gestational diabetes is a condition where blood sugar levels become elevated during pregnancy. It requires dietary management, regular monitoring, and sometimes medication.
#
# Morning sickness involves nausea and vomiting, typically occurring in the first trimester. Eating small, frequent meals and staying hydrated can help manage symptoms.
#
# Swelling, especially in the feet and ankles, is common during pregnancy due to increased fluid retention. Elevating the feet and reducing salt intake can help.
#
# Weight gain during pregnancy varies but generally ranges from 25-35 pounds for a woman with a normal BMI. It's important to follow healthcare provider guidelines for a healthy pregnancy.
#
# Ultrasound scans are used to monitor fetal development, check for any abnormalities, and determine the baby's position and size. They are typically done at various stages of pregnancy."""
#
#
# def chatbot():
#     print("Hello! I am here to answer your questions about pregnancy.")
#     print("Type 'exit' to end the conversation.")
#     while True:
#         question = input("You: ")
#         if question.lower() in ["exit", "quit"]:
#             print("Goodbye! Take care.")
#             break
#
#         answer = answer_question(question, context)
#         print(f"Chatbot: {answer}")
#
# if __name__ == "__main__":
#     chatbot()
#
#
#
#
#
#
#
#
#
#
#
#
#


import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "distilbert-base-uncased-distilled-squad"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)


def answer_question(question, context):
    keyword_responses = {
        "trimesters": "Pregnancy is divided into three trimesters: The first trimester lasts from week 1 to week 12. The second trimester lasts from week 13 to week 26. The third trimester lasts from week 27 to the end of pregnancy.",
        "symptoms of pregnancy": "Early symptoms of pregnancy may include missed periods, tender breasts, nausea and vomiting, hunger, and frequent urination.",
        "confirm pregnancy": "Pregnancy may be confirmed with a pregnancy test.",
        "prenatal care": "Prenatal care improves pregnancy outcomes and typically includes regular visits to a healthcare provider, nutritional advice, and monitoring of the mother and fetus's health.",
        "stages of labor": "Labor is divided into three stages: The first stage is the dilation of the cervix. The second stage is the delivery of the baby. The third stage is the delivery of the placenta.",
        "diet during pregnancy": "A balanced diet during pregnancy includes fruits, vegetables, whole grains, lean proteins, and dairy products. It's important to avoid alcohol, caffeine, and certain fish high in mercury.",
        "exercise during pregnancy": "Regular exercise during pregnancy can help with weight management, reduce back pain, and improve mood. Recommended activities include walking, swimming, and prenatal yoga.",
        "common discomforts": "Common discomforts during pregnancy include morning sickness, heartburn, constipation, and back pain. These can often be managed with diet, exercise, and proper hydration.",
        "high-risk pregnancy": "A high-risk pregnancy may involve conditions such as preeclampsia, gestational diabetes, or multiple pregnancies. Regular monitoring and specialized care are essential for managing high-risk pregnancies.",
        "prenatal vitamins": "Prenatal vitamins, including folic acid, iron, and calcium, support the health of the mother and the developing baby. They are usually recommended before and during pregnancy.",
        "fetal development": "Fetal development progresses through distinct stages: The first trimester focuses on basic cell differentiation. The second trimester involves the development of organs and systems. The third trimester is characterized by significant growth and maturation.",
        "postpartum care": "Postpartum care includes physical recovery, mental health support, and newborn care. It's important for new mothers to attend postnatal check-ups and seek support as needed.",
        "breastfeeding": "Breastfeeding provides essential nutrients and antibodies to the baby. It also promotes bonding and has health benefits for both the mother and the child.",
        "gestational diabetes": "Gestational diabetes is a condition where blood sugar levels become elevated during pregnancy. It requires dietary management, regular monitoring, and sometimes medication.",
        "morning sickness": "Morning sickness involves nausea and vomiting, typically occurring in the first trimester. Eating small, frequent meals and staying hydrated can help manage symptoms.",
        "swelling during pregnancy": "Swelling, especially in the feet and ankles, is common during pregnancy due to increased fluid retention. Elevating the feet and reducing salt intake can help.",
        "weight gain during pregnancy": "Weight gain during pregnancy varies but generally ranges from 25-35 pounds for a woman with a normal BMI. It's important to follow healthcare provider guidelines for a healthy pregnancy.",
        "ultrasound during pregnancy": "Ultrasound scans are used to monitor fetal development, check for any abnormalities, and determine the baby's position and size. They are typically done at various stages of pregnancy.",
        "birth plan": "A birth plan outlines your preferences for labor and delivery, including pain management, the presence of a birth partner, and any specific requests for the birth process.",
        "preterm labor": "Preterm labor occurs when labor begins before 37 weeks of pregnancy. Signs include regular contractions and changes in vaginal discharge. Immediate medical attention is required.",
        "c-section": "A Cesarean section (C-section) is a surgical procedure to deliver a baby through incisions in the abdomen and uterus. It may be planned or performed in an emergency.",
        "preeclampsia": "Preeclampsia is a pregnancy complication characterized by high blood pressure and signs of damage to other organs, usually the liver and kidneys. It requires close monitoring and management.",
        "miscarriage": "Miscarriage is the loss of a pregnancy before the 20th week. It can be caused by genetic factors, health conditions, or other reasons. Support and medical care are important.",
        "mental health during pregnancy": "Mental health during pregnancy is crucial. It's common to experience a range of emotions, and support from healthcare providers, family, and friends is important.",
        "vaccinations during pregnancy": "Certain vaccinations, like the flu shot and Tdap, are recommended during pregnancy to protect both the mother and the baby from infections.",
        "travel during pregnancy": "Travel during pregnancy is generally safe, but it's important to consult with a healthcare provider. Stay hydrated, move frequently, and be aware of medical facilities at the destination."
    }

    for keyword, response in keyword_responses.items():
        if keyword in question.lower():
            return response

    response = qa_pipeline({
        'question': question,
        'context': context
    })
    return response['answer']