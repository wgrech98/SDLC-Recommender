scrum_text = '<ul class="popover__message">' +
                '<li>Scrum employs an iterative and feedback strategy by adopting short development cycles referred to as sprints</li>'+
                '<li>Development tasks are undertaken according to priority from the sprint backlog </li>'+
                '<li>This strategy makes Scrum appropriate for dynamic customer requirements</li>'+
            '</ul>'

waterfall_text = '<ul class="popover__message">' +
                    '<li>The Waterfall methodology is regarded as the methodology suitable for projects with stringent requirements</li>'+
                    '<li>Due to its rigidity, the model is easy to use and understand, and simple to coordinate</li>'+
                '</ul>'

kanban_text = '<ul class="popover__message">' +
                    '<li>The Kanban approach falls under the agile methodology where work scheduling takes precedence over other factors</li>'+
                    '<li>Individual tasks are listed in the Kanban board according to their current progression to being completed </li>'+
                '</ul>'

spiral_text = '<ul class="popover__message">' +
                '<li>A combination of the iterative development process and the waterfall methodology</li>'+
                '<li>Accounts for the risk factor in software projects. This is done through the rings in the spiral which are used to resemble every phase in the SD process</li>'+
                '<li>In every stage of the spiral process, prototypes are designed for the client to test and identify risks during the development process, thus unknown risks are gradually reduced</li>'+
             '</ul>'

rad_text = '<ul class="popover__message">' +
                '<li>Quick development, rapid delivery, and at minimum cost</li>'+
                '<li>The project is split into sub-components to ease the process of modification during the development process</li>'+            
            '</ul>'

hybr_waterfall_scrum_text = '<ul class="popover__message">' +
                                '<li>This hybridised solution adopts the strict Work Breakdown Structure (WBS) strategy of the Waterfall methodology along with the rapid sprint framework of the Scrum methodology</li>'+
                            '</ul>'

hybrid_scrum_kanban_text = '<ul class="popover__message">' +
                                '<li>This hybrid methodology is suitable for teams who require the structured process of the Scrum methodology with the visibility of the Kanban methodology</li>'+               
                                '</ul>'


function ShowMessageCn2() {

    var cn2 = document.getElementById('result_cn2').innerHTML;
    let text = ''

    if (cn2.startsWith("Scrum")) {
        text = scrum_text;
        //  block of code to be executed if condition1 is true
    } else if (cn2.startsWith("Waterfall")) {
        text = waterfall_text;
        //  block of code to be executed if the condition1 is false and condition2 is true
    } else if (cn2.includes("Kanban")) {
        text = kanban_text;

    } else if (cn2.includes("Spiral")) {
        text = spiral_text;

    } else if (cn2.includes("RAD")) {
        text = rad_text;

    } else if (cn2.includes("Hybrid: Scrum and Waterfall")) {
        text = hybr_waterfall_scrum_text;

    } else if (cn2.includes("Hybrid: Scrum and Kanban")) {
        text = hybrid_scrum_kanban_text;
    } 

    document.getElementById("wrapper_cn2").innerHTML = text
};

function ShowMessageKnn() {

    var knn = document.getElementById('result_knn').innerHTML;
    let textKnn = ''

    if (knn.startsWith("Scrum")) {
        textKnn = scrum_text;
        //  block of code to be executed if condition1 is true
    } else if (knn.startsWith("Waterfall")) {
        textKnn = waterfall_text;
        //  block of code to be executed if the condition1 is false and condition2 is true
    } else if (knn.includes("Kanban")) {
        textKnn = kanban_text;

    } else if (knn.includes("Spiral")) {
        textKnn = spiral_text;

    } else if (knn.includes("RAD")) {
        textKnn = rad_text;

    } else if (knn.includes("Hybrid: Scrum and Waterfall")) {
        textKnn = hybr_waterfall_scrum_text

    } else if (knn.includes("Hybrid: Scrum and Kanban")) {
        textKnn = hybrid_scrum_kanban_text;
    } 

    document.getElementById("wrapper_knn").innerHTML = textKnn
};

function ShowMessaged3() {

    var d3 = document.getElementById('result_d3').innerHTML;
    let textd3 = ''

    if (d3.startsWith("Scrum")) {
        textd3 = scrum_text;
        //  block of code to be executed if condition1 is true
    } else if (d3.startsWith("Waterfall")) {
        textd3 = waterfall_text;
        //  block of code to be executed if the condition1 is false and condition2 is true
    } else if (d3.includes("Kanban")) {
        textd3 = kanban_text;

    } else if (d3.includes("Spiral")) {
        textd3 = spiral_text;

    } else if (d3.includes("RAD")) {
        textd3 = rad_text;

    } else if (d3.includes("Hybrid: Scrum and Waterfall")) {
        textd3 = hybr_waterfall_scrum_text

    } else if (d3.includes("Hybrid: Scrum and Kanban")) {
        textd3 = hybrid_scrum_kanban_text;
    } 

    document.getElementById("wrapper_d3").innerHTML = textd3
};


ShowMessageCn2();
ShowMessageKnn();
ShowMessaged3();
