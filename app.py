from flask import Flask, render_template, request
from test_rules import Test 
from decisionTreeWebsite import D3_RMS as D3
from knnWebsite import KNN_RMS as knn

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST', 'GET'])
def result():
    req_vol = request.values.get("requirementsVolatilitySelect")
    req_clar = request.values.get("requirementsClaritySelect")
    dev_time = request.values.get("developmentTimeSelect")
    project_size = request.values.get("projectSizeSelect")
    team_size = request.values.get("teamSizeSelect")
    prod_complexity = request.values.get("productComplexitySelect")
    test_intensity = request.values.get("testingSelect")
    risk_analysis = request.values.get("riskAnalysisSelect")
    user_participation = request.values.get("userParticipationSelect")
    team_expertise = request.values.get("teamExpertiseSelect")
    dev_expertise = request.values.get("developmentExpertiseSelect")
    doc_needed = request.values.get("documentationNeededSelect")
    fund_avail = request.values.get("fundingAvailableSelect")
    delivery_speed = request.values.get("deliverySpeedSelect")
    task_visualisation = request.values.get("taskVisualisationSelect")
    prototyping = request.values.get("prototypingSelect")
    
    testSet = [[req_vol, req_clar, dev_time, project_size,
                team_size, prod_complexity, test_intensity,
                risk_analysis, user_participation, team_expertise,
                dev_expertise, doc_needed, fund_avail, delivery_speed, task_visualisation,
                prototyping]]
    
    CN2 = Test(testSet)
    result_CN2 = CN2.test_model()

    KNN = knn(testSet)
    result_KNN = KNN.perform_KNN()

    D_3 = D3(testSet)
    result_D3 = D_3.perform_D31()


    return render_template("result.html", result10 = result_CN2, result20 = result_KNN, result30 = result_D3)
    


if __name__ == '__main__':
    app.run(debug= True, port=5001)