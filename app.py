from flask import Flask, render_template, request
from Algorithms.cn2Website import CN2_Algorithm
from Algorithms.decisionTreeWebsite import D3_Algorithm as D3
from Algorithms.knnWebsite import KNN_Algorithm as knn

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST', 'GET'])
def result():
    """
        Function to get the characteristic values entered by the active user
        in the index.html page, pass these values to the algorithms to render
        predictions, and display these through the result.html page
    """

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

    # The CN2 prediction
    CN2 = CN2_Algorithm(testSet)
    result_CN2, rule_cn2 = CN2.test_model()

    # The KNN prediction
    KNN = knn(testSet)
    result_KNN, html = KNN.perform_KNN()

    # The Decision Tree prediction
    D_3 = D3(testSet)
    result_D3 = D_3.perform_D3()
    explanation = D_3.get_explanation()

    return render_template("result.html", result10=result_CN2, result20=result_KNN, result30=result_D3, rule_of_cn2=rule_cn2, html_knn=html, exp_d3=explanation)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
