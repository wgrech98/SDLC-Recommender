$(document).ready(function() {
    $("[data-toggle='tooltip']").tooltip();
    $('#wrapper_1_cn2').show()
    $('#wrapper_another_cn2').hide()
    $('#wrapper_1_knn').show()
    $('#wrapper_another_knn').hide()
    $('#wrapper_1_d3').show()
    $('#wrapper_another_D3').hide()

    $('#NextBtnCN2').on('click', function(){
        $('#wrapper_another_cn2') == ShowMessageCn2()
        $('#wrapper_another_cn2').show()
        $('#wrapper_1_cn2').hide()
    });

    $('#BackBtnCN2').on('click', function(){
        $('#wrapper_1_cn2').show()
        $('#wrapper_another_cn2').hide()
    });

    $('#NextBtnKNN').on('click', function(){
        $('#wrapper_another_knn') == ShowMessageKnn()
        $('#wrapper_another_knn').show()
        $('#wrapper_1_knn').hide()
    });

    $('#BackBtnKNN').on('click', function(){
        $('#wrapper_1_knn').show()
        $('#wrapper_another_knn').hide()
    });
    
    $('#NextBtnD3').on('click', function(){
        $('#wrapper_another_D3') == ShowMessaged3()
        $('#wrapper_another_D3').show()
        $('#wrapper_1_d3').hide()
    });

    $('#BackBtnD3').on('click', function(){
        $('#wrapper_1_d3').show()
        $('#wrapper_another_D3').hide()
    });
});


scrum_text = 
            '<ul class="popover__message">' +
                '<li>Scrum employs an iterative and feedback strategy by adopting short development cycles referred to as sprints</li>'+
                '<li>Development tasks are undertaken according to priority from the sprint backlog </li>'+
                '<li>This strategy makes Scrum appropriate for dynamic customer requirements</li>'+
                '<li>Dynamic customer requirements, rapid delivery, continuous customer invovlement, and rapid software testing are some of the most important factors in this methodology</li>'+
            '</ul>'

waterfall_text =
                '<ul class="popover__message">' +
                    '<li>The Waterfall methodology is regarded as the methodology suitable for projects with stringent requirements</li>'+
                    '<li>Due to its rigidity, the model is easy to use and understand, and simple to coordinate</li>'+
                    '<li>Strict documentation practices, early defined and fixed requirements, minimal customer involvement during development of the product are some of the most important factors in this methodology</li>'+
                '</ul>'

kanban_text = 
                '<ul class="popover__message">' +
                    '<li>The Kanban approach falls under the agile methodology where work scheduling takes precedence over other factors</li>'+
                    '<li>Individual tasks are listed in the Kanban board according to their current progression to being completed </li>'+
                    '<li>Task visualisation, continuous testing, and project size are some of the most important factors in this methodology</li>'+
                '</ul>'

spiral_text = 
            '<ul class="popover__message">' +
                    '<li>A combination of the iterative development process and the Waterfall methodology</li>'+
                    '<li>Accounts for the risk factor in software projects. This is done through the rings in the spiral which are used to resemble every phase in the SD process</li>'+
                    '<li>In every stage of the spiral process, prototypes are designed for the client to test and identify risks during the development process, thus unknown risks are gradually reduced</li>'+
                '</ul>'

rad_text = 
            '<ul class="popover__message">' +
                '<li>Quick development, rapid delivery, and at minimum cost are some of the most important factors in this methodology</li>'+
                '<li>The project is split into sub-components to ease the process of modification during the development process</li>'+            
            '</ul>'

hybr_waterfall_scrum_text = 
                            '<ul class="popover__message">' +
                                '<li>This hybridised solution adopts the strict Work Breakdown Structure (WBS) strategy of the Waterfall methodology along with the rapid sprint framework of the Scrum methodology</li>'+
                                '<li>Suitable for organisations that wants to shift from Waterfall to Scrum</li>'+
                                '<li>Documentation, rapid delivery, and continuous customer invovlement are some of the most important factors in this methodology </li>'+
                            '</ul>'

hybrid_scrum_kanban_text = 
                            '<ul class="popover__message">' +
                                '<li>This hybrid methodology is suitable for teams who require the structured process of the Scrum methodology with the visibility of the Kanban methodology</li>'+               
                                '<li>Task visualisation, rapid delivery, and continuous customer invovlement are some of the most important factors in this methodology</li>'+
                            '</ul>'    


function ShowMessageCn2() {

    var cn2 = document.getElementById('result_cn2').innerHTML;

    if (cn2.startsWith("Scrum")) {
        text = scrum_text;
        //  block of code to be executed if condition1 is true
    } else if (cn2.startsWith("Waterfall")) {
        text = waterfall_text;
        //  block of code to be executed if the condition1 is false and condition2 is true
    } else if (cn2.startsWith("Kanban")) {
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

    document.getElementById("wrapper_cn2_message").innerHTML = text
};

function ShowMessageKnn() {

    var knn = document.getElementById('result_knn').innerHTML;

    if (knn.startsWith("Scrum")) {
        textKnn = scrum_text;
        //  block of code to be executed if condition1 is true
    } else if (knn.startsWith("Waterfall")) {
        textKnn = waterfall_text;
        //  block of code to be executed if the condition1 is false and condition2 is true
    } else if (knn.startsWith("Kanban")) {
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

    document.getElementById("wrapper_knn_message").innerHTML = textKnn
};

function ShowMessaged3() {

    var d3 = document.getElementById('result_d3').innerHTML;

    if (d3.startsWith("Scrum")) {
        textd3 = scrum_text;
        //  block of code to be executed if condition1 is true
    } else if (d3.startsWith("Waterfall")) {
        textd3 = waterfall_text;
        //  block of code to be executed if the condition1 is false and condition2 is true
    } else if (d3.startsWith("Kanban")) {
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

    document.getElementById("wrapper_d3_message").innerHTML = textd3
};
