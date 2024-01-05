# import model_joblib
import numpy as np
import joblib
import streamlit as st
import matplotlib.pyplot as plt



def diabetes_prediction(loaded_model, input_data):
    try:
        # Convert input data to float and reshape for prediction
        input_data = [float(value) for value in input_data]
        #input_data = input_data
        input_data_reshaped = np.array(input_data).reshape(1, -1)

        # Perform the prediction
        prediction = loaded_model.predict(input_data_reshaped)

        if prediction[0] == 0:
            return 'The person is not diabetic'
        else:
            return 'The person is diabetic'
    except Exception as e:
        return f"Error making prediction: {e}"





def validate_gender(gender):
    if gender == 'Female':
        return 0
    else:
        return 1

def validate_HR_tension(ht):
    if ht == 'Yes':
        return 1
    else:
        return 0
def validate_He_disease(Hd):
    if Hd == 'Yes':
        return 1
    else:
        return 0


smoking_options = {
        'No_information': 0,
        'Currently_smoking': 1,
        'ForEver_smoking': 2,
        'Former_smoker': 3,
        'Never_smoke': 4,
        'Currently_Not_smoking': 5

}




def main():
    loaded_model = None
    try:
        #loaded_model = joblib.load('D:/Vishnu_prjct/model_joblib')
        loaded_model = joblib.load('model_joblib')


    except Exception as e:
        st.error(f"Error loading the model: {e}")

    st.set_page_config(
        page_title="Diabetes Prediction",
        page_icon=":hospital:",
        layout="wide"
    )
    st.title('Diabetes Prediction')
    st.markdown("---")



    Gender = st.selectbox('Select Gender', ['Female', 'Male'])
    Gender = validate_gender(Gender)
    Age = st.number_input('Enter Age', min_value=1, max_value=90)
    Hyper_Tension = st.selectbox('Do you Have Blood pressure Taking Medicines ', ['Yes','No'])#, placeholder='Hyper_tension')
    Hyper_Tension = validate_HR_tension(Hyper_Tension)

    Heart_disease = st.selectbox('Do you have Heart_disease Taking Medicines ', ['Yes','No'],placeholder='Heart_disease')
    Heart_disease = validate_He_disease(Heart_disease)

    selected_smoking_option = st.selectbox('Select Smoking Status', list(smoking_options.keys()))
    Smoking = smoking_options[selected_smoking_option]
    BMI = st.number_input('BMI Range', min_value=10.0, max_value=97.0, step=1.0)
    HbA1c = st.number_input(' Haemoglobin Level HbA1c_Level', min_value=3.0, max_value=9.0, step=0.1)
    Blood_glucose = st.number_input('Enter Blood Glucose Level', min_value=70, max_value=300)




    diagnosis = ''

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction(loaded_model,[Gender, Age,Hyper_Tension, Heart_disease,
                                             Smoking, BMI, HbA1c, Blood_glucose])

        st.success(diagnosis)


if __name__ == '__main__':
    main()
