import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saves_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    
    return data

data = load_model()

regressor = data['model']
ohe_vendor = data['ohe_vendor']
ohe_model = data['ohe_model']

def show_predicted_page():
    st.title('Relative CPU Performance')
    st.write("""### We need some information""")
    
    vendors = ['adviser', 'amdahl', 'apollo', 'basf', 'bti', 'burroughs', 'c.r.d',
       'cdc', 'cambex', 'dec', 'dg', 'formation', 'four-phase', 'gould',
       'hp', 'harris', 'honeywell', 'ibm', 'ipl', 'magnuson', 'microdata',
       'nas', 'ncr', 'nixdorf', 'perkin-elmer', 'prime', 'siemens',
       'sperry', 'sratus', 'wang']

    models = ['32/60', '470v/7', '470v/7a', '470v/7b', '470v/7c', '470v/b',
       '580-5840', '580-5850', '580-5860', '580-5880', 'dn320', 'dn420',
       '7/65', '7/68', '5000', '8000', 'b1955', 'b2900', 'b2925', 'b4955',
       'b5900', 'b5920', 'b6900', 'b6925', '68/10-80', 'universe:2203t',
       'universe:68', 'universe:68/05', 'universe:68/137',
       'universe:68/37', 'cyber:170/750', 'cyber:170/760',
       'cyber:170/815', 'cyber:170/825', 'cyber:170/835', 'cyber:170/845',
       'omega:480-i', 'omega:480-ii', 'omega:480-iii', '1636-1',
       '1636-10', '1641-1', '1641-11', '1651-1', 'decsys:10:1091',
       'decsys:20:2060', 'microvax-1', 'vax:11/730', 'vax:11/750',
       'vax:11/780', 'eclipse:c/350', 'eclipse:m/600', 'eclipse:mv/10000',
       'eclipse:mv/4000', 'eclipse:mv/6000', 'eclipse:mv/8000',
       'eclipse:mv/8000-ii', 'f4000/100', 'f4000/200', 'f4000/200ap',
       'f4000/300', 'f4000/300ap', '2000/260', 'concept:32/8705',
       'concept:32/8750', 'concept:32/8780', '3000/30', '3000/40',
       '3000/44', '3000/48', '3000/64', '3000/88', '3000/iii', '100',
       '300', '500', '600', '700', '80', '800', 'dps:6/35', 'dps:6/92',
       'dps:6/96', 'dps:7/35', 'dps:7/45', 'dps:7/55', 'dps:7/65',
       'dps:8/44', 'dps:8/49', 'dps:8/50', 'dps:8/52', 'dps:8/62',
       'dps:8/20', '3033:s', '3033:u', '3081', '3081:d', '3083:b',
       '3083:e', '370/125-2', '370/148', '370/158-3', '38/3', '38/4',
       '38/5', '38/7', '38/8', '4321', '4331-1', '4331-11', '4331-2',
       '4341', '4341-1', '4341-10', '4341-11', '4341-12', '4341-2',
       '4341-9', '4361-4', '4361-5', '4381-1', '4381-2', '8130-a',
       '8130-b', '8140', '4436', '4443', '4445', '4446', '4460', '4480',
       'm80/30', 'm80/31', 'm80/32', 'm80/42', 'm80/43', 'm80/44',
       'seq.ms/3200', 'as/3000', 'as/3000-n', 'as/5000', 'as/5000-e',
       'as/5000-n', 'as/6130', 'as/6150', 'as/6620', 'as/6630', 'as/6650',
       'as/7000', 'as/7000-n', 'as/8040', 'as/8050', 'as/8060',
       'as/9000-dpc', 'as/9000-n', 'as/9040', 'as/9060', 'v8535:ii',
       'v8545:ii', 'v8555:ii', 'v8565:ii', 'v8565:ii-e', 'v8575:ii',
       'v8585:ii', 'v8595:ii', 'v8635', 'v8650', 'v8655', 'v8665',
       'v8670', '8890/30', '8890/50', '8890/70', '3205', '3210', '3230',
       '50-2250', '50-250-ii', '50-550-ii', '50-750-ii', '50-850-ii',
       '7.521', '7.531', '7.536', '7.541', '7.551', '7.561', '7.865-2',
       '7.870-2', '7.872-2', '7.875-2', '7.880-2', '7.881-2',
       '1100/61-h1', '1100/81', '1100/82', '1100/83', '1100/84',
       '1100/93', '1100/94', '80/3', '80/4', '80/5', '80/6', '80/8',
       '90/80-model-3', '32', 'vs-100', 'vs-90']


    vendor_name = st.selectbox('Vendor Name', vendors)
    model_name = st.selectbox('Model Name', models)
    myct = st.number_input("Machine Cycle Time in Nanoseconds")
    mmin = st.number_input("minimum main memory in kilobytes")
    mmax = st.number_input("maximum main memory in kilobytes")
    cach = st.number_input("cache memory in kilobytes")
    chmin = st.number_input("minimum channels in units")
    chmax = st.number_input("maximum channels in units")
    prp = st.number_input("published relative performance")

    done = st.button('Calculate Estimated Relative Performance')

    if done:


        # Concatenate all the features
        # input_features = np.array([[myct, mmin, mmax, cach, chmin, chmax, prp, vendor_name, model_name]])
        # input_features[:, -2] = ohe_vendor.transform(input_features[:, -2])
        # input_features[:, -1] = ohe_model.transform(input_features[:, -1])
        # input_features = input_features.astype(float)

        # print(input_features)

        input_features = np.array([[myct, mmin, mmax, cach, chmin, chmax, prp, vendor_name, model_name]])
        categorical_features = np.array([[vendor_name, model_name]])
        numerical_features = np.array([[myct, mmin, mmax, cach, chmin, chmax, prp]])

        # Apply one-hot encoding to the categorical features
        encoded_vendor = ohe_vendor.transform(categorical_features[:, 0].reshape(1, -1))
        encoded_model = ohe_model.transform(categorical_features[:, 1].reshape(1, -1))

        # Concatenate the encoded categorical features and the numerical features
        input_features = np.concatenate((numerical_features, encoded_vendor, encoded_model), axis=1)


        # Make predictions using the trained model
        predicted_performance = regressor.predict(input_features)

        st.subheader(f"Estimated Relative Performance: {predicted_performance[0]:.2f}")
