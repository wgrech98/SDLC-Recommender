from flask import Flask, render_template, request
from test_rules import Test
from decisionTreeWebsite import D3_RMS as D3
from knnWebsite import KNN_RMS as knn

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST', 'GET'])
def result():
    requirements_volatility = request.values.get(
        "requirementsVolatilitySelect")
    requirements_clarity = request.values.get("requirementsClaritySelect")
    development_time = request.values.get("developmentTimeSelect")
    project_size = request.values.get("projectSizeSelect")
    team_size = request.values.get("teamSizeSelect")
    product_complexity = request.values.get("productComplexitySelect")
    testing_intensity = request.values.get("testingSelect")
    risk_analysis = request.values.get("riskAnalysisSelect")
    user_participation = request.values.get("userParticipationSelect")
    team_expertise = request.values.get("teamExpertiseSelect")
    development_expertise = request.values.get("developmentExpertiseSelect")
    documentation_needed = request.values.get("documentationNeededSelect")
    funding_availibility = request.values.get("fundingAvailableSelect")
    delivery_speed = request.values.get("deliverySpeedSelect")
    task_visualisation = request.values.get("taskVisualisationSelect")
    prototyping = request.values.get("prototypingSelect")

    testSet = [[requirements_volatility, requirements_clarity, development_time, project_size,
                team_size, product_complexity, testing_intensity,
                risk_analysis, user_participation, team_expertise,
                development_expertise, documentation_needed, funding_availibility, delivery_speed, task_visualisation,
                prototyping]]

    CN2 = Test(testSet)
    result_CN2, rule_cn2 = CN2.test_model()

    KNN = knn(testSet)
    result_KNN, html = KNN.perform_KNN()

    D_3 = D3(testSet)
    result_D3 = D_3.perform_D31()
    explanation = D_3.get_explanation()

    return render_template("result.html", result10=result_CN2, result20=result_KNN, result30=result_D3, rule_of_cn2=rule_cn2, html_knn=html, exp_d3=explanation)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
